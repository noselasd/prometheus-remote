from prometheus import types_pb2 as _types_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WriteRequest(_message.Message):
    __slots__ = ("timeseries", "metadata")
    TIMESERIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    timeseries: _containers.RepeatedCompositeFieldContainer[_types_pb2.TimeSeries]
    metadata: _containers.RepeatedCompositeFieldContainer[_types_pb2.MetricMetadata]
    def __init__(self, timeseries: _Optional[_Iterable[_Union[_types_pb2.TimeSeries, _Mapping]]] = ..., metadata: _Optional[_Iterable[_Union[_types_pb2.MetricMetadata, _Mapping]]] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("queries", "accepted_response_types")
    class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SAMPLES: _ClassVar[ReadRequest.ResponseType]
        STREAMED_XOR_CHUNKS: _ClassVar[ReadRequest.ResponseType]
    SAMPLES: ReadRequest.ResponseType
    STREAMED_XOR_CHUNKS: ReadRequest.ResponseType
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_RESPONSE_TYPES_FIELD_NUMBER: _ClassVar[int]
    queries: _containers.RepeatedCompositeFieldContainer[Query]
    accepted_response_types: _containers.RepeatedScalarFieldContainer[ReadRequest.ResponseType]
    def __init__(self, queries: _Optional[_Iterable[_Union[Query, _Mapping]]] = ..., accepted_response_types: _Optional[_Iterable[_Union[ReadRequest.ResponseType, str]]] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[QueryResult]
    def __init__(self, results: _Optional[_Iterable[_Union[QueryResult, _Mapping]]] = ...) -> None: ...

class Query(_message.Message):
    __slots__ = ("start_timestamp_ms", "end_timestamp_ms", "matchers", "hints")
    START_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    MATCHERS_FIELD_NUMBER: _ClassVar[int]
    HINTS_FIELD_NUMBER: _ClassVar[int]
    start_timestamp_ms: int
    end_timestamp_ms: int
    matchers: _containers.RepeatedCompositeFieldContainer[_types_pb2.LabelMatcher]
    hints: _types_pb2.ReadHints
    def __init__(self, start_timestamp_ms: _Optional[int] = ..., end_timestamp_ms: _Optional[int] = ..., matchers: _Optional[_Iterable[_Union[_types_pb2.LabelMatcher, _Mapping]]] = ..., hints: _Optional[_Union[_types_pb2.ReadHints, _Mapping]] = ...) -> None: ...

class QueryResult(_message.Message):
    __slots__ = ("timeseries",)
    TIMESERIES_FIELD_NUMBER: _ClassVar[int]
    timeseries: _containers.RepeatedCompositeFieldContainer[_types_pb2.TimeSeries]
    def __init__(self, timeseries: _Optional[_Iterable[_Union[_types_pb2.TimeSeries, _Mapping]]] = ...) -> None: ...

class ChunkedReadResponse(_message.Message):
    __slots__ = ("chunked_series", "query_index")
    CHUNKED_SERIES_FIELD_NUMBER: _ClassVar[int]
    QUERY_INDEX_FIELD_NUMBER: _ClassVar[int]
    chunked_series: _containers.RepeatedCompositeFieldContainer[_types_pb2.ChunkedSeries]
    query_index: int
    def __init__(self, chunked_series: _Optional[_Iterable[_Union[_types_pb2.ChunkedSeries, _Mapping]]] = ..., query_index: _Optional[int] = ...) -> None: ...
