from fastapi import Request


class BrowserRuleHandler:   # pylint: disable=too-few-public-methods
    async def handle(self, request: Request, attribute: str, url: str) -> str | None:
        if attribute in request.headers.get("user-agent", ""):
            return url
        return None


class HostRuleHandler:   # pylint: disable=too-few-public-methods
    async def handle(self, request: Request, attribute: str, url: str) -> str | None:
        if attribute == "localhost":
            attribute = "127.0.0.1"
        if attribute in request.headers.get("host", ""):
            return url
        return None
