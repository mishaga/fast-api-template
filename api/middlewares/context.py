from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response

from config import context


class ContextMiddleware(BaseHTTPMiddleware):
    """Middleware for filling context with entrypoint parameter."""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Dispatch method.

        Fills entrypoint context parameter.

        Parameters:
            request: Request
            call_next: what to call next

        Returns:
            Response
        """
        context.entrypoint.set(str(request.url))
        return await call_next(request)
