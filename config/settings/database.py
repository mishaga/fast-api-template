from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from config import const


class DatabaseSettings(BaseSettings):
    """Database settings."""

    model_config = SettingsConfigDict(
        extra=const.IGNORE_STR,
        env_file=const.ENV_FILENAME,
        env_prefix='POSTGRES_',
    )

    host: str
    port: str = '5432'
    user: str
    password: SecretStr
    database: str

    def get_async_connection_link(self) -> str:
        """Return string for async database connection.

        Returns:
            credentials for async database connection
        """
        return 'postgresql+asyncpg://{credentials}'.format(
            credentials=self._get_credentials(),
        )

    def get_sync_connection_link(self) -> str:
        """Return string for sync database connection.

        Returns:
            credentials for sync database connection
        """
        return 'postgresql+psycopg2://{credentials}'.format(
            credentials=self._get_credentials(),
        )

    def _get_credentials(self) -> str:
        """Return string of database credentials.

        Returns:
            credentials for database connection
        """
        return '{user}:{password}@{host}:{port}/{database}'.format(
            user=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.database,
        )
