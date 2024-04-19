from sqlalchemy.orm import declarative_base, declared_attr

from common_functions import strings


class DeclarativeBase:
    """Base class for models."""

    @declared_attr
    def __tablename__(cls):  # noqa: N805  first argument of a method should be named 'self'
        """Define table name for child class.

        It's not necessary to define __tablename__ parameter in the model,
        it will be defined automatically.

        Returns:
            table name
        """
        return strings.camel_to_snake_case(cls.__name__)


BaseModel = declarative_base(cls=DeclarativeBase)
