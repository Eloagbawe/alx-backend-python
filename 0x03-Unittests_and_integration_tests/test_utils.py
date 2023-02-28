#!/usr/bin/env python3
"""This file contains the TestAccessNestedMap class"""
import unittest
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """The TestAccessNestedMap class"""
    @parameterized.expand([
        ({"a": 1}, ('a', ), 1),
        ({"a": {"b": 2}}, ('a', ), {"b": 2}),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: Any) -> Any:
        """The test_access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ('a'), KeyError),
        ({"a": 1}, ('a', 'b'), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, result: Any) -> Any:
        """The test_access_nested_map_exception function"""

        with self.assertRaises(result):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """The TestGetJson Class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url: str, test_payload: Dict,
                      mock_request: Callable) -> None:
        """The test_get_json function"""

        mock_response = MagicMock()
        mock_response.json.return_value = test_payload

        mock_request.get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """The TestMemoize class"""
    def test_memoize(self):
        """the test_memoize class"""

        class TestClass:
            """The TestClass"""

            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test_class = TestClass()
            res = test_class.a_property
            res2 = test_class.a_property
            self.assertTrue(res, 42)
            self.assertTrue(res, 42)

        mock_method.assert_called_once()
