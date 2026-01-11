#!/bin/bash
set -e
cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/../

# Python
python -m isort src/thc_backend_server
python -m black -q src/thc_backend_server
python -m docformatter -i -r src/thc_backend_server
python -m ruff check --fix src/thc_backend_server
