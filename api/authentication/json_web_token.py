import datetime

import jwt

from api.authentication.classes import GeneratedToken, JwtDataVersion1
from common_functions import dates
from config import const, settings
from db import models


def generate_token(user: models.User, expires_at: datetime.datetime | None = None) -> GeneratedToken:
    """Generate JSON Web Token for user.

    Parameters:
        user: a user to generate token for
        expires_at: when token should be expired

    Returns:
        JSON Web Token (string) and its expiration datetime
    """
    now = dates.now()

    if not expires_at:
        expires_at = now + datetime.timedelta(days=const.DEFAULT_TOKEN_EXPIRATION_DAYS)

    token = jwt.encode(
        payload=JwtDataVersion1(
            version=1,
            user_id=user.id,
            iat=now,
            exp=expires_at,
        ),
        key=settings.project.jwt_secret.get_secret_value(),
        algorithm=settings.project.jwt_algorithm,
    )
    return GeneratedToken(
        token=token,
        expires_at=expires_at,
    )


def decode_token(token: str) -> JwtDataVersion1:
    """Decode JWT.

    Parameters:
        token: a token string to decode

    Returns:
        decoded data (should be dict JwtDataVersion1)
    """
    return jwt.decode(
        jwt=token,
        key=settings.project.jwt_secret.get_secret_value(),
        algorithms=[settings.project.jwt_algorithm],
    )
