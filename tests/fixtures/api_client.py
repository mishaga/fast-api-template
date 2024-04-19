import pytest
from httpx import AsyncClient

from api.app import app
from tests.const import BASE_API_URL, SCOPE_FUNCTION


@pytest.fixture(scope=SCOPE_FUNCTION)
async def client() -> AsyncClient:
    """Test api client."""
    async with AsyncClient(app=app, base_url=BASE_API_URL) as api_client:
        yield api_client
