from fastapi import HTTPException, Request

from api import exceptions
from api.authentication.classes import JwtErrorUser, JwtUser


async def auth_user_only(request: Request) -> JwtUser:
    """Check if user was authenticated with header.

    Parameters:
        request: user's request

    Raises:
        HTTPException: when there is a problem with the auth token
        NoAuthHeader: when there is an unknown error

    Returns:
        JwtUser model
    """
    if isinstance(request.user, JwtErrorUser):
        raise HTTPException(
            status_code=request.user.status_code,
            detail=request.user.detail,
        )

    if not request.user.is_authenticated:
        raise exceptions.token.NoAuthHeader()

    return request.user
