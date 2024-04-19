from sqlalchemy import func, select

from db.base_model import BaseModel
from db.session import Session


async def get_objects_count(model: BaseModel) -> int:
    """Check count of records of a model."""
    table = model.__table__
    statement = select(func.count()).select_from(table)

    async with Session() as session:
        raw_response = await session.execute(statement)

    return raw_response.scalar_one()


async def assert_objects_count(model: BaseModel, expected_count: int) -> None:
    """Assert count of records of a model."""
    count = await get_objects_count(model)
    error_message = f'Expected to be {expected_count} records of {model} in DB, {count} retrieved'
    assert count == expected_count, error_message
