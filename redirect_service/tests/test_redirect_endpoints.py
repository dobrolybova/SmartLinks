from http import HTTPStatus
from unittest.mock import AsyncMock

import pytest

from redirect_service.redirect_db_handler import RedirectDbHandler


def test_404(client):
    res = client.get("/wrong_url")
    assert res.status_code == HTTPStatus.NOT_FOUND


def test_405(client):
    res = client.post("/api/v1/redirect")
    assert res.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    res = client.put("/api/v1/redirect")
    assert res.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    res = client.patch("/api/v1/redirect")
    assert res.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_redirect(client):
    res = client.get("/api/v1/redirect", follow_redirects=False)
    assert res.headers["location"] == "http://"


def test_redirect_400(client_fetch_error):
    res = client_fetch_error.get("/api/v1/redirect", follow_redirects=False)
    assert res.status_code == HTTPStatus.BAD_REQUEST


def test_redirect_no_rules(wrong_data_error):
    res = wrong_data_error.get("/api/v1/redirect", follow_redirects=False)
    assert res.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.asyncio
async def test_db_handler():
    db_handler = RedirectDbHandler()
    db_handler.async_session = AsyncMock
