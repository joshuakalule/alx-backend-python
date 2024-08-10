#!/usr/bin/env python3
"""Task 0. Parametize a unit test."""

import unittest
from unittest import mock
from parameterized import parameterized  # type: ignore
import utils  # type: ignore
from typing import Any  # type: ignore


class TestGetJson(unittest.TestCase):
    """ Test class for the get json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload) -> None:
        """Test that fetching test_url returns test_payload."""
        with unittest.mock.patch('utils.requests.get') as mock_requests_get:
            mock_response = mock.Mock()
            mock_response.json.return_value = test_payload
            mock_requests_get.return_value = mock_response

            payload = utils.get_json(test_url)
            mock_requests_get.assert_called_once_with(test_url)
            self.assertEqual(payload, test_payload)


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
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a", )),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: dict,
                                         path: tuple) -> None:
        """Test that nested_map called with path raises KeyError."""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
