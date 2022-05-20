from typing import Any, Dict, Mapping, Optional, Union

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.test import testcases
from django.test.client import Client as DjangoClient
from django.test.client import ClientHandler
from django.test.client import RequestFactory as DjangoRequestFactory

import coreapi
import requests
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response

def force_authenticate(
    request: Request, user: Optional[Union[AnonymousUser, AbstractBaseUser]] = ..., token: Optional[Token] = ...
) -> None: ...

class HeaderDict(requests.packages.urllib3._collections.HTTPHeaderDict):
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
        data: Optional[Union[Mapping[str, Any], str]] = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
    ) -> Request: ...
    def post(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: Optional[str] = ...,
        content_type: Optional[str] = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
    ) -> Request: ...
    def put(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: Optional[str] = ...,
        content_type: Optional[str] = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
    ) -> Request: ...
    def patch(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: Optional[str] = ...,
        content_type: Optional[str] = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
    ) -> Request: ...
    def delete(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: Optional[str] = ...,
        content_type: Optional[str] = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
    ) -> Request: ...
    def options(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: Optional[str] = ...,
        content_type: Optional[Any] = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
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
        **extra: str
    ) -> Request: ...

class ForceAuthClientHandler(ClientHandler):
    def __init__(self, *args: Any, **kwargs: Any): ...
    def get_response(self, request: Request) -> Response: ...  # type: ignore[override]

class APIClient(APIRequestFactory, DjangoClient):
    handler: Any = ...
    def credentials(self, **kwargs: Any) -> Any: ...
    def force_authenticate(self, user: Optional[Any] = ..., token: Optional[Token] = ...) -> None: ...
    def request(self, **kwargs: Any) -> Response: ...  # type: ignore[override]
    def get(  # type: ignore [override]
        self,
        path: str,
        data: Optional[Union[Dict[str, Any], str]] = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
    ) -> Response: ...
    def post(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: Optional[str] = ...,
        content_type: Optional[str] = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
    ) -> Response: ...
    def put(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: Optional[str] = ...,
        content_type: Optional[str] = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
    ) -> Response: ...
    def patch(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: Optional[str] = ...,
        content_type: Optional[str] = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
    ) -> Response: ...
    def delete(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: Optional[str] = ...,
        content_type: Optional[str] = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
    ) -> Response: ...
    def options(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        format: Optional[str] = ...,
        content_type: Optional[str] = ...,
        follow: bool = ...,
        *,
        QUERY_STRING: str = ...,
        **extra: str
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
