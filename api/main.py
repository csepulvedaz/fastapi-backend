from logging.config import dictConfig

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

# Constants
from api.constants.error_constants import VALIDATION_ERROR

# Config
from api.core.config import (
    app_config,
    logs_config,
)
from api.core.prisma import prisma

# Routes
from api.routes import *


dictConfig(logs_config)

app = FastAPI(**app_config)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_, exc: RequestValidationError):
    return VALIDATION_ERROR.send(validation_error=exc)


@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()


app.include_router(root_routes)
app.include_router(auth_routes)
app.include_router(user_routes)
