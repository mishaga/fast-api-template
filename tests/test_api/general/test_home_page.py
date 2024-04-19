import jsonschema
from httpx import AsyncClient
from starlette import status

from tests import const, schemas


async def test_home_page(client: AsyncClient):
    """Test home page."""
    response = await client.get(url=const.HOME_URL)
    assert response.status_code == status.HTTP_200_OK
    jsonschema.validate(
        instance=response.json(),
        schema=schemas.HomePageSchema,
        format_checker=jsonschema.Draft202012Validator.FORMAT_CHECKER,
    )
