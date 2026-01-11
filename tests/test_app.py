"""Test cases for the THC-BACKEND-SERVER FastAPI application."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from thc_backend_server.app import _add_exception_handlers, _create_app, app_

TEST_ORIGIN = "http://test.com"


def test_create_app_initializes_and_includes_routers() -> None:
    """Test FastAPI app initialization and routers."""
    app = _create_app(
        allow_origins=[TEST_ORIGIN],
    )
    client = TestClient(app)
    # CORS headers
    response = client.options("/", headers={"Origin": TEST_ORIGIN})
    assert "access-control-allow-origin" in response.headers


def test_healthz_endpoint() -> None:
    client = TestClient(app_)
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json() == {"status": True}


def test_readyz_endpoint() -> None:
    client = TestClient(app_)
    resp = client.get("/readyz")
    assert resp.status_code == 200
    assert resp.json() == {"status": True}


def test_cors_headers_present() -> None:
    client = TestClient(app_)
    resp = client.options("/", headers={"Origin": TEST_ORIGIN})
    # Should allow all origins by default
    assert resp.headers.get("access-control-allow-origin") == "*"


def test_generic_exception_handler_returns_500() -> None:
    app = FastAPI()

    @app.get("/raise")
    async def raise_error():
        raise RuntimeError("fail")

    _add_exception_handlers(app)
    client = TestClient(app, raise_server_exceptions=False)
    resp = client.get("/raise")
    assert resp.status_code == 500
    assert resp.json() == {"detail": "Internal server error"}
