from http import HTTPStatus
from logging import getLogger

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from rule_service.rule_interfaces import DbHandlerIf
from rule_service.rule_dependencies import db_handler
from rule_service.rule_schemas import CreateRuleReq, Rules

rule_router = APIRouter(prefix="/api/v1")

logger = getLogger(__name__)


@rule_router.post("/rule")
async def add_rule(body: CreateRuleReq, db: DbHandlerIf = Depends(db_handler)):
    try:
        for data in body.data:
            rules_data = Rules(rule=body.rule_type, priority=body.priority, property=data.property, url=data.url)
            await db.add(data=rules_data)
    except Exception as exc:
        logger.error(f"{exc}")
        return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content={"error": str(exc)})
    return JSONResponse(status_code=HTTPStatus.OK, content={"add_rule": "OK"})


@rule_router.delete("/rule")
async def delete_rule(rule_type: str, db: DbHandlerIf = Depends(db_handler)):
    try:
        await db.delete(rule=rule_type)
    except Exception as exc:
        logger.error(f"{exc}")
        return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content={"error": str(exc)})
    return JSONResponse(status_code=HTTPStatus.OK, content={"delete_rule": "OK"})
