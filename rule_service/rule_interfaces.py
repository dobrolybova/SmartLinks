from typing import Protocol, Any


class DbHandlerIf(Protocol):
    async def add(self, data: Any) -> None:
        ...

    async def delete(self, **kwargs) -> None:
        ...
