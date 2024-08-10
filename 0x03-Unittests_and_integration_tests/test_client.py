#!/usr/bin/env python3
"""Test module to test methods in client module."""


import client  # type: ignore
from parameterized import parameterized  # type: ignore
import unittest  # type: ignore
from unittest.mock import patch, PropertyMock  # type: ignore


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClientClass."""

    @parameterized.expand([
        ('google', {'repos_url': 'https://api.github.com/orgs/google/repos'})
    ])
    def test_public_repos_url(self, org, payload):
        """Test the public_repos_url property."""
        target = 'client.GithubOrgClient.org'
        with patch(target, new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload

            test_client = client.GithubOrgClient(org)

            expected = payload['repos_url']
            self.assertEqual(test_client._public_repos_url, expected)

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
