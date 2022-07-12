from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Type, TypeVar, Union

from django.db.models import QuerySet
from django.http.response import HttpResponseBase
from typing_extensions import Literal, Protocol

from rest_framework.authentication import BaseAuthentication
from rest_framework.filters import _FilterBackendProtocol
from rest_framework.parsers import BaseParser
from rest_framework.permissions import _PermissionClass
from rest_framework.renderers import BaseRenderer
from rest_framework.schemas.inspectors import ViewInspector
from rest_framework.serializers import BaseSerializer
from rest_framework.throttling import BaseThrottle

class MethodMapper(Dict[str, Any]):
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

_LOWER_CASE_HTTP_VERBS = List[
    Union[
        Literal["get"],
        Literal["post"],
        Literal["delete"],
        Literal["put"],
        Literal["patch"],
        Literal["trace"],
        Literal["options"],
    ]
]

_MIXED_CASE_HTTP_VERBS = Sequence[
    Union[
        Literal["GET"],
        Literal["POST"],
        Literal["DELETE"],
        Literal["PUT"],
        Literal["PATCH"],
        Literal["TRACE"],
        Literal["OPTIONS"],
        Literal["get"],
        Literal["post"],
        Literal["delete"],
        Literal["put"],
        Literal["patch"],
        Literal["trace"],
        Literal["options"],
    ]
]

class ViewSetAction(Protocol[_F]):
    detail: bool
    methods: _LOWER_CASE_HTTP_VERBS
    url_path: str
    url_name: str
    kwargs: Mapping[str, Any]
    mapping: MethodMapper
    __call__: _F

_CallableViewHandler = Callable[..., HttpResponseBase]

_F = TypeVar("_F", bound=_CallableViewHandler)

# TODO(sbdchd): update these to return a Protocol with the property that gets
# attached along with __call__ set to the func

def api_view(http_method_names: Optional[_MIXED_CASE_HTTP_VERBS] = ...) -> Callable[[_F], _F]: ...

_RenderClassesParam = Sequence[Type[BaseRenderer]]

def renderer_classes(renderer_classes: _RenderClassesParam) -> Callable[[_F], _F]: ...

_ParserClassesParam = Sequence[Type[BaseParser]]

def parser_classes(parser_classes: _ParserClassesParam) -> Callable[[_F], _F]: ...

_AuthClassesParam = Sequence[Type[BaseAuthentication]]

def authentication_classes(authentication_classes: _AuthClassesParam) -> Callable[[_F], _F]: ...

_ThrottleClassesParam = Sequence[Type[BaseThrottle]]

def throttle_classes(throttle_classes: _ThrottleClassesParam) -> Callable[[_F], _F]: ...

_PermClassesParam = Sequence[Type[_PermissionClass]]

def permission_classes(permission_classes: _PermClassesParam) -> Callable[[_F], _F]: ...

_SchemaClassesParam = Optional[Type[ViewInspector]]

def schema(view_inspector: _SchemaClassesParam) -> Callable[[_F], _F]: ...
def action(
    methods: Optional[_MIXED_CASE_HTTP_VERBS] = ...,
    detail: bool = ...,
    url_path: Optional[str] = ...,
    url_name: Optional[str] = ...,
    suffix: Optional[str] = ...,
    name: Optional[str] = ...,
    # **kwargs expanded, might have missed a few
    serializer_class: Type[BaseSerializer] = ...,
    permission_classes: _PermClassesParam = ...,
    throttle_classes: _ThrottleClassesParam = ...,
    schema: _SchemaClassesParam = ...,
    authentication_classes: _AuthClassesParam = ...,
    renderer_classes: _RenderClassesParam = ...,
    parser_classes: _ParserClassesParam = ...,
    filter_backends: Sequence[Type[_FilterBackendProtocol]] = ...,
    lookup_field: str = ...,
    lookup_url_kwarg: Optional[str] = ...,
    queryset: QuerySet[Any] = ...,
    **kwargs: Any,
) -> Callable[[_F], _F]: ...
