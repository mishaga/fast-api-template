import logging

from starlette.requests import Request

from api import responses
from config import const
from db import selectors
from db.session import Session

log = logging.getLogger(const.LOGGER_API)


async def user_info(request: Request) -> responses.UserInfo:
    """User info page.

    Parameters:
        request: user's Request

    Returns:
        model with basic user info.
    """
    log.info('Requesting user info')

    async with Session() as session:
        user = await selectors.user.get(
            session=session,
            user_id=request.user.user_id,
        )

    return responses.UserInfo(
        id=user.id,
        name=user.full_name,
    )
