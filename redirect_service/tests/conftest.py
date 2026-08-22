from unittest.mock import AsyncMock

import pytest
from starlette.testclient import TestClient

from redirect_service.redirect_dependencies import db_handler
from redirect_service.redirect_main import app
from redirect_service.redirect_schemas import Rules


class DbMock:   # pylint: disable = too-few-public-methods
    def fetch_all(self):
        mock_func = AsyncMock(return_value=[
            Rules(id=1, rule="host", priority=1, property="localhost", url=""),
            Rules(id=1, rule="browser", priority=1, property="testclient", url="http://"),
        ])
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


class ErrDbMock:   # pylint: disable = too-few-public-methods
    def fetch_all(self):
        mock_func = AsyncMock(return_value=[])
        return mock_func()


def exception_mock():
    return ErrDbMock()


@pytest.fixture()
def client_fetch_error() -> TestClient:
    app.dependency_overrides[db_handler] = exception_mock
    return TestClient(app)


class WrongDataDbMock:   # pylint: disable = too-few-public-methods
    def fetch_all(self):
        mock_func = AsyncMock(return_value=[1])
        return mock_func()


def wrong_data_mock():
    return WrongDataDbMock()


@pytest.fixture()
def wrong_data_error() -> TestClient:
    app.dependency_overrides[db_handler] = wrong_data_mock
    return TestClient(app)
