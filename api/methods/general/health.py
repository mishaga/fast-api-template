import logging

from sqlalchemy import select
from sqlalchemy.sql.functions import current_timestamp

from api import responses
from config import const
from db.session import Session

log = logging.getLogger(const.LOGGER_API)


async def health() -> responses.HealthPage:
    """Health page.

    Returns:
        health page info
    """
    log.info('Requesting health check')
    async with Session() as session:
        try:
            await session.execute(statement=select(current_timestamp()))
        except Exception:
            database = False
        else:
            database = True

    return responses.HealthPage(
        database=database,
    )
