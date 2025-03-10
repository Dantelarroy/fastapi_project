from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import logging

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logging.info(f"Solicitud: {request.method} {request.url}")
        return await call_next(request)
