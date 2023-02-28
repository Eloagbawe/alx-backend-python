#!/usr/bin/env python3
"""This file contains classes to test client.py"""
import unittest
from unittest import mock

from client import GithubOrgClient
from utils import get_json
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from requests import HTTPError
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """The TestGithubOrgClient Class"""

    @parameterized.expand([
        ('google', 'https://api.github.com/orgs/google'),
        ('abc', 'https://api.github.com/orgs/abc')
    ])
    @patch('utils.requests')
    def test_org(self, org: str, result: str, mock_requests: Callable) -> None:
        """The test_org method"""
        mock_response = MagicMock()
        mock_response.json.return_value = result
        mock_requests.get.return_value = mock_response

        client_class = GithubOrgClient(org)
        self.assertEqual(client_class.org, result)
        # mock_response.assert_called_once_with(
        #     "https://api.github.com/orgs/{}".format(org)
        # )

    def test_public_repos_url(self) -> None:
        """The test_public_repos_url method"""
        with mock.patch('client.GithubOrgClient.org',
                        new_callable=PropertyMock) as mock_method:
            mock_method.return_value = {
                'repos_url': 'https://api.github.com/google/repos'
            }
            client_class = GithubOrgClient('google')
            self.assertEqual(client_class._public_repos_url,
                             'https://api.github.com/google/repos')

    @patch('client.get_json')
    def test_public_repos(self, mock_requests: MagicMock) -> None:
        """The test_public_repos_url method"""
        payload = {
            'repos_url': 'https://api.github.com/google/repos',
            'payload': [
                {'name': 'https://api.github.com/google/repos/1'},
                {'name': 'https://api.github.com/google/repos/2'},
                {'name': 'https://api.github.com/google/repos/3'},
            ]
        }
        mock_requests.return_value = payload['payload']
        with mock.patch('client.GithubOrgClient._public_repos_url',
                        new_callable=PropertyMock) as mock_property:
            mock_property.return_value = payload["repos_url"]
            client_class = GithubOrgClient('google')
            self.assertEqual(client_class.public_repos(), [
                'https://api.github.com/google/repos/1',
                'https://api.github.com/google/repos/2',
                'https://api.github.com/google/repos/3'
            ])
            mock_requests.assert_called_once()
        mock_property.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, result: bool) -> None:
        """The test_has_license method"""
        client_class = GithubOrgClient('google')
        self.assertEqual(client_class.has_license(repo, license_key), result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
