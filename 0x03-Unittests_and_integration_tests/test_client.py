#!/usr/bin/env python3
"""Test module to test methods in client module."""


import client  # type: ignore
from parameterized import parameterized  # type: ignore
import unittest  # type: ignore
from unittest.mock import patch, PropertyMock  # type: ignore


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClientClass."""

    @patch(
        'client.get_json',
        new_callable=PropertyMock,
        return_value=[{'name': 'repo1'}, {'name': 'repo2'}])
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos()"""
        target = 'client.GithubOrgClient._public_repos_url'
        with patch(target, new_callable=PropertyMock) as mock_property:
            mock_property.return_value = 'doesnt matter'

            test_client = client.GithubOrgClient("test")

            test_public_repos = test_client.public_repos()

            self.assertEqual(test_public_repos, ['repo1', 'repo2'])

            mock_property.assert_called_once()
            mock_get_json.assert_called_once()

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
