import pytest
from alembic import command as alembic_command
from alembic import config as alembic_config

from config import const
from tests.const import SCOPE_FUNCTION


@pytest.fixture(scope=SCOPE_FUNCTION)
def database():
    """Apply migrations before tests and downgrade afterward."""
    config_path = const.PROJECT_ROOT_PATH / 'alembic.ini'
    config = alembic_config.Config(file_=str(config_path))

    alembic_command.upgrade(config, 'head')
    yield
    alembic_command.downgrade(config, 'base')
