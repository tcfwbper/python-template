# Copyright 2025 Tsung-Han Chang. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Main FastAPI application for THC-BACKEND-SERVER."""
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any, cast

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .logger import logger_


@asynccontextmanager
async def lifespan(
    app: FastAPI,  # pylint: disable=unused-argument,redefined-outer-name
) -> AsyncGenerator[None, None]:
    """Manage application lifespan events.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    # startup
    logger_.info("Starting up application")

    yield

    # housekeeping
    logger_.info("Application shutdown completed")


def _add_additional_routes(app: FastAPI) -> None:  # pylint: disable=redefined-outer-name
    """Add /healthz endpoint to the FastAPI app."""

    @app.get("/healthz")
    async def healthz() -> dict[str, bool]:
        return {"status": True}

    @app.get("/readyz")
    async def readyz() -> dict[str, bool]:
        return {"status": True}


def _add_exception_handlers(fastapi_app: FastAPI) -> None:
    """Add generic exception handler to the FastAPI app.

    Args:
        fastapi_app (FastAPI): The FastAPI application instance.
    """

    @fastapi_app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request, exc: Exception  # pylint: disable=unused-argument
    ) -> JSONResponse:
        """Handle uncaught exceptions and return a generic error response.

        Args:
            request (Request): The incoming request.
            exc (Exception): The exception that was raised.

        Returns:
            JSONResponse: A generic 500 error response.
        """
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"},
        )


def _create_app(
    allow_origins: list[str] | None = None,
) -> FastAPI:
    """Create and configure the FastAPI application.

    Args:
        allow_origins (list[str] | None): List of allowed CORS origins.

    Returns:
        FastAPI: Configured FastAPI application.
    """
    allow_origins = allow_origins or ["*"]

    fastapi_app = FastAPI(lifespan=lifespan)

    _add_additional_routes(fastapi_app)
    _add_exception_handlers(fastapi_app)

    cast(Any, fastapi_app).add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return fastapi_app


app_ = _create_app()
