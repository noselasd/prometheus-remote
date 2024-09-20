from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricMetadata(_message.Message):
    __slots__ = ("type", "metric_family_name", "help", "unit")
    class MetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[MetricMetadata.MetricType]
        COUNTER: _ClassVar[MetricMetadata.MetricType]
        GAUGE: _ClassVar[MetricMetadata.MetricType]
        HISTOGRAM: _ClassVar[MetricMetadata.MetricType]
        GAUGEHISTOGRAM: _ClassVar[MetricMetadata.MetricType]
        SUMMARY: _ClassVar[MetricMetadata.MetricType]
        INFO: _ClassVar[MetricMetadata.MetricType]
        STATESET: _ClassVar[MetricMetadata.MetricType]
    UNKNOWN: MetricMetadata.MetricType
    COUNTER: MetricMetadata.MetricType
    GAUGE: MetricMetadata.MetricType
    HISTOGRAM: MetricMetadata.MetricType
    GAUGEHISTOGRAM: MetricMetadata.MetricType
    SUMMARY: MetricMetadata.MetricType
    INFO: MetricMetadata.MetricType
    STATESET: MetricMetadata.MetricType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METRIC_FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    type: MetricMetadata.MetricType
    metric_family_name: str
    help: str
    unit: str
    def __init__(self, type: _Optional[_Union[MetricMetadata.MetricType, str]] = ..., metric_family_name: _Optional[str] = ..., help: _Optional[str] = ..., unit: _Optional[str] = ...) -> None: ...

class Sample(_message.Message):
    __slots__ = ("value", "timestamp")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    value: float
    timestamp: int
    def __init__(self, value: _Optional[float] = ..., timestamp: _Optional[int] = ...) -> None: ...

class Exemplar(_message.Message):
    __slots__ = ("labels", "value", "timestamp")
    LABELS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[Label]
    value: float
    timestamp: int
    def __init__(self, labels: _Optional[_Iterable[_Union[Label, _Mapping]]] = ..., value: _Optional[float] = ..., timestamp: _Optional[int] = ...) -> None: ...

