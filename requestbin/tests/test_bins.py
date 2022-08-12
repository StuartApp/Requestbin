import requests
import unittest
import os
import logging
from api import *


# curl -X POST -d "private=false&name=test" http://localhost:8000/api/v1/bins
# curl -X POST -d "fizz=buzz" http://localhost:8000/name

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")


class TestBinCreation(unittest.TestCase):
    def test_bin_without_name(self):
        data = {'private': False}
        req = create_bin(data)
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()["private"], False)
        self.assertEqual(req.json()["request_count"], 0)

    def test_bin_with_name(self):
        bin_name='test'
        data = {'private':False, 'name': bin_name}
        req = create_bin(data)
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()["name"], bin_name)
        self.assertEqual(req.json()["private"], False)
        self.assertEqual(req.json()["request_count"], 0)
