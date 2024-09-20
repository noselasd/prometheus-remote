from datetime import  datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from prometheus.remote_pb2 import ReadRequest, ReadResponse, Query, QueryResult
from prometheus.types_pb2 import Sample, TimeSeries, Label, LabelMatcher
import snappy
import polars as pl
class HTTPRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler with additional properties and functions."""

    def do_GET(self):
        """handle GET requests."""
        self.send_response(200, "ok")
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        body = snappy.decompress(body)
        print(f'POST to {self.path}:\n', body)
        request = ReadRequest()
        i = request.ParseFromString(body)
        print(f'read {i=} from {request}')

        read_response = ReadResponse()
        for q in request.queries:
            qres = self.query_handler(q)
            read_response.results.append(qres)
       # print("Sending response:\n", read_response)

        response = snappy.compress(read_response.SerializeToString())
        self.send_response(200)
        self.send_header('Content-Length', str(len(response)))
        self.send_header('Content-Encoding', "snappy")
        self.send_header('Content-Type', "application/x-protobuf")
        self.end_headers()

        self.wfile.write(response)

    # Sample query:
    # sip_analysis_rolling_1h{   external="true",
    #                            metric="n_calls",
    #                            aggregation="anr_label_country",
    #                            anr_label_country=~"A.*",
    #
    # }
    # We could even filter on other metric columns in our table too e.g. n_hangup>0

    def query_handler(self, q : Query) -> QueryResult:
        ldf = pl.scan_parquet("./data/*.parquet")
        series = next((m for m in q.matchers if m.name == "__name__"), None)
        # promql have to filter on aggregation and metric name
        aggregation = next((m for m in q.matchers if m.name == "aggregation"), None)
        metric = next((m for m in q.matchers if m.name == "metric"), None)

        columns = ldf.collect_schema().names()
        result = QueryResult()
        if series is None or aggregation is None or metric is None:
            return result
        if aggregation.value not in columns:
            return result
        if metric.value not in columns:
            return result
        for m in q.matchers:
            # metric: our defined name for the metric column (e.g. n_calls)
            # aggregation: our defined name for the aggregation dataset (e.g. anr_label_country)
            # external: label added in prometheus.yml so prometheus routes queries to us
            # __name__: Prometheus passes the metric name as a lable (this also means
            #           prometheus can do e.g. a regexp filter on it in query). The PromQL:
            #           sip_analysis_rolling_1h{external="true",
            #                                   metric="n_calls",
            #                                   aggregation="anr_label_country"}
            #           is the same as
            #                               {   __name__=sip_analysis_rolling_1h,
            #                                   external="true",
            #                                   metric="n_calls",
            #                                   aggregation="anr_label_country"}
            # This code ignores the metric name for now...

            if m.name in ('metric', "__name__", "aggregation", "external"):
                continue
            match m.type:
                case LabelMatcher.NEQ:
                    ldf = ldf.filter(pl.col(m.name) != m.value)
                case LabelMatcher.EQ:
                    ldf = ldf.filter(pl.col(m.name) == m.value)
                case LabelMatcher.RE:
                    ldf = ldf.filter(pl.col(m.name).str.contains(m.value))
                case LabelMatcher.NRE:
                    ldf = ldf.filter(~pl.col(m.name).str.contains(m.value))

        ldf = ldf.select(pl.col('timestamp'), pl.col('aggregation'), pl.col(metric.value), pl.col(aggregation.value))

        begin = datetime.fromtimestamp(q.start_timestamp_ms/1000)
        end =  datetime.fromtimestamp(q.end_timestamp_ms/1000)
        print("begin", begin, "end", end)
        ldf = ldf.filter(pl.col("timestamp") >= begin)
        ldf = ldf.filter(pl.col("timestamp") <= end)

        dict_dfs = ldf.collect().partition_by(aggregation.value,"aggregation", as_dict=True, include_key=False)
        for k,df in dict_dfs.items():
            ts = TimeSeries()
            ts.labels.append(Label(name = '__name__', value = series.value))
            ts.labels.append(Label(name = aggregation.value, value = str(k[0])))
            ts.labels.append(Label(name = 'aggregation', value = str(k[1])))

            for row in df.sort('timestamp').iter_rows(): # Timestamps MUST be sorted..
                ts.samples.append(Sample(value = row[1], timestamp = int(row[0].timestamp() * 1000)))
            result.timeseries.append(ts)
        return result








httpd = HTTPServer(('',8088), HTTPRequestHandler)
httpd.serve_forever()

# PromQL: anr_label_country{external="true", metric="n_hangup"}
