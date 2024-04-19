import abc

from db.session import Session


class BaseFactory[T](abc.ABC):  # noqa: WPS111 Found too short name
    """Base Factory class."""

    @classmethod
    @abc.abstractmethod
    async def build(cls, **kwargs) -> T:
        """Abstract method for building object.

        Raises:
            NotImplementedError: when calling an abstract method
        """
        raise NotImplementedError

    @classmethod
    async def create(cls, **kwargs) -> T:
        """Create (build and insert to DB) object.

        Returns:
            created object
        """
        object_ = await cls.build(**kwargs)
        async with Session() as session:
            session.add(object_)
            await session.commit()
            return object_

    @classmethod
    async def create_batch(cls, cnt: int, /, **kwargs) -> list[T]:  # noqa: WPS451 (Found positional-only argument)
        """Create several objects.

        Returns:
            list of created object
        """
        assert cnt > 0, 'count of objects should be greater than 0'

        objects_list = []

        async with Session() as session:
            for _ in range(cnt):
                object_ = await cls.build(**kwargs)
                objects_list.append(object_)
                session.add(object_)
            await session.commit()

        return objects_list
