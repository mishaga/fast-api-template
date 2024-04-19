from http import HTTPMethod

from fastapi import APIRouter, Depends
from starlette import status

from api.authentication.depends import auth_user_only
from api.methods.user.user_info import user_info

router = APIRouter(
    prefix='/user',
    tags=['User'],
    dependencies=[Depends(auth_user_only)],
)

router.add_api_route(
    path='/info',
    endpoint=user_info,
    methods=[HTTPMethod.GET],
    status_code=status.HTTP_200_OK,
)
