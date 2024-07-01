#!/usr/bin/env python3
"""
unittests
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map as nmp
from utils import get_json
from unittest.mock import patch, Mock
import requests


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])

    def test_access_nested_map_exception(self, seq, path):
        """
        Tests the access_nested_map error raiseing
        in case of wrong key
        """
        with self.assertRaises(KeyError):
            nmp(seq, path)


class TestGetJson(unittest.TestCase):
    """
    Tests the get_json Method
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")  # Ensure the patch target is correct
    def test_get_json(self, test_url, expected_payload, mock_request):
        """
        Tests the get_json Method
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_payload
        mock_request.return_value = mock_response

        result = get_json(test_url)
        
        mock_request.assert_called_once_with(test_url)
        
        self.assertEqual(result, expected_payload)
