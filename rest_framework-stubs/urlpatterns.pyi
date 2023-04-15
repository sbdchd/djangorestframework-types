from collections.abc import Sequence
from re import Pattern

from django.urls.resolvers import RoutePattern, URLPattern, URLResolver

def apply_suffix_patterns(
    urlpatterns: Sequence[URLResolver | RoutePattern | URLPattern | Pattern[str]],
    suffix_pattern: str | Pattern[str],
    suffix_required: bool,
    suffix_route: str | None = ...,
) -> list[URLPattern]: ...
def format_suffix_patterns(
    urlpatterns: Sequence[URLResolver | RoutePattern | URLPattern | Pattern[str]],
    suffix_required: bool = ...,
    allowed: list[URLPattern | Pattern[str] | str] | None = ...,
) -> list[URLPattern]: ...
