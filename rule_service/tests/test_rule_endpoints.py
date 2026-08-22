from http import HTTPStatus

import pytest

from rule_service.rule_db_handler import RuleDbHandler
from rule_service.rule_schemas import Rules
from rule_service.tests.conftest import MockContext


def test_404(client):
    res = client.get("/wrong_url")
    assert res.status_code == HTTPStatus.NOT_FOUND


def test_405(client):
    res = client.get("/api/v1/rule")
    assert res.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    res = client.put("/api/v1/rule")
    assert res.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    res = client.patch("/api/v1/rule")
    assert res.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_422(client):
    res = client.post("/api/v1/rule", json={})
    assert res.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_add_rule(client):
    res = client.post("/api/v1/rule", json={
        "rule_type": "browser",
        "priority": 1,
        "data": [
            {
                "property": "Firefox", "url": "https://yandex.ru/maps/213/moscow/?ll=37.617700%2C55.755863&z=10"
            }
        ]
    })
    assert res.status_code == HTTPStatus.OK
    assert res.json() == {"add_rule": "OK"}


def test_delete_rule(client):
    res = client.delete("/api/v1/rule?rule_type=browser")
    assert res.status_code == HTTPStatus.OK
    assert res.json() == {"delete_rule": "OK"}


@pytest.mark.asyncio
async def test_db_handler():
    db_handler = RuleDbHandler()
    db_handler.async_session = MockContext
    await db_handler.add(data=Rules())
    await db_handler.delete(rule="")
