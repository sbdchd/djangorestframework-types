import datetime
import uuid
from collections import OrderedDict
from collections.abc import (
    Callable,
    Generator,
    Iterable,
    Mapping,
    MutableMapping,
    Sequence,
)
from decimal import Decimal
from enum import Enum
from json import JSONDecoder, JSONEncoder
from re import Pattern
from typing import (
    Any,
    Final,
    Generic,
    Literal,
    NoReturn,
    Optional,
    Protocol,
    TypeVar,
    Union,
)

from django.core.files.base import File
from django.db import models
from rest_framework.serializers import BaseSerializer

class _Empty(Enum):
    sentinel: Literal[0]

empty: Final[Literal[_Empty.sentinel]]

class BuiltinSignatureError(Exception): ...

class CreateOnlyDefault:
    requires_context: bool = ...
    default: Any = ...
    def __init__(self, default: Any) -> None: ...
    def __call__(self, serializer_field: Field[Any, Any, Any, Any]) -> Any: ...

class CurrentUserDefault:
    requires_context: bool = ...
    def __call__(self, serializer_field: Field[Any, Any, Any, Any]) -> Any: ...

class SkipField(Exception): ...

class Option(Protocol):
    start_option_group: bool = ...
    end_option_group: bool = ...
    label: str
    value: str
    display_text: str

def is_simple_callable(obj: Callable[..., Any]) -> bool: ...
def get_attribute(instance: Any, attrs: list[str] | None) -> Any: ...
def set_value(dictionary: MutableMapping[str, Any], keys: Sequence[str], value: Any) -> None: ...
def to_choices_dict(choices: Sequence[Any]) -> OrderedDict[Any, Any]: ...
def flatten_choices_dict(choices: dict[Any, Any]) -> OrderedDict[Any, Any]: ...
def iter_options(
    grouped_choices: OrderedDict[Any, Any], cutoff: int | None = ..., cutoff_text: str | None = ...
) -> Generator[Option, None, None]: ...
def get_error_detail(exc_info: Any) -> Any: ...

REGEX_TYPE: Pattern[str]
NOT_READ_ONLY_WRITE_ONLY: str
NOT_READ_ONLY_REQUIRED: str
NOT_REQUIRED_DEFAULT: str
USE_READONLYFIELD: str
MISSING_ERROR_MESSAGE: str

_IN = TypeVar("_IN")  # Instance Type
_VT = TypeVar("_VT")  # Value Type
_DT = TypeVar("_DT")  # Data Type
_RP = TypeVar("_RP")  # Representation Type

class SupportsToPython(Protocol):
    def to_python(self, value: Any) -> Any: ...

_DefaultInitial = Union[_VT, Callable[[], _VT], None, _Empty]

