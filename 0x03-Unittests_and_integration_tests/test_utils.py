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
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


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
