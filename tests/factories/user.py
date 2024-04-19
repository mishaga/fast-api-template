import faker

from common_functions import dates
from db.models import User
from tests import factories

_faker = faker.Faker()


class UserFactory(factories.BaseFactory):
    """Factory for creation Users."""

    @classmethod
    async def build(cls, **kwargs) -> User:
        """Build object.

        Returns:
            built object of User model
        """
        assert 'id' not in kwargs, 'user id should not be passed'

        first_name = _faker.first_name()
        last_name = _faker.last_name()

        kwargs.setdefault('first_name', first_name)
        kwargs.setdefault('last_name', last_name)
        kwargs.setdefault('email', f'{first_name}.{last_name}@email.fake'.lower())
        kwargs.setdefault('confirmed', True)
        kwargs.setdefault('created_at', dates.now())

        return User(**kwargs)


async def handle_user(kwargs: dict) -> None:
    """Handle user.

    If user is in the kwargs, passes its id and removes object from kwargs.
    If user_id is in not the kwargs, creates one and store its id in kwargs.
    """
    if 'user' in kwargs:
        user = kwargs.pop('user')
        kwargs['user_id'] = user.id

    if 'user_id' not in kwargs:
        user = await UserFactory.create()
        kwargs['user_id'] = user.id
