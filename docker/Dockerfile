FROM python:3.10.13-alpine

WORKDIR /app
RUN --mount=type=cache,sharing=locked,mode=0777,target=/app/.cache/uv,id=uv \
    --mount=from=ghcr.io/astral-sh/uv:0.6.12,source=/uv,target=/usr/bin/uv \
    --mount=type=bind,target=uv.lock,src=uv.lock \
    --mount=type=bind,target=pyproject.toml,src=pyproject.toml \
    uv sync --locked --no-dev --no-install-project -p 3.10.13

ENV PATH="/app/.venv/bin:$PATH" \
    UV_PYTHON=/app/.venv/bin/python

COPY src/thc_backend_server ./thc_backend_server
COPY main.py .

ENTRYPOINT ["python", "main.py"]
