from typing import Any

from django.db.models import QuerySet

def pygments_css(style: Any) -> str | None: ...
def pygments_highlight(text: str, lang: str, style: Any) -> Any: ...
def md_filter_add_syntax_highlight(md: Any) -> bool: ...
def unicode_http_header(value: str | bytes) -> str: ...
def distinct(queryset: QuerySet[Any], base: QuerySet[Any] | None) -> QuerySet[Any]: ...

SHORT_SEPARATORS: tuple[str, str]
LONG_SEPARATORS: tuple[str, str]
INDENT_SEPARATORS: tuple[str, str]
