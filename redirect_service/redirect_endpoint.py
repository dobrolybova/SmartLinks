from http import HTTPStatus
from logging import getLogger

from fastapi import APIRouter, Request, Depends
from starlette.responses import RedirectResponse, JSONResponse

from redirect_service.redirect_interfaces import DbHandlerIf, RuleHandlerIf
from redirect_service.redirect_dependencies import db_handler
from redirect_service.redirect_rule_config import rule_config_map
from redirect_service.redirect_schemas import Rules

redirect_router = APIRouter(prefix="/api/v1")

logger = getLogger(__name__)


@redirect_router.get("/redirect")
async def redirect(request: Request, db: DbHandlerIf = Depends(db_handler)):
    rules: list[Rules] = await db.fetch_all()
    for rule in rules:
        try:
            handler: RuleHandlerIf = rule_config_map.get(rule.rule)()
            url = await handler.handle(request=request, attribute=rule.property, url=rule.url)
            if url:
                return RedirectResponse(url=url)
        except Exception as exc:
            logger.error(f"Skipp rule {rule} due to {exc}")
    return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content={"error": "No redirect rule"})
