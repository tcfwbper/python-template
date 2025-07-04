# pylint: disable=unused-argument
"""Pytest configuration for MyPythonPorject.

Defines custom markers and test collection ordering.
"""
from typing import Any


def pytest_configure(config: Any) -> None:
    """Register custom markers for pytest.

    Args:
        config: The pytest config object.
    """
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(session: Any, config: Any, items: list[Any]) -> None:
    """Modify the order of test collection based on predefined file order.

    Args:
        session: The pytest session object.
        config: The pytest config object.
        items: List of collected test items.
    """
    order = {
        "test_app.py": 0,
    }

    items.sort(
        key=lambda item: order.get(item.module.__file__.split("/")[-1], float("inf"))
    )
