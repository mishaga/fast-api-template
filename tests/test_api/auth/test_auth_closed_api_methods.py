import uuid

import pytest
from httpx import AsyncClient
from starlette import status

from api.authentication.json_web_token import generate_token
from common_functions import dates
from db import models
from tests import const
from tests.helper_classes import AuthUrlData


@pytest.mark.parametrize('url_data', const.AUTH_URLS)
async def test_no_auth(client: AsyncClient, url_data: AuthUrlData):
    """Test request to auth-closed methods with no auth data."""
    response = await client.request(method=url_data.method, url=url_data.url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Unauthorized'}


@pytest.mark.parametrize('url_data', const.AUTH_URLS)
@pytest.mark.parametrize('header', (
    'pascal python rust',
    'bearer 123 456',
    'bearer 123',
    'bearer 123.456',
    'bearer 123.456.789',
    'bearer ',
    'bearer',
))
async def test_invalid_auth_credentials(
    client: AsyncClient,
    url_data: AuthUrlData,
    header: str,
):
    """Test request to auth-closed methods with invalid auth data."""
    response = await client.request(
        method=url_data.method,
        url=url_data.url,
        headers={
            'Authorization': header,
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': 'Invalid auth header'}


@pytest.mark.parametrize('url_data', const.AUTH_URLS)
@pytest.mark.parametrize('header', (
    f'Basic {uuid.uuid4()}',
    f'Token {uuid.uuid4()}',
))
async def test_invalid_auth_scheme(
    client: AsyncClient,
    url_data: AuthUrlData,
    header: str,
):
    """Test request to auth-closed methods with wrong auth cheme."""
    response = await client.request(method=url_data.method, url=url_data.url, headers={
        'Authorization': header,
    })
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': 'Invalid auth scheme'}


@pytest.mark.parametrize('url_data', const.AUTH_URLS)
async def test_expired_token(
    client: AsyncClient,
    user: models.User,
    url_data: AuthUrlData,
):
    """Test expired token."""
    generated_token = generate_token(user=user, expires_at=dates.now())
    response = await client.request(
        method=url_data.method,
        url=url_data.url,
        headers={
            'Authorization': f'Bearer {generated_token.token}',
        },
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {'detail': 'Token expired'}
