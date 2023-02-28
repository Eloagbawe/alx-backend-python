#!/usr/bin/env python3
"""This file contains classes to test client.py"""
import unittest
from unittest import mock

from client import GithubOrgClient
from utils import get_json
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


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

    def test_public_repos_url(self):
        """The test_public_repos_url"""
        with mock.patch('client.GithubOrgClient.org',
                        new_callable=PropertyMock) as mock_method:
            mock_method.return_value = {
                'repos_url': 'https://api.github.com/google/repos'
            }
            client_class = GithubOrgClient('google')
            self.assertEqual(client_class._public_repos_url,
                             'https://api.github.com/google/repos')
