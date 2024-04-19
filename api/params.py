import typing

from config import const, settings


def get_origins() -> set[str]:
    """Origins for API.

    Returns:
        set of allowed origins
    """
    origins = {
        const.SITE_URL,
    }
    if settings.project.debug:
        origins.add('http://127.0.0.1:5173')
        origins.add('http://localhost:5173')

    return origins


def get_settings() -> dict[str, typing.Any]:
    """Parameters for FastAPI.

    Returns:
        dict with settings
    """
    fastapi_settings = {
        'debug': settings.project.debug,
        'title': settings.project.name,
        'version': settings.project.version,
    }

    if not settings.project.debug:
        fastapi_settings['redoc_url'] = None
        fastapi_settings['docs_url'] = None
        fastapi_settings['openapi_url'] = None

    return fastapi_settings
