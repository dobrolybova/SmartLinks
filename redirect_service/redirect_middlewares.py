import os
from time import time

from fastapi import Request, Response
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import CollectorRegistry, Summary, multiprocess


registry = CollectorRegistry()
sum_registry = registry
if "prometheus_multiproc_def" in os.environ:
    multiprocess.MultiProcessCollector(registry)
    # registry should be None in case of multiprocess
    sum_registry = None

SERVER_REQUEST = Summary(
    "server_req_seconds",
    "Server request metric",
    ["method", "uri", "status"],
    registry=sum_registry,
)


def get_status(response: Response) -> int:
    try:
        status = response.status_code.value
    except AttributeError:
        status = response.status_code
    return status


class Monitoring(BaseHTTPMiddleware):    # pylint: disable=too-few-public-methods
    async def dispatch(self, request: Request, call_next):
        start_time = time()
        response: Response | None = None
        try:
            response = await call_next(request)
            return response
        finally:
            if response is not None:
                status = get_status(response)
            else:
                status = None
            SERVER_REQUEST.labels(
                request.method, request.url, status
            ).observe(time() - start_time)


middleware_seq = [Middleware(Monitoring)]
