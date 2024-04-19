import pytest

from api.authentication.classes import JwtUser
from api.authentication.json_web_token import generate_token
from db.models import User
from tests import factories
from tests.const import SCOPE_FUNCTION


@pytest.fixture(scope=SCOPE_FUNCTION)
async def user(database) -> User:
    """Return user object.

    Returns:
        User model
    """
    return await factories.UserFactory.create()


@pytest.fixture(scope=SCOPE_FUNCTION)
async def auth_data(user: User) -> JwtUser:
    """Return JwtUser for regular user.

    Returns:
        JwtUser
    """
    generated_token = generate_token(user=user)
    return JwtUser(
        user_id=user.id,
        token=generated_token.token,
    )
