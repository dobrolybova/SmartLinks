from logging import getLogger, basicConfig

import uvicorn
from fastapi import FastAPI, Depends

from rule_service.rule_dependencies import log_incoming_body
from rule_service.rule_endpoint import rule_router

logger = getLogger(__name__)

basicConfig(filename="", filemode="w", level="INFO", format="%(asctime)s,%(levelname)-5s %(filename)s:%(funcName)s:%(lineno)-5d %(message)s")


app = FastAPI()

app.include_router(rule_router, dependencies=[Depends(log_incoming_body)])


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
