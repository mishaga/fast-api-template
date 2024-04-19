from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from config import settings

_engine: AsyncEngine = create_async_engine(
    url=settings.database.get_async_connection_link(),
    pool_pre_ping=True,
    # debug if needed: echo=settings.project.debug,
)
_sync_engine = create_engine(
    url=settings.database.get_sync_connection_link(),
    pool_pre_ping=True,
    # debug if needed: echo=settings.project.debug,
)

Session = async_sessionmaker(
    bind=_engine,
    expire_on_commit=False,
)
SyncSession = sessionmaker(
    bind=_sync_engine,
    expire_on_commit=False,
)
