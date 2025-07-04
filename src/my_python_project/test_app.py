# pylint: disable=redefined-outer-name,unused-argument
"""Test cases for the MyPythonProject FastAPI application."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from my_python_project.app import add_exception_handlers, create_app

TEST_ORIGIN = "http://test.com"


def test_create_app_initializes_and_includes_routers() -> None:
    """Test FastAPI app initialization and routers."""
    app = create_app(
        allow_origins=[TEST_ORIGIN],
    )
    client = TestClient(app)
    # CORS headers
    response = client.options("/", headers={"Origin": TEST_ORIGIN})
    assert "access-control-allow-origin" in response.headers


def test_exception_handler_returns_500() -> None:
    """Test exception handler."""
    app = FastAPI()

    @app.get("/raise")
    def raise_error() -> None:
        raise RuntimeError("fail")

    add_exception_handlers(app)
    client = TestClient(app, raise_server_exceptions=False)
    resp = client.get("/raise")
    assert resp.status_code == 500
    assert resp.json() == {"detail": "Internal server error"}
