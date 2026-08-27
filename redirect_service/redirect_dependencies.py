from logging import getLogger
from fastapi import Request

from redirect_service.redirect_interfaces import DbHandlerIf
from redirect_service.redirect_db_handler import RedirectDbHandler

logger = getLogger(__name__)


async def log_incoming_body(request: Request) -> None:
    logger.info(f"New incoming request for redirect. {request.headers}")



def db_handler() -> DbHandlerIf:
    return RedirectDbHandler()
