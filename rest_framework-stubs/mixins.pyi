from typing import Any, Dict

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

class CreateModelMixin:
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def perform_create(self, serializer: BaseSerializer) -> None: ...
    def get_success_headers(self, data: Any) -> Dict[str, str]: ...

class ListModelMixin:
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class RetrieveModelMixin:
    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class UpdateModelMixin:
    def update(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def perform_update(self, serializer: BaseSerializer) -> None: ...
    def partial_update(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class DestroyModelMixin:
    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def perform_destroy(self, instance: Any) -> None: ...
