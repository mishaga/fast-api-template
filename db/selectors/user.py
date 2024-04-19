from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import models


async def get(
    session: AsyncSession,
    user_id: int,
) -> models.User:
    """Return user model by user_id."""
    statement = select(models.User).filter(
        models.User.id == user_id,
    )
    raw_value = await session.execute(statement)
    return raw_value.scalar_one()


async def get_by_email(
    session: AsyncSession,
    email: str,
) -> models.User:
    """Return user model by email."""
    statement = select(models.User).filter(
        models.User.email == email,
    )
    raw_value = await session.execute(statement)
    return raw_value.scalar_one()


async def create(
    session: AsyncSession,
    email: str,
    first_name: str,
    last_name: str,
) -> models.User:
    """Create user."""
    user = models.User(
        email=email,
        first_name=first_name,
        last_name=last_name,
    )

    session.add(user)
    await session.commit()

    return user
