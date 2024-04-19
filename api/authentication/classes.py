import dataclasses
import datetime
import typing

from starlette.authentication import BaseUser


@dataclasses.dataclass(frozen=True, slots=True)
class GeneratedToken:
    """Token and its expiration datetime."""

    token: str
    expires_at: datetime.datetime


class JwtDataVersion1(typing.TypedDict):
    """Data to decode in JWT."""

    version: int
    user_id: int
    iat: datetime.datetime
    exp: datetime.datetime


class JwtUser(BaseUser):
    """Model for authorised user."""

    def __init__(self, user_id: int, token: str) -> None:
        """Init method.

        Parameters:
            user_id: user id
            token: token string
        """
        self.user_id = user_id
        self.token = token

    @property
    def is_authenticated(self) -> bool:
        """This user is authenticated.

        Returns:
            bool (True)
        """
        return True

    @property
    def header(self) -> dict[typing.Literal['Authorization'], str]:
        """Dict with authorization header.

        Returns:
            dict with authorization header
        """
        return {
            'Authorization': f'Bearer {self.token}',
        }


class JwtErrorUser(BaseUser):
    """Model for unauthorised user with code and the reason why it was not authorised."""

    def __init__(self, status_code: int, detail: str) -> None:
        """Init method.

        Parameters:
            status_code: HTTP status code to return
            detail: text of error
        """
        self.status_code = status_code
        self.detail = detail

    @property
    def is_authenticated(self) -> bool:
        """This user is not authenticated.

        Returns:
            bool (False)
        """
        return False

    @property
    def header(self) -> dict[typing.Literal['Authorization'], typing.Literal['']]:
        """Dict with authorization header.

        In this case header is empty.

        Returns:
            dict with empty authorization header
        """
        return {
            'Authorization': '',
        }
