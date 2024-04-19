from starlette import status

from api.exceptions.base_exception import BaseApiException


class NoAuthHeader(BaseApiException):
    """Auth header was not passed."""

    status_code = status.HTTP_401_UNAUTHORIZED


class InvalidAuthHeader(BaseApiException):
    """Auth header has incorrect format (should be 'Bearer <value>')."""

    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Invalid auth header'


class InvalidAuthScheme(BaseApiException):
    """Auth header has incorrect scheme (should be Bearer)."""

    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Invalid auth scheme'


class TokenExpired(BaseApiException):
    """Token has expired."""

    status_code = status.HTTP_403_FORBIDDEN
    detail = 'Token expired'
