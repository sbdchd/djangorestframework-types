from collections.abc import Callable, Mapping, Sequence
from typing import (
    Any,
    Literal,
    Optional,
    Protocol,
    TypeVar,
)

from django.db.models import QuerySet
from django.http.response import HttpResponseBase
from rest_framework.authentication import BaseAuthentication
from rest_framework.filters import FilterBackendProtocol
from rest_framework.parsers import BaseParser
from rest_framework.permissions import _PermissionClass
from rest_framework.renderers import BaseRenderer
from rest_framework.schemas.inspectors import ViewInspector
from rest_framework.serializers import BaseSerializer
from rest_framework.throttling import BaseThrottle

class MethodMapper(dict[str, Any]):
    def __init__(self, action: Callable[..., Any], methods: Sequence[str]) -> None: ...
    def _map(self, method: str, func: Callable[..., Any]) -> Callable[..., Any]: ...
    def get(self, func: Callable[..., Any]) -> Callable[..., Any]: ...  # type: ignore
    def post(self, func: Callable[..., Any]) -> Callable[..., Any]: ...
    def put(self, func: Callable[..., Any]) -> Callable[..., Any]: ...
    def patch(self, func: Callable[..., Any]) -> Callable[..., Any]: ...
    def delete(self, func: Callable[..., Any]) -> Callable[..., Any]: ...
    def head(self, func: Callable[..., Any]) -> Callable[..., Any]: ...
    def options(self, func: Callable[..., Any]) -> Callable[..., Any]: ...
    def trace(self, func: Callable[..., Any]) -> Callable[..., Any]: ...

_LOWER_CASE_HTTP_VERBS = list[
    Literal["get"]
    | Literal["post"]
    | Literal["delete"]
    | Literal["put"]
    | Literal["patch"]
    | Literal["trace"]
    | Literal["options"]
]

_MIXED_CASE_HTTP_VERBS = Sequence[
    Literal["GET"]
    | Literal["POST"]
    | Literal["DELETE"]
    | Literal["PUT"]
    | Literal["PATCH"]
    | Literal["TRACE"]
    | Literal["OPTIONS"]
    | Literal["get"]
    | Literal["post"]
    | Literal["delete"]
    | Literal["put"]
    | Literal["patch"]
    | Literal["trace"]
    | Literal["options"]
]

_CallableViewHandler = Callable[..., HttpResponseBase]
_F = TypeVar("_F", bound=_CallableViewHandler)

class ViewSetAction(Protocol[_F]):
    detail: bool
    methods: _LOWER_CASE_HTTP_VERBS
    url_path: str
    url_name: str
    kwargs: Mapping[str, Any]
    mapping: MethodMapper
    __call__: _F

# TODO(sbdchd): update these to return a Protocol with the property that gets
# attached along with __call__ set to the func

def api_view(http_method_names: _MIXED_CASE_HTTP_VERBS | None = ...) -> Callable[[_F], _F]: ...

_RenderClassesParam = Sequence[type[BaseRenderer]]

def renderer_classes(renderer_classes: _RenderClassesParam) -> Callable[[_F], _F]: ...

_ParserClassesParam = Sequence[type[BaseParser]]

def parser_classes(parser_classes: _ParserClassesParam) -> Callable[[_F], _F]: ...

_AuthClassesParam = Sequence[type[BaseAuthentication]]

def authentication_classes(authentication_classes: _AuthClassesParam) -> Callable[[_F], _F]: ...

_ThrottleClassesParam = Sequence[type[BaseThrottle]]

def throttle_classes(throttle_classes: _ThrottleClassesParam) -> Callable[[_F], _F]: ...

_PermClassesParam = Sequence[_PermissionClass]

def permission_classes(permission_classes: _PermClassesParam) -> Callable[[_F], _F]: ...

_SchemaClassesParam = Optional[type[ViewInspector]]

def schema(view_inspector: _SchemaClassesParam) -> Callable[[_F], _F]: ...
def action(
    methods: _MIXED_CASE_HTTP_VERBS | None = ...,
    detail: bool = ...,
    url_path: str | None = ...,
    url_name: str | None = ...,
    suffix: str | None = ...,
    name: str | None = ...,
    # **kwargs expanded, might have missed a few
    serializer_class: type[BaseSerializer] = ...,
    permission_classes: _PermClassesParam = ...,
    throttle_classes: _ThrottleClassesParam = ...,
    schema: _SchemaClassesParam = ...,
    authentication_classes: _AuthClassesParam = ...,
    renderer_classes: _RenderClassesParam = ...,
    parser_classes: _ParserClassesParam = ...,
    filter_backends: Sequence[type[FilterBackendProtocol]] = ...,
    lookup_field: str = ...,
    lookup_url_kwarg: str | None = ...,
    queryset: QuerySet[Any] = ...,
    **kwargs: Any,
) -> Callable[[_F], ViewSetAction[_F]]: ...
