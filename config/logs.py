import datetime
import json
import logging.config  # noqa: WPS301 Found dotted raw import
from functools import cache
from types import MappingProxyType
from zoneinfo import ZoneInfo

from common_functions import env
from config import const, context

_DEBUG_LOGGER = MappingProxyType({
    'level': logging.DEBUG,
    'handlers': {const.DEFAULT_STR},
})
_WARNING_LOGGER = MappingProxyType({
    'level': logging.WARNING,
    'handlers': {const.DEFAULT_STR},
})


class JsonFormatter(logging.Formatter):
    """JSON log formatter."""

    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON.

        Parameters:
            record: a log record to format

        Returns:
            json log string
        """
        now = datetime.datetime.now(tz=ZoneInfo('UTC'))
        json_message = {
            'level': record.levelname,
            '@timestamp': f'{now.isoformat()}Z',
            'logger': record.name,
            'data': {
                'message': record.getMessage(),
                'entrypoint': context.entrypoint.get(None),
            },
        }

        if record.exc_info and not record.exc_text:
            record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            json_message['exception'] = record.exc_text
        if record.stack_info:
            json_message['stack_trace'] = self.formatStack(record.stack_info)

        return json.dumps(json_message, ensure_ascii=False)


@cache
def setup_logging():
    """Set up logging."""
    if env.is_test():
        return
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            const.DEFAULT_STR: {
                '()': 'config.logs.JsonFormatter',
            },
        },
        'handlers': {
            const.DEFAULT_STR: {
                'class': 'logging.StreamHandler',
                'formatter': const.DEFAULT_STR,
            },
        },
        'root': _DEBUG_LOGGER,
        'loggers': {
            'apscheduler': _WARNING_LOGGER,
            'asyncio': _WARNING_LOGGER,
            'uvicorn': _WARNING_LOGGER,
            'pika': _WARNING_LOGGER,
            'dramatiq': _WARNING_LOGGER,
            'tasks': _WARNING_LOGGER,
            'httpcore': _WARNING_LOGGER,
            'httpx': _WARNING_LOGGER,
            'tzlocal': _WARNING_LOGGER,
        },
    })
