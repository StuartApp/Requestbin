import requests
import unittest
import os
import logging
from api import *

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
