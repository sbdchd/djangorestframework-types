from typing import Any

from coreapi.codecs.base import BaseCodec
from openapi_codec.encode import generate_swagger_object as generate_swagger_object

class OpenAPICodec(BaseCodec):
    media_type: str = ...
    format: str = ...
    def decode(self, bytes: Any, **options: Any) -> Any: ...
    def encode(self, document: Any, **options: Any) -> Any: ...
