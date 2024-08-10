#!/usr/bin/env python3
"""Task 0. Parametize a unit test."""

import unittest  # type: ignore
from parameterized import parameterized  # type: ignore
from utils import access_nested_map  # type: ignore
from typing import Any  # type: ignore


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

    @parameterized.expand([
        ({}, ("a", )),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: dict,
                                         path: tuple) -> None:
        """Test that nested_map called with path raises KeyError."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
