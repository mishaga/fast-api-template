import types
import typing
from http import HTTPMethod

from tests.helper_classes import AuthUrlData

BASE_API_URL: typing.Final[str] = 'http://project-api.test'

SCOPE_SESSION: typing.Literal['session'] = 'session'
SCOPE_FUNCTION: typing.Literal['function'] = 'function'

TEST_EMAIL = 'abc@test.com'
TEST_CAPTCHA_VALUE = 'any-string'
TELEGRAM_CHAT_ID = 123

HOME_URL = '/'
HEALTH_URL = '/health'
FAVICON_URL = '/favicon.ico'

USER_INFO_URL = '/user/info'

# auth-closed API URLs
AUTH_URLS = (
    AuthUrlData(method=HTTPMethod.GET, url=USER_INFO_URL),
)

# all API URLs and theirs allowed methods
URL_METHODS = types.MappingProxyType({
    HOME_URL: {HTTPMethod.GET},
    HEALTH_URL: {HTTPMethod.GET},
    FAVICON_URL: {HTTPMethod.GET},

    USER_INFO_URL: {HTTPMethod.GET},

    '/redoc': {HTTPMethod.HEAD, HTTPMethod.GET},
    '/openapi.json': {HTTPMethod.HEAD, HTTPMethod.GET},
    '/docs': {HTTPMethod.HEAD, HTTPMethod.GET},
    '/docs/oauth2-redirect': {HTTPMethod.HEAD, HTTPMethod.GET},
})
