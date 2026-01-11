# Python Template
This is a template for python projects.

## Prerequisites
1. An environment with Ubuntu or Alpine
2. At least one of python3.x is Installed
3. Corresponding python3.x-venv is installed

## QuickStart
1. create virtual environment
    ```
    bash dev/venv-create
    source .venv/bin/activate
    ```
2. install uv
    ```
    bash dev/uv-install.sh
    ```
3. set up python project
    ```
    ./dev/bootstrap.sh
    ```
3. run your app
    ```
    python main.py
    ```
4. format and test before commit
    ```
    bash dev/format-and-test.sh
    ```
