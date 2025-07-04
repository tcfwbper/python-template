#!/bin/bash
set -e
cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/../

echo "=== test.sh ==="

echo "- Start Python checks"

echo "- isort: start"
python -m isort --check-only src/my_python_project
echo "- isort: done"

echo "- black: start"
python -m black --check src/my_python_project
echo "- black: done"

echo "- docformatter: start"
python -m docformatter -c -r src/my_python_project
echo "- docformatter:  done"

echo "- ruff: start"
python -m ruff check src/my_python_project
echo "- ruff: done"

echo "- mypy: start"
python -m mypy src/my_python_project
echo "- mypy: done"

echo "- pylint: start"
python -m pylint src/my_python_project
echo "- pylint: done"

echo "- flake8: start"
python -m flake8 src/my_python_project
echo "- flake8: done"

echo "- pytest: start"
if [[ "$1" == "--skip-slow" ]]; then
  python -m pytest --cov=src/my_python_project --disable-warnings -m "not slow"
else
  python -m pytest --cov=src/my_python_project --disable-warnings
fi
echo "- pytest: done"

echo "- All Python checks passed"
