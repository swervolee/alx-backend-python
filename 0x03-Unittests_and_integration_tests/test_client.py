#!/usr/bin/env python3
"""
Test the client module
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests the github client class
    """
    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, param, mock_get_json):
        """
        Tests the org method
        """
        # mock_get_json.return_value = None

        obj = GithubOrgClient(param)
        org_data = obj.org()

        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{param}")
