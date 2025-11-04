from collections import OrderedDict
from collections.abc import Callable
from typing import Any, TypeVar

from django.db.models import Model
from django.http.response import HttpResponse
from rest_framework import generics, mixins, views
from rest_framework.decorators import ViewSetAction
from rest_framework.request import Request

def _is_extra_action(attr: Any) -> bool: ...

_ViewFunc = Callable[..., HttpResponse]

class ViewSetMixin:
    # Classvars assigned in as_view()
    name: str | None
    description: str | None
    suffix: str | None
    detail: bool
    basename: str
    # Instance attributes assigned in view wrapper
    action_map: dict[str, str]
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    # NOTE: Assigned in initialize_request()
    action: str
    @classmethod
    def as_view(
        cls, actions: dict[str, str | ViewSetAction[Any]] | None = ..., **initkwargs: Any
    ) -> Callable[..., HttpResponse]: ...
    def initialize_request(self, request: Request, *args: Any, **kwargs: Any) -> Request: ...
    def reverse_action(self, url_name: str, *args: Any, **kwargs: Any) -> str: ...
    @classmethod
    def get_extra_actions(cls) -> list[_ViewFunc]: ...
    def get_extra_action_url_map(self) -> OrderedDict[str, str]: ...

_MT_co = TypeVar("_MT_co", bound=Model, covariant=True)

class ViewSet(ViewSetMixin, views.APIView): ...
class GenericViewSet(ViewSetMixin, generics.GenericAPIView[_MT_co]): ...
class ReadOnlyModelViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet[_MT_co]): ...
class ModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet[_MT_co],
): ...