class Field(Generic[_VT, _DT, _RP, _IN]):
    """
    Type arguments:
    - _VT: The data type which the validated data will be represented as
    - _DT: The type which unserialized data will be before being transformed into _VT
    - _RT: A primitive type (ex., str or int) which can be used to represent the field's serialized and validated value (Similar to repr())
    - _IN: Type of an instance of this field class
    """

    allow_null: bool = ...
    default: _VT | None = ...
    default_empty_html: Any = ...
    default_error_messages: dict[str, str] = ...
    default_validators: list[Callable[..., Any]] = ...
    error_messages: dict[str, str] = ...
    field_name: str | None = ...
    help_text: str | None = ...
    initial: _VT | Callable[[], _VT] | None = ...
    # NOTE(sbdchd): I made some of these Any so that when declaring a field on
    # a serializer with the same name we don't get a type error.
    label: Any
    parent: BaseSerializer
    read_only: bool
    required: Any
    source: Any
    source_attrs: list[str] = ...
    style: dict[str, Any]
    write_only: bool
    def __init__(
        self,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[_VT] = ...,
        initial: _DefaultInitial[_VT] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...
    def bind(self, field_name: str, parent: BaseSerializer) -> None: ...
    @property
    def validators(self) -> list[Callable[..., Any]]: ...
    @validators.setter
    def validators(self, validators: list[Callable[..., Any]]) -> None: ...
    def get_validators(self) -> list[Callable[..., Any]]: ...
    def get_initial(self) -> _VT | None: ...
    def get_value(self, dictionary: Mapping[Any, Any]) -> Any: ...
    def get_attribute(self, instance: _IN) -> _RP | None: ...
    def get_default(self) -> _VT | None: ...
    def validate_empty_values(self, data: Any) -> tuple[bool, Any]: ...
    def run_validation(self, data: Any = ...) -> Any: ...
    def run_validators(self, value: Any) -> None: ...
    def to_internal_value(self, data: _DT) -> _VT: ...
    def to_representation(self, value: _VT) -> _RP: ...
    def fail(self, key: str, **kwargs: Any) -> NoReturn: ...
    @property
    def root(self) -> BaseSerializer: ...
    @property
    def context(self) -> dict[str, Any]: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> Field[Any, Any, Any, Any]: ...
    def __deepcopy__(self, memo: Mapping[Any, Any]) -> Field[Any, Any, Any, Any]: ...

class BooleanField(
    Field[
        bool,
        Union[
            bool,
            None,
            Literal["t"],
            Literal["T"],
            Literal["y"],
            Literal["Y"],
            Literal["yes"],
            Literal["YES"],
            Literal["true"],
            Literal["True"],
            Literal["TRUE"],
            Literal["on"],
            Literal["On"],
            Literal["ON"],
            Literal["1"],
            Literal[1],
            Literal["f"],
            Literal["F"],
            Literal["n"],
            Literal["N"],
            Literal["no"],
            Literal["NO"],
            Literal["false"],
            Literal["False"],
            Literal["FALSE"],
            Literal["off"],
            Literal["Off"],
            Literal["OFF"],
            Literal["0"],
            Literal[0],
        ],
        bool,
        Any,
    ]
):
    TRUE_VALUES: set[str | bool | int] = ...
    FALSE_VALUES: set[str | bool | int | float] = ...
    NULL_VALUES: set[str | None] = ...

class NullBooleanField(
    Field[
        Union[bool, None],
        Union[
            bool,
            None,
            Literal["t"],
            Literal["T"],
            Literal["y"],
            Literal["Y"],
            Literal["yes"],
            Literal["YES"],
            Literal["true"],
            Literal["True"],
            Literal["TRUE"],
            Literal["on"],
            Literal["On"],
            Literal["ON"],
            Literal["1"],
            Literal[1],
            Literal["f"],
            Literal["F"],
            Literal["n"],
            Literal["N"],
            Literal["no"],
            Literal["NO"],
            Literal["false"],
            Literal["False"],
            Literal["FALSE"],
            Literal["off"],
            Literal["Off"],
            Literal["OFF"],
            Literal["0"],
            Literal[0],
            Literal["null"],
            Literal["Null"],
            Literal["NULL"],
            Literal[""],
        ],
        bool,
        Any,
    ]
):
    TRUE_VALUES: set[str | bool | int] = ...
    FALSE_VALUES: set[str | bool | int | float] = ...
    NULL_VALUES: set[str | None] = ...

class CharField(Field[str, str, str, Any]):
    allow_blank: bool = ...
    trim_whitespace: bool = ...
    max_length: int | None = ...
    min_length: int | None = ...
    def __init__(
        self,
        *,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[str] = ...,
        initial: _DefaultInitial[str] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        allow_blank: bool = ...,
        trim_whitespace: bool = ...,
        max_length: int = ...,
        min_length: int | None = ...,
    ): ...

class EmailField(CharField): ...

class RegexField(CharField):
    def __init__(
        self,
        regex: str | Pattern[str],
        *,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[str] = ...,
        initial: _DefaultInitial[str] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        allow_blank: bool = ...,
        trim_whitespace: bool = ...,
        max_length: int = ...,
        min_length: int | None = ...,
    ): ...

class SlugField(CharField):
    allow_unicode: bool = ...
    def __init__(
        self,
        allow_unicode: bool = ...,
        *,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[str] = ...,
        initial: _DefaultInitial[str] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        allow_blank: bool = ...,
        trim_whitespace: bool = ...,
        max_length: int = ...,
        min_length: int | None = ...,
    ): ...

class URLField(CharField): ...

class UUIDField(Field[uuid.UUID, Union[uuid.UUID, str, int], str, Any]):
    valid_formats: Sequence[str] = ...
    uuid_format: str
    def __init__(
        self,
        *,
        format: str | None = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[uuid.UUID] = ...,
        initial: _DefaultInitial[uuid.UUID] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...

class IPAddressField(CharField):
    protocol: str
    unpack_ipv4: bool
    def __init__(
        self,
        protocol: str = ...,
        *,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[str] = ...,
        initial: _DefaultInitial[str] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        allow_blank: bool = ...,
        trim_whitespace: bool = ...,
        max_length: int = ...,
        min_length: int | None = ...,
    ): ...

class IntegerField(Field[int, Union[float, int, str], int, Any]):
    MAX_STRING_LENGTH: int = ...
    re_decimal: Pattern[str] = ...
    max_value: int | None = ...
    min_value: int | None = ...
    def __init__(
        self,
        *,
        max_value: int | None = ...,
        min_value: int | None = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[int] = ...,
        initial: _DefaultInitial[int] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...

class FloatField(Field[float, Union[float, int, str], str, Any]):
    MAX_STRING_LENGTH: int = ...
    re_decimal: Pattern[str] = ...
    max_value: float | None = ...
    min_value: float | None = ...
    def __init__(
        self,
        *,
        max_value: float = ...,
        min_value: float = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[float] = ...,
        initial: _DefaultInitial[float] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...

class DecimalField(Field[Decimal, Union[int, float, str, Decimal], str, Any]):
    MAX_STRING_LENGTH: int = ...
    max_digits: int | None
    decimal_places: int | None
    coerce_to_string: bool | None
    max_value: Decimal | int | float | None
    min_value: Decimal | int | float | None
    localize: bool
    rounding: str | None
    max_whole_digits = Optional[int]
    def __init__(
        self,
        max_digits: int | None,
        decimal_places: int | None,
        coerce_to_string: bool = ...,
        max_value: Decimal | int | float = ...,
        min_value: Decimal | int | float = ...,
        localize: bool = ...,
        rounding: str | None = ...,
        *,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[Decimal] = ...,
        initial: _DefaultInitial[Decimal] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...
    def validate_precision(self, value: Decimal) -> Decimal: ...
    def quantize(self, value: Decimal) -> Decimal: ...

class DateTimeField(Field[datetime.datetime, Union[datetime.datetime, str], str, Any]):
    datetime_parser: Callable[[str, str], datetime.datetime] = ...
    format: str | None = ...
    input_formats: Sequence[str] = ...
    timezone: datetime.tzinfo = ...
    def __init__(
        self,
        format: str | None = ...,
        input_formats: Sequence[str] = ...,
        default_timezone: datetime.tzinfo | None = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[datetime.datetime] = ...,
        initial: _DefaultInitial[datetime.datetime] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...
    def enforce_timezone(self, value: datetime.datetime) -> datetime.datetime: ...
    def default_timezone(self) -> str | None: ...

class DateField(Field[datetime.date, Union[datetime.date, str], str, Any]):
    datetime_parser: Callable[[str, str], datetime.datetime] = ...
    format: str | None = ...
    input_formats: Sequence[str] = ...
    def __init__(
        self,
        format: str | None = ...,
        input_formats: Sequence[str] = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[datetime.date] = ...,
        initial: _DefaultInitial[datetime.date] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...

class TimeField(Field[datetime.time, Union[datetime.time, str], str, Any]):
    datetime_parser: Callable[[str, str], datetime.datetime] = ...
    format: str | None = ...
    input_formats: Sequence[str] = ...
    def __init__(
        self,
        format: str | None = ...,
        input_formats: Sequence[str] = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[datetime.time] = ...,
        initial: _DefaultInitial[datetime.time] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...

class DurationField(Field[datetime.timedelta, Union[datetime.timedelta, str], str, Any]):
    max_value: datetime.timedelta | None = ...
    min_value: datetime.timedelta | None = ...
    def __init__(
        self,
        *,
        max_value: datetime.timedelta | int | float = ...,
        min_value: datetime.timedelta | int | float = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[datetime.timedelta] = ...,
        initial: _DefaultInitial[datetime.timedelta] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...

class ChoiceField(Field[str, Union[str, int, tuple[str | int, str | int | tuple[Any, ...]]], str, Any]):
    html_cutoff: int | None = ...
    html_cutoff_text: str | None = ...
    allow_blank: bool = ...
    grouped_choices: OrderedDict[Any, Any] = ...
    choice_strings_to_values: dict[str, Any] = ...
    _choices: OrderedDict[Any, Any] = ...
    def __init__(
        self,
        choices: Sequence[Any],
        *,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _Empty | str | int | Callable[[], str] | Callable[[], int] = ...,
        initial: _Empty | str | int | Callable[[], str] | Callable[[], int] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        html_cutoff: int = ...,
        html_cutoff_text: str = ...,
        allow_blank: bool = ...,
    ): ...
    def iter_options(self) -> Iterable[Option]: ...
    def _get_choices(self) -> dict[Any, Any]: ...
    def _set_choices(self, choices: Sequence[Any]) -> None: ...
    choices = property(_get_choices, _set_choices)

class MultipleChoiceField(
    ChoiceField,
    Field[
        str,
        Sequence[str | int | tuple[str | int, str | int]],
        Sequence[str | tuple[str | int, str | int]],
        Any,
    ],
):
    allow_empty: bool = ...
    def __init__(
        self,
        choices: Sequence[Any],
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _Empty
        | Sequence[str]
        | Sequence[int]
        | Callable[[], Sequence[str]]
        | Callable[[], Sequence[int]] = ...,
        initial: _Empty
        | Sequence[str]
        | Sequence[int]
        | Callable[[], Sequence[str]]
        | Callable[[], Sequence[int]] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        html_cutoff: int = ...,
        html_cutoff_text: str = ...,
        allow_blank: bool = ...,
        allow_empty: bool = ...,
    ): ...

class FilePathField(ChoiceField):
    def __init__(
        self,
        path: str,
        match: str = ...,
        recursive: bool = ...,
        allow_files: bool = ...,
        allow_folders: bool = ...,
        required: bool = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        default: _Empty | str | int | Callable[[], str] | Callable[[], int] = ...,
        initial: _Empty | str | int | Callable[[], str] | Callable[[], int] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        html_cutoff: int = ...,
        html_cutoff_text: str = ...,
        allow_blank: bool = ...,
    ): ...

class FileField(Field[File, File, Union[str, None], Any]):  # this field can return None without raising!
    max_length: int = ...
    allow_empty_file: bool = ...
    use_url: bool = ...
    def __init__(
        self,
        *,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _Empty | File | Callable[[], File] = ...,
        initial: _Empty | File | Callable[[], File] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        max_length: int = ...,
        allow_empty_file: bool = ...,
        use_url: bool = ...,
    ): ...

class ImageField(FileField):
    _DjangoImageField: SupportsToPython = ...
    def __init__(
        self,
        *,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _Empty | File | Callable[[], File] = ...,
        initial: _Empty | File | Callable[[], File] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        max_length: int = ...,
        allow_empty_file: bool = ...,
        use_url: bool = ...,
        _DjangoImageField: type[SupportsToPython] = ...,
    ): ...

class _UnvalidatedField(Field[Any, Any, Any, Any]): ...

class ListField(Field[list[Any], list[Any], list[Any], Any]):
    child: Field[Any, Any, Any, Any] = ...
    allow_empty: bool = ...
    max_length: int | None = ...
    min_length: int | None = ...
    def __init__(
        self,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _Empty | list[Any] | Callable[[], list[Any]] = ...,
        initial: _Empty | list[Any] | Callable[[], list[Any]] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        *,
        child: Field[Any, Any, Any, Any] = ...,
        allow_empty: bool = ...,
        max_length: int = ...,
        min_length: int = ...,
    ): ...
    def run_child_validation(self, data: list[Mapping[Any, Any]]) -> Any: ...

class DictField(Field[dict[Any, Any], dict[Any, Any], dict[Any, Any], Any]):
    child: Field[Any, Any, Any, Any] = ...
    allow_empty: bool = ...
    def __init__(
        self,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _Empty | dict[Any, Any] | Callable[[], dict[Any, Any]] = ...,
        initial: _Empty | dict[Any, Any] | Callable[[], dict[Any, Any]] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        *,
        child: Field[Any, Any, Any, Any] = ...,
        allow_empty: bool = ...,
    ): ...
    def run_child_validation(self, data: Any) -> Any: ...

class HStoreField(DictField):
    child: CharField = ...

class JSONField(
    Field[Union[dict[str, Any], list[dict[str, Any]]], Union[dict[str, Any], list[dict[str, Any]]], str, Any]
):
    binary: bool = ...
    encoder: JSONEncoder | None = ...
    decoder: JSONDecoder | None = ...
    def __init__(
        self,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _Empty | Mapping[Any, Any] | Callable[[], Mapping[Any, Any]] = ...,
        initial: _Empty | Mapping[Any, Any] | Callable[[], Mapping[Any, Any]] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        *,
        binary: bool = ...,
        encoder: JSONEncoder = ...,
        decoder: JSONDecoder = ...,
    ): ...

class ReadOnlyField(Field[Any, Any, Any, Any]): ...
class HiddenField(Field[Any, Any, Any, Any]): ...

class SerializerMethodField(Field[Any, Any, Any, Any]):
    method_name: str = ...
    def __init__(
        self,
        method_name: str = ...,
        *,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Any = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...

class ModelField(Field[Any, Any, Any, Any]):
    model_field: models.Field[Any, Any] = ...
    max_length: int = ...
    def __init__(
        self,
        model_field: models.Field[Any, Any],
        *,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Any = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        max_length: int = ...,
    ): ...
