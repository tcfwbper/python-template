#!/bin/bash
set -e
cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/../

# Python
python -m isort src/my_python_project
python -m black -q src/my_python_project
python -m docformatter -i -r src/my_python_project
python -m ruff check --fix src/my_python_project