class Histogram(_message.Message):
    __slots__ = ("count_int", "count_float", "sum", "schema", "zero_threshold", "zero_count_int", "zero_count_float", "negative_spans", "negative_deltas", "negative_counts", "positive_spans", "positive_deltas", "positive_counts", "reset_hint", "timestamp")
    class ResetHint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Histogram.ResetHint]
        YES: _ClassVar[Histogram.ResetHint]
        NO: _ClassVar[Histogram.ResetHint]
        GAUGE: _ClassVar[Histogram.ResetHint]
    UNKNOWN: Histogram.ResetHint
    YES: Histogram.ResetHint
    NO: Histogram.ResetHint
    GAUGE: Histogram.ResetHint
    COUNT_INT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ZERO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ZERO_COUNT_INT_FIELD_NUMBER: _ClassVar[int]
    ZERO_COUNT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_SPANS_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_DELTAS_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_SPANS_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_DELTAS_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    RESET_HINT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    count_int: int
    count_float: float
    sum: float
    schema: int
    zero_threshold: float
    zero_count_int: int
    zero_count_float: float
    negative_spans: _containers.RepeatedCompositeFieldContainer[BucketSpan]
    negative_deltas: _containers.RepeatedScalarFieldContainer[int]
    negative_counts: _containers.RepeatedScalarFieldContainer[float]
    positive_spans: _containers.RepeatedCompositeFieldContainer[BucketSpan]
    positive_deltas: _containers.RepeatedScalarFieldContainer[int]
    positive_counts: _containers.RepeatedScalarFieldContainer[float]
    reset_hint: Histogram.ResetHint
    timestamp: int
    def __init__(self, count_int: _Optional[int] = ..., count_float: _Optional[float] = ..., sum: _Optional[float] = ..., schema: _Optional[int] = ..., zero_threshold: _Optional[float] = ..., zero_count_int: _Optional[int] = ..., zero_count_float: _Optional[float] = ..., negative_spans: _Optional[_Iterable[_Union[BucketSpan, _Mapping]]] = ..., negative_deltas: _Optional[_Iterable[int]] = ..., negative_counts: _Optional[_Iterable[float]] = ..., positive_spans: _Optional[_Iterable[_Union[BucketSpan, _Mapping]]] = ..., positive_deltas: _Optional[_Iterable[int]] = ..., positive_counts: _Optional[_Iterable[float]] = ..., reset_hint: _Optional[_Union[Histogram.ResetHint, str]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class BucketSpan(_message.Message):
    __slots__ = ("offset", "length")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class TimeSeries(_message.Message):
    __slots__ = ("labels", "samples", "exemplars", "histograms")
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    EXEMPLARS_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAMS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[Label]
    samples: _containers.RepeatedCompositeFieldContainer[Sample]
    exemplars: _containers.RepeatedCompositeFieldContainer[Exemplar]
    histograms: _containers.RepeatedCompositeFieldContainer[Histogram]
    def __init__(self, labels: _Optional[_Iterable[_Union[Label, _Mapping]]] = ..., samples: _Optional[_Iterable[_Union[Sample, _Mapping]]] = ..., exemplars: _Optional[_Iterable[_Union[Exemplar, _Mapping]]] = ..., histograms: _Optional[_Iterable[_Union[Histogram, _Mapping]]] = ...) -> None: ...

class Label(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Labels(_message.Message):
    __slots__ = ("labels",)
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[Label]
    def __init__(self, labels: _Optional[_Iterable[_Union[Label, _Mapping]]] = ...) -> None: ...

class LabelMatcher(_message.Message):
    __slots__ = ("type", "name", "value")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EQ: _ClassVar[LabelMatcher.Type]
        NEQ: _ClassVar[LabelMatcher.Type]
        RE: _ClassVar[LabelMatcher.Type]
        NRE: _ClassVar[LabelMatcher.Type]
    EQ: LabelMatcher.Type
    NEQ: LabelMatcher.Type
    RE: LabelMatcher.Type
    NRE: LabelMatcher.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: LabelMatcher.Type
    name: str
    value: str
    def __init__(self, type: _Optional[_Union[LabelMatcher.Type, str]] = ..., name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ReadHints(_message.Message):
    __slots__ = ("step_ms", "func", "start_ms", "end_ms", "grouping", "by", "range_ms")
    STEP_MS_FIELD_NUMBER: _ClassVar[int]
    FUNC_FIELD_NUMBER: _ClassVar[int]
    START_MS_FIELD_NUMBER: _ClassVar[int]
    END_MS_FIELD_NUMBER: _ClassVar[int]
    GROUPING_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    RANGE_MS_FIELD_NUMBER: _ClassVar[int]
    step_ms: int
    func: str
    start_ms: int
    end_ms: int
    grouping: _containers.RepeatedScalarFieldContainer[str]
    by: bool
    range_ms: int
    def __init__(self, step_ms: _Optional[int] = ..., func: _Optional[str] = ..., start_ms: _Optional[int] = ..., end_ms: _Optional[int] = ..., grouping: _Optional[_Iterable[str]] = ..., by: bool = ..., range_ms: _Optional[int] = ...) -> None: ...

class Chunk(_message.Message):
    __slots__ = ("min_time_ms", "max_time_ms", "type", "data")
    class Encoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Chunk.Encoding]
        XOR: _ClassVar[Chunk.Encoding]
        HISTOGRAM: _ClassVar[Chunk.Encoding]
        FLOAT_HISTOGRAM: _ClassVar[Chunk.Encoding]
    UNKNOWN: Chunk.Encoding
    XOR: Chunk.Encoding
    HISTOGRAM: Chunk.Encoding
    FLOAT_HISTOGRAM: Chunk.Encoding
    MIN_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    min_time_ms: int
    max_time_ms: int
    type: Chunk.Encoding
    data: bytes
    def __init__(self, min_time_ms: _Optional[int] = ..., max_time_ms: _Optional[int] = ..., type: _Optional[_Union[Chunk.Encoding, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class ChunkedSeries(_message.Message):
    __slots__ = ("labels", "chunks")
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[Label]
    chunks: _containers.RepeatedCompositeFieldContainer[Chunk]
    def __init__(self, labels: _Optional[_Iterable[_Union[Label, _Mapping]]] = ..., chunks: _Optional[_Iterable[_Union[Chunk, _Mapping]]] = ...) -> None: ...
