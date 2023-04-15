from collections.abc import Callable, Sequence
from typing import Any

from rest_framework.renderers import BaseRenderer
from rest_framework.schemas.coreapi import AutoSchema as AutoSchema
from rest_framework.schemas.coreapi import ManualSchema as ManualSchema
from rest_framework.schemas.coreapi import SchemaGenerator as SchemaGenerator
from rest_framework.schemas.inspectors import DefaultSchema as DefaultSchema
from rest_framework.settings import api_settings as api_settings

def get_schema_view(
    title: str | None = ...,
    url: str | None = ...,
    description: str | None = ...,
    urlconf: str | None = ...,
    renderer_classes: Sequence[type[BaseRenderer]] | None = ...,
    public: bool = ...,
    patterns: Sequence[Any] | None = ...,
    generator_class: type[SchemaGenerator] = ...,
    authentication_classes: Sequence[str] = ...,
    permission_classes: Sequence[str] = ...,
    version: str | None = ...,
) -> Callable[..., Any]: ...
