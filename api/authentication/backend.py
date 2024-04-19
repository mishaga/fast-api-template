import jwt
from starlette.authentication import (
    AuthCredentials,
    AuthenticationBackend,
    BaseUser,
)
from starlette.requests import HTTPConnection

from api import exceptions
from api.authentication.classes import JwtDataVersion1, JwtErrorUser, JwtUser
from api.authentication.json_web_token import decode_token


class AuthBackend(AuthenticationBackend):
    """Custom auth backend class."""

    async def authenticate(self, conn: HTTPConnection) -> tuple[AuthCredentials, BaseUser]:
        """Authenticate method for the backend.

        Parameters:
            conn: an HTTPConnection

        Returns:
            tuple with AuthCredentials and a user
        """
        try:  # noqa: WPS229 Found too long try body length
            token = _get_token_from_headers(conn)
            decoded_data = _decode_token(token)
        except exceptions.auth.BaseApiException as exc:
            return AuthCredentials(None), JwtErrorUser(exc.status_code, exc.detail)

        return AuthCredentials(['authenticated']), JwtUser(decoded_data['user_id'], token)


def _get_token_from_headers(conn: HTTPConnection) -> str:
    """Return value of auth header.

    Parameters:
        conn: an HTTPConnection

    Returns:
         value of auth header

    Raises:
        NoAuthHeader: when auth header was not passed
        InvalidAuthHeader: when header is invalid
        InvalidAuthScheme: when auth scheme is not "Bearer"
    """
    if 'Authorization' not in conn.headers:
        raise exceptions.token.NoAuthHeader()

    auth = conn.headers['Authorization']

    try:
        scheme, token = auth.split()
    except Exception:
        raise exceptions.token.InvalidAuthHeader()

    if scheme.lower() != 'bearer':
        raise exceptions.token.InvalidAuthScheme()

    return token


def _decode_token(token: str) -> JwtDataVersion1:
    """Check token.

    Parameters:
        token: jwt token value

    Returns:
        decoded data (dict, should be JwtDataVersion1)

    Raises:
        TokenExpired: when token has expired
        InvalidAuthHeader: when token cannot be decoded
    """
    try:
        return decode_token(token=token)
    except jwt.exceptions.ExpiredSignatureError:
        raise exceptions.token.TokenExpired()
    except Exception:
        raise exceptions.token.InvalidAuthHeader()
