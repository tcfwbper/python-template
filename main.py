"""Entrypoint for running the THC-BACKEND-SERVER FastAPI application."""
import uvicorn

from thc_backend_server import app_

if __name__ == "__main__":
    uvicorn.run(
        app_,
        host="0.0.0.0",
        port=int(8080),
        workers=1,
    )
