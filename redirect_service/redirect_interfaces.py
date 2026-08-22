from typing import Protocol, Any


class DbHandlerIf(Protocol):   # pylint: disable=too-few-public-methods
    async def fetch_all(self) -> Any:
        ...


class RuleHandlerIf(Protocol):  # pylint: disable=too-few-public-methods
    async def handle(self, request: Any, attribute: str, url: str) -> str | None:
        ...
