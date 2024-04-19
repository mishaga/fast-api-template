from http import HTTPMethod

import pytest
from fastapi.routing import APIRoute
from httpx import AsyncClient
from starlette import status

from api.app import app
from tests import const


@pytest.mark.parametrize('methods_data', const.URL_METHODS.items())
@pytest.mark.parametrize('check_method', HTTPMethod)
async def test_wrong_method(
    client: AsyncClient,
    methods_data: tuple[str, set[str]],
    check_method: str,
):
    """Test unexpected method."""
    url, allowed_methods = methods_data
    if check_method not in allowed_methods:
        response = await client.request(method=check_method, url=url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        if check_method == HTTPMethod.HEAD:
            assert response.text == ''
        else:
            assert response.json() == {'detail': 'Method Not Allowed'}


@pytest.mark.parametrize('route', app.routes)
async def test_list_urls(route: APIRoute):
    """Test if url is present in ultimate list."""
    assert route.path in const.URL_METHODS, f'URL "{route.path}" not found in allowed list'
