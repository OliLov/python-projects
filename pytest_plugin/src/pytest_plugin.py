"""Pytest plugin, register assert rewrite."""
import pytest

pytest.register_assert_rewrite("test.assertions")
