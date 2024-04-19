from starlette import status

from api.exceptions.base_exception import BaseApiException


class UserExists(BaseApiException):
    """User already exists."""

    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'User already exists'


class EmailNotFound(BaseApiException):
    """User and Code pair not found."""

    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Email not found'


class CredentialsPairNotFound(BaseApiException):
    """User and Code pair not found."""

    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Email / Code pair not found'


class CaptchaVerificationFailed(BaseApiException):
    """Captcha verification failed."""

    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Captcha verification failed'
