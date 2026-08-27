from unittest.mock import AsyncMock

import pytest
from starlette.testclient import TestClient

from rule_service.rule_dependencies import db_handler
from rule_service.rule_main import app


class MockBeginContext:
    async def __aenter__(self):
        return MockBegin()

    async def __aexit__(self, *args):
        pass


class MockBegin:
    def begin(self):
        return MockBeginContext()

    def add(self, *args):
        pass

    async def commit(self):
        return AsyncMock()

    async def execute(self, *args):
        pass


class MockContext:
    async def __aenter__(self):
        return MockBegin()

    async def __aexit__(self, *args):
        pass


class DbMock:
    def add(self, **kwargs):    # pylint: disable = unused-argument
        mock_func = AsyncMock()
        return mock_func()

    def delete(self, **kwargs):    # pylint: disable = unused-argument
        mock_func = AsyncMock()
        return mock_func()


def mock_db_handler():
    return DbMock()


@pytest.fixture()
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def override_dependency():
    app.dependency_overrides[db_handler] = mock_db_handler
    yield
