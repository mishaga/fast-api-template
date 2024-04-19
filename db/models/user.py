import sqlalchemy as sa

from common_functions import dates
from db.base_model import BaseModel


class User(BaseModel):
    """Model for users."""

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
    )
    email = sa.Column(
        sa.Text,
        unique=True,
        nullable=False,
        default='',
    )
    first_name = sa.Column(
        sa.Text,
        nullable=False,
        default='',
    )
    last_name = sa.Column(
        sa.Text,
        nullable=False,
        default='',
    )
    confirmed = sa.Column(
        sa.Boolean,
        nullable=False,
        default=False,
    )
    created_at = sa.Column(
        sa.DateTime(timezone=True),
        nullable=False,
        default=dates.now,
    )

    def __repr__(self) -> str:
        """Representation of user model.

        Returns:
            string representation of user model
        """
        return 'User({self.id})'.format(self=self)

    def __eq__(self, other) -> bool:
        """Return equivalent of objects.

        Parameters:
            other: object to compare with

        Returns:
            are objects equal
        """
        if isinstance(other, User):
            return self.id == other.id

        return False

    @property
    def full_name(self) -> str:
        """User's full name.

        Returns:
            full name of the user.
        """
        return f'{self.first_name} {self.last_name}'.strip()
