from http import HTTPMethod

from fastapi import APIRouter
from starlette import status

from api.methods.general.favicon import favicon
from api.methods.general.health import health
from api.methods.general.home import home

router = APIRouter(
    prefix='',
    tags=['General'],
)

router.add_api_route(
    path='/',
    endpoint=home,
    methods=[HTTPMethod.GET],
    status_code=status.HTTP_200_OK,
)
router.add_api_route(
    path='/health',
    endpoint=health,
    methods=[HTTPMethod.GET],
    status_code=status.HTTP_200_OK,
)
router.add_api_route(
    path='/favicon.ico',
    endpoint=favicon,
    methods=[HTTPMethod.GET],
    status_code=status.HTTP_200_OK,
)
