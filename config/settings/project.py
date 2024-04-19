from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from config import const


def _version() -> str:
    """Return project version (from file).

    Returns:
        version of the project
    """
    try:
        with open('/var/version', 'r') as version_file:
            line = version_file.readline()
    except FileNotFoundError:
        return 'unknown'

    return line.strip()


class ProjectSettings(BaseSettings):
    """Project settings."""

    model_config = SettingsConfigDict(
        extra=const.IGNORE_STR,
        env_file=const.ENV_FILENAME,
    )

    name: str = 'project_name'
    version: str = _version()
    debug: bool = False
    environment: str
    timezone: str = 'Europe/London'
    sentry_dsn: SecretStr
    jwt_secret: SecretStr
    jwt_algorithm: str = 'HS512'
