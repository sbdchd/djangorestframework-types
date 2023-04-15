from collections import OrderedDict
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import (
    Any,
    TypeVar,
)

from django.db.models import Manager, Model, QuerySet
from rest_framework.fields import Field, Option
from rest_framework.request import Request

def method_overridden(method_name: str, klass: type, instance: Model) -> bool: ...

class ObjectValueError(ValueError): ...
class ObjectTypeError(TypeError): ...

class Hyperlink(str):
    def __new__(cls, url: str, obj: Any) -> Hyperlink: ...
    def __getnewargs__(self) -> None: ...  # type: ignore [override]
    @property
    def name(self) -> str: ...
    is_hyperlink: bool = ...

class PKOnlyObject:
    pk: Any = ...
    def __init__(self, pk: Any) -> None: ...

MANY_RELATION_KWARGS: Sequence[str]

_MT = TypeVar("_MT", bound=Model)

class RelatedField(Field[Any, Any, Any, Any]):
    queryset: QuerySet[Any] | Manager[Any] | None = ...
    html_cutoff: int | None = ...
    html_cutoff_text: str | None = ...
    def __init__(
        self,
        many: bool = ...,
        allow_empty: bool = ...,
        queryset: QuerySet[Any] | Manager[Any] | None = ...,
        html_cutoff: int | None = ...,
        html_cutoff_text: str = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Any = ...,
        source: Callable[..., Any] | str = ...,
        label: str | None = ...,
        help_text: str = ...,
        allow_null: bool = ...,
        validators: Sequence[Callable[..., Any]] | None = ...,
        error_messages: dict[str, str] | None = ...,
        style: dict[str, str] | None = ...,
    ): ...
    # mypy doesn't accept the typing below, although its accurate to what this class is doing, hence the ignore
    def __new__(cls, *args: Any, **kwargs: Any) -> RelatedField | ManyRelatedField: ...  # type: ignore
    @classmethod
    def many_init(cls, *args: Any, **kwargs: Any) -> ManyRelatedField: ...
    def get_queryset(self) -> QuerySet[Any]: ...
    def use_pk_only_optimization(self) -> bool: ...
    def get_choices(self, cutoff: int | None = ...) -> OrderedDict[Any, Any]: ...
    @property
    def choices(self) -> OrderedDict[Any, Any]: ...
    @property
    def grouped_choices(self) -> OrderedDict[Any, Any]: ...
    def iter_options(self) -> Iterable[Option]: ...
    def get_attribute(self, instance: Any) -> Any | None: ...
    def display_value(self, instance: Any) -> str: ...

class StringRelatedField(RelatedField): ...

class PrimaryKeyRelatedField(RelatedField):
    pk_field: str | None = ...
    def __init__(
        self,
        many: bool = ...,
        allow_empty: bool = ...,
        queryset: QuerySet[_MT] | Manager[_MT] | None = ...,
        html_cutoff: int | None = ...,
        html_cutoff_text: str = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Any = ...,
        source: Callable[..., Any] | str = ...,
        label: str | None = ...,
        help_text: str = ...,
        allow_null: bool = ...,
        validators: Sequence[Callable[..., Any]] | None = ...,
        error_messages: dict[str, str] | None = ...,
        style: dict[str, str] | None = ...,
        pk_field: str | Field[Any, Any, Any, Any] | None = ...,
    ): ...

class HyperlinkedRelatedField(RelatedField):
    reverse: Callable[..., Any] = ...
    lookup_field: str = ...
    lookup_url_kwarg: str = ...
    format: str | None = ...
    view_name: str | None = ...
    def __init__(
        self,
        many: bool = ...,
        allow_empty: bool = ...,
        queryset: QuerySet[_MT] | Manager[_MT] | None = ...,
        html_cutoff: int | None = ...,
        html_cutoff_text: str = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Any = ...,
        source: Callable[..., Any] | str = ...,
        label: str | None = ...,
        help_text: str = ...,
        allow_null: bool = ...,
        validators: Sequence[Callable[..., Any]] | None = ...,
        error_messages: dict[str, str] | None = ...,
        style: dict[str, str] | None = ...,
        view_name: str | None = ...,
        lookup_field: str | None = ...,
        lookup_url_kwarg: str | None = ...,
        format: str | None = ...,
    ): ...
    def get_object(self, view_name: str, *view_args: Any, **view_kwargs: Any) -> Any: ...
    def get_url(self, obj: Model, view_name: str, request: Request, format: str) -> str | None: ...

class HyperlinkedIdentityField(HyperlinkedRelatedField): ...

class SlugRelatedField(RelatedField):
    slug_field: str | None = ...
    def __init__(
        self,
        many: bool = ...,
        allow_empty: bool = ...,
        queryset: QuerySet[_MT] | Manager[_MT] | None = ...,
        html_cutoff: int | None = ...,
        html_cutoff_text: str = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: _MT | Callable[[Any], _MT] = ...,
        source: Callable[..., Any] | str = ...,
        label: str | None = ...,
        help_text: str = ...,
        allow_null: bool = ...,
        validators: Sequence[Callable[..., Any]] | None = ...,
        error_messages: dict[str, str] | None = ...,
        style: dict[str, str] | None = ...,
        slug_field: str | None = ...,
    ): ...
    def to_internal_value(self, data: Any) -> Any: ...
    def to_representation(self, value: Any) -> str: ...

class ManyRelatedField(Field[Sequence[Any], Sequence[Any], list[Any], Any]):
    default_empty_html: list[object] = ...
    html_cutoff: int | None = ...
    html_cutoff_text: str | None = ...
    child_relation: RelatedField = ...
    allow_empty: bool = ...
    def __init__(
        self,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Sequence[Any] = ...,
        initial: Sequence[Any] | Callable[[Any], Sequence[Any]] = ...,
        source: Callable[..., Any] | str = ...,
        label: str | None = ...,
        help_text: str | None = ...,
        style: dict[str, str] | None = ...,
        error_messages: dict[str, str] | None = ...,
        validators: Sequence[Callable[..., Any]] | None = ...,
        allow_null: bool = ...,
        child_relation: RelatedField = ...,
    ): ...
    def get_value(self, dictionary: Mapping[Any, Any]) -> list[Any]: ...
    def get_choices(self, cutoff: int | None = ...) -> OrderedDict[Any, Any]: ...
    @property
    def choices(self) -> OrderedDict[Any, Any]: ...
    @property
    def grouped_choices(self) -> OrderedDict[Any, Any]: ...
    def iter_options(self) -> Iterable[Option]: ...
