import typing
from pathlib import Path

SITE_NAME: typing.Final[str] = 'project.local'
SITE_URL: typing.Final[str] = f'https://{SITE_NAME}'

LOGGER_API: typing.Final[str] = 'api'

ENV_FILENAME: typing.Literal['.env'] = '.env'
IGNORE_STR: typing.Literal['ignore'] = 'ignore'
DEFAULT_STR: typing.Literal['default'] = 'default'

PROJECT_ROOT_PATH = Path(__file__).parent.parent
STATIC_PATH = PROJECT_ROOT_PATH / 'static'

DEFAULT_TOKEN_EXPIRATION_DAYS: typing.Final[int] = 180
