from typing import Any


def pytest_collection_modifyitems(session: Any, config: Any, items: list[Any]) -> None:
    """Modify the order of test collection based on predefined file order.

    Args:
        session: The pytest session object.
        config: The pytest config object.
        items: List of collected test items.
    """
    order = {
        "test_app.py": 0,
        "test_logger.py": 1,
    }

    items.sort(key=lambda item: order.get(item.module.__file__.split("/")[-1], float("inf")))
