from logging import getLogger

from starlette.requests import Request

from rule_service.rule_db_handler import RuleDbHandler
from rule_service.rule_interfaces import DbHandlerIf

logger = getLogger(__name__)


async def log_incoming_body(request: Request) -> None:
    body = await request.body()
    logger.info(f"New incoming request to change redirect rule {body} {request.headers} {request.query_params}")


def db_handler() -> DbHandlerIf:
    return RuleDbHandler()
