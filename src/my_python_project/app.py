"""Main FastAPI application for MyPythonPorject."""

import logging
import os

import filelock
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def create_app(
    allow_origins: list[str] | None = None,
) -> FastAPI:
    """Create and configure the FastAPI application.

    Args:
        allow_origins (list[str] | None): List of allowed CORS origins.

    Returns:
        FastAPI: Configured FastAPI application.
    """
    allow_origins = allow_origins or ["*"]
    fastapi_app = FastAPI()
    # fastapi_app.include_router(<your_router>)
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return fastapi_app


def add_exception_handlers(fastapi_app: FastAPI) -> None:
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


# prevent accessing db simultaneously
init_lock = filelock.FileLock("/tmp/init_my_python_project.lock")
with init_lock.acquire(timeout=300):
    app = create_app()
    add_exception_handlers(app)

if __name__ == "__main__":
    uvicorn.run(
        "my_python_project.app:app",
        host="0.0.0.0",
        port=int(os.getenv("my_python_project", "5050")),
        workers=1,
    )
