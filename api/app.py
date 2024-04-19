from http import HTTPMethod

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware

from api.authentication.backend import AuthBackend
from api.middlewares import ContextMiddleware
from api.params import get_origins, get_settings
from api.routers import general, user
from config import logs, sentry

sentry.init()
logs.setup_logging()

app = FastAPI(**get_settings())

app.add_middleware(ContextMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_origins(),
    allow_credentials=True,
    allow_methods={HTTPMethod.GET, HTTPMethod.POST, HTTPMethod.PATCH, HTTPMethod.DELETE},
    allow_headers={'Content-Type', 'Authorization'},
)
app.add_middleware(AuthenticationMiddleware, backend=AuthBackend())

app.include_router(general.router)
app.include_router(user.router)
