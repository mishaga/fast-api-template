from functools import cache

import sentry_sdk

from config import settings


@cache
def init() -> None:
    """Init sentry."""
    if settings.project.sentry_dsn.get_secret_value():
        sentry_sdk.init(
            dsn=settings.project.sentry_dsn.get_secret_value(),
            environment=settings.project.environment,
            release=settings.project.version,
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
        )
