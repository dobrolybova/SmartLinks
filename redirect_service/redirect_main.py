from logging import getLogger, basicConfig

import uvicorn
from fastapi import FastAPI, Depends

from redirect_service.redirect_middlewares import middleware_seq
from redirect_service.redirect_dependencies import log_incoming_body
from redirect_service.redirect_endpoint import redirect_router

logger = getLogger(__name__)

basicConfig(filename="", filemode="w", level="INFO", format="%(asctime)s,%(levelname)-5s %(filename)s:%(funcName)s:%(lineno)-5d %(message)s")


app = FastAPI(middleware=middleware_seq)

app.include_router(redirect_router, dependencies=[Depends(log_incoming_body)])


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
