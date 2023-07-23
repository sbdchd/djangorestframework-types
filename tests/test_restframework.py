from rest_framework.decorators import permission_classes
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
