"""Assertions."""

import logging
from typing import Any


def is_eq(actual: Any, expected: Any, step: str, error_message: str) -> None:
    """Tests if actual is equal to expected.

    :param actual: The actual value.
    :param expected: The expected value.
    :param step: The step.
    :param error_message: The error message if assertion fails.
    """
    logging.info(step)

    assert actual == expected, error_message
