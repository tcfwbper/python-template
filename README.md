# Python Template
This is a template for python projects.

## Prerequisites
1. An environment with Ubuntu OS
2. At least one of python3.x is Installed
3. Corresponding python3.x-venv is installed

## QuickStart
1. create virtual environment
    ```
    ./dev/venv-create
    source .venv/bin/activate
    ```
2. set up python project
    ```
    ./dev/bootstrap.sh
    ```
3. run your app
    ```
    python3 src/my_python_project/app.py
    ```
4. format and test before commit
    ```
    ./dev/format-and-test.sh
    ```
