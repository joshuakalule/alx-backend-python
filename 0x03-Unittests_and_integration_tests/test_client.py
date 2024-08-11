#!/usr/bin/env python3
"""Test module to test methods in client module."""


import client  # type: ignore
from parameterized import parameterized, parameterized_class  # type: ignore
import unittest  # type: ignore
from unittest.mock import patch, Mock, PropertyMock  # type: ignore
from fixtures import TEST_PAYLOAD
from typing import Any


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Test on GithubOrgClient.public_repos in an integration test

    Tests that calling public_repos() method works well as it depends on;
    public_repos() < repos_payload() < _public_repos_url < org()

    This is performed by only mocking calls that access external resources
    such as requests.get in get_json
    Other calls are not mocked
    """

    @classmethod
    def setUpClass(cls):
        """
        Initiate a patcher for 'requests.get' such that
        requests.get(url).json() returns based on url
        """
        cls.test_org = 'example'
        cls.apache_license_key = 'apache-2.0'

        def get_return(expected: str = None) -> Any:
            """Helper function"""
            test_repos_url = cls.org_payload['repos_url']
            test_org_url = f"https://api.github.com/orgs/{cls.test_org}"
            available = {
                test_org_url: cls.org_payload,
                test_repos_url: cls.repos_payload
            }
            if expected not in available:
                answer = None
            answer = available[expected]

            mock = Mock()
            mock.json.return_value = answer

            return mock

        cls.get_patcher = patch('utils.requests.get', side_effect=get_return)

        cls.mock_requests_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stops the patch on requests.get"""
        cls.get_patcher.stop()

    def setUp(self):
        """Create client"""
        self.test_client = client.GithubOrgClient(self.test_org)

    def tearDown(self):
        """Delete client"""
        del self.test_client

    def test_public_repos_no_license(self):
        """
        Test the public_repos method
        when called with no license returns all repos
        """
        self.assertEqual(self.test_client.public_repos(), self.expected_repos)

    def test_public_repos_have_licenses(self):
        """
        Test that public repos method when called with a license,
        returns the right repos
        """
        test_repos = self.test_client.public_repos(self.apache_license_key)
        self.assertEqual(test_repos, self.apache2_repos)


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClientClass."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, answer):
        """Test test_has_license() method."""
        test_client = client.GithubOrgClient("test")
        test_result = test_client.has_license(repo, license_key)
        self.assertEqual(test_result, answer)

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
