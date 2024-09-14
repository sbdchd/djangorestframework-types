from typing import Sequence

from rest_framework.decorators import permission_classes
from rest_framework.filters import FilterBackendProtocol
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.test import APIClient
from typing_extensions import assert_type


def test_test_client_types() -> None:
    client = APIClient()

    res = client.get("/api/v1/foo")

    assert_type(res.status_code, int)


def test_decorator_types() -> None:
    permission_classes([IsAuthenticated])
    permission_classes([IsAuthenticated | IsAdminUser])


def test_filter_backends_types() -> None:
    """
    django-filter does not use typing, so we're testing if untyped code also works fine
    with our types.

    https://github.com/carltongibson/django-filter/pull/1585
    """

    class DjangoFilterBackend:
        def filter_queryset(self, request, queryset, view):  # type: ignore
            filterset = self.get_filterset(request, queryset, view)  # type: ignore
            return filterset.qs

    class BookAPIView(GenericAPIView):
        filter_backends = (DjangoFilterBackend,)

    # mypy and pyright works differently here:
    # mypy: Expression is of type "tuple[type[DjangoFilterBackend]]", not "Sequence[type[FilterBackendProtocol]]"  [assert-type]
    # Disable this check for now in mypy.
    # At least assigning to filter_backends works fine, that's our main concern here.
    assert_type(BookAPIView.filter_backends, Sequence[type[FilterBackendProtocol]])  # type: ignore[assert-type]
