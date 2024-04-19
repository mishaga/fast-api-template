import datetime
from zoneinfo import ZoneInfo

from config import settings


def now() -> datetime.datetime:
    """Return current datetime with timezone.

    Returns:
        current datetime with timezone
    """
    return datetime.datetime.now(tz=ZoneInfo(settings.project.timezone))
