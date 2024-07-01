#!/usr/bin/env python3
"""
unittests
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map as nmp


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, seq, path, expectation):
        """
        Tests the access_nested_map function using
        paramerized parameters.
        """
        self.assertEqual(nmp(seq, path), expectation)
