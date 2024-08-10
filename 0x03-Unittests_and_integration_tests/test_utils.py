#!/usr/bin/env python3
"""Task 0. Parametize a unit test."""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for the Nested map function."""

    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple,
                               result: Any) -> None:
        """Test that nested_map, with path results into result."""
        self.assertEqual(access_nested_map(nested_map, path), result)
