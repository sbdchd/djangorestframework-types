from collections.abc import Mapping
from typing import Any, Optional

import coreapi
import requests
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.test import testcases
from django.test.client import Client as DjangoClient
from django.test.client import ClientHandler
from django.test.client import RequestFactory as DjangoRequestFactory
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from urllib3._collections import HTTPHeaderDict

def force_authenticate(
    request: Request, user: AnonymousUser | AbstractBaseUser | None = ..., token: Token | None = ...
) -> None: ...

class HeaderDict(HTTPHeaderDict):
    def get_all(self, key: Any, default: Any) -> Any: ...

class MockOriginalResponse:
    msg: Any = ...
    closed: bool = ...
    def __init__(self, headers: Any) -> None: ...
    def isclosed(self) -> Any: ...
    def close(self) -> None: ...

class DjangoTestAdapter(requests.adapters.HTTPAdapter):
    app: Any = ...
    factory: Any = ...
    def __init__(self) -> None: ...
    def get_environ(self, request: Request) -> Any: ...
    def send(self, request: Request, *args: Any, **kwargs: Any) -> requests.Response: ...  # type: ignore[override]
    def close(self) -> None: ...

class RequestsClient(requests.Session): ...

class CoreAPIClient(coreapi.Client):
    def __init__(self, *args: Any, **kwargs: Any): ...
    @property
    def session(self) -> Any: ...

_RequestData = Optional[Any]

class APIRequestFactory(DjangoRequestFactory):
    renderer_classes_list: Any = ...
    default_format: Any = ...
    enforce_csrf_checks: Any = ...
    renderer_classes: Any = ...
    def __init__(self, enforce_csrf_checks: bool = ..., **defaults: Any) -> None: ...
    def request(self, **kwargs: Any) -> Request: ...  # type: ignore[override]
    def get(  # type: ignore [override]
        self,
        path: str,
        data: Mapping[str, Any] | str | None = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Request: ...
    def post(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Request: ...
    def put(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Request: ...
    def patch(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Request: ...
    def delete(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Request: ...
    def options(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: str | None = ...,
        content_type: Any | None = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Request: ...
    def generic(  # type: ignore[override]
        self,
        method: str,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Request: ...

class ForceAuthClientHandler(ClientHandler):
    def __init__(self, *args: Any, **kwargs: Any): ...
    def get_response(self, request: Request) -> Response: ...  # type: ignore[override]

class APIClient(APIRequestFactory, DjangoClient):  # pyright: ignore[reportIncompatibleMethodOverride]
    handler: Any = ...
    def credentials(self, **kwargs: Any) -> Any: ...
    def force_authenticate(self, user: Any | None = ..., token: Token | None = ...) -> None: ...
    def request(self, **kwargs: Any) -> Response: ...  # type: ignore[override]
    def get(  # type: ignore [override]
        self,
        path: str,
        data: dict[str, Any] | str | None = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Response: ...
    def post(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Response: ...
    def put(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Response: ...
    def patch(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Response: ...
    def delete(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Response: ...
    def options(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str,
    ) -> Response: ...
    def logout(self) -> None: ...

class APITransactionTestCase(testcases.TransactionTestCase):
    client_class: APIClient = ...
    client: APIClient

class APITestCase(testcases.TestCase):
    client_class: APIClient = ...
    client: APIClient

class APISimpleTestCase(testcases.SimpleTestCase):
    client_class: APIClient = ...
    client: APIClient

class APILiveServerTestCase(testcases.LiveServerTestCase):
    client_class: APIClient = ...
    client: APIClient

class URLPatternsTestCase(testcases.SimpleTestCase): ...
