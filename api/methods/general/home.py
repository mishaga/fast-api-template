from api import responses
from config import settings


async def home() -> responses.HomeResponse:
    """Home page.

    Returns:
        model with basic project information
    """
    return responses.HomeResponse(
        service=settings.project.name,
        version=settings.project.version,
        environment=settings.project.environment,
    )
