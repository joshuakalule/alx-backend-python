#!/usr/bin/env python3
"""Test module to test methods in client module."""


import client  # type: ignore
from parameterized import parameterized  # type: ignore
import unittest  # type: ignore
from unittest.mock import patch  # type: ignore


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClientClass."""

    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'}),
    ])
    def test_org(self, org: str, response: dict) -> None:
        """Test the org method."""
        with patch('client.get_json', return_value=response) as mock_get_json:
            test_client = client.GithubOrgClient(org)

            test_response = test_client.org
            expected_url = f"https://api.github.com/orgs/{org}"
            mock_get_json.assert_called_once_with(expected_url)

            self.assertEqual(test_response, response)
