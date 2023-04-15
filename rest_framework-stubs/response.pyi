from collections.abc import Mapping
from typing import Any

from django.template.response import SimpleTemplateResponse

class Response(SimpleTemplateResponse):
    data: object
    exception: bool = ...
    content_type: str | None = ...
    _headers: dict[str, tuple[str, str]]
    def __init__(
        self,
        data: object = ...,
        status: int | None = ...,
        template_name: str | None = ...,
        headers: Mapping[str, str] | None = ...,
        exception: bool = ...,
        content_type: str | None = ...,
    ): ...
    @property
    def rendered_content(self) -> Any: ...
    @property
    def status_text(self) -> str: ...
