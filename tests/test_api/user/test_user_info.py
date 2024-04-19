from dirty_equals import IsStr
from httpx import AsyncClient
from starlette import status

from api.authentication.classes import JwtUser
from tests import const


async def test_user_info(client: AsyncClient, auth_data: JwtUser):
    """Test user info."""
    response = await client.get(url=const.USER_INFO_URL, headers=auth_data.header)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'id': auth_data.user_id,
        'name': IsStr(min_length=3),
    }
