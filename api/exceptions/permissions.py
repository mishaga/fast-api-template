from starlette import status

from api.exceptions.base_exception import BaseApiException


class NotAdminError(BaseApiException):
    """Used when auth header was not passed."""

    status_code = status.HTTP_403_FORBIDDEN
    detail = 'The user is not an administrator'


class NotJuryError(BaseApiException):
    """Used when auth header was not passed."""

    status_code = status.HTTP_403_FORBIDDEN
    detail = 'The user is not a member of the jury'
