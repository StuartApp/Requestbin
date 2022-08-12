import unittest
import os
from api import *

# curl -X POST -d "private=false&name=xx" http://localhost:8000/api/v1/bins
# curl -X POST -d "fizz=buzz" http://localhost:8000/xx
# curl -X GET http://localhost:8000/api/v1/bins/xx/requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")


class TestWebhookReception(unittest.TestCase):
    def setUp(self):
        self.bin_name='test'
        data = {'private':False, 'name': self.bin_name}
        create_bin(data)

    def test_sent_webhook(self):
        req = create_webhook(self.bin_name)
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.text, 'ok\n')


    def test_capture_webhook(self):
        key = 'fizz'
        value = 'buzz'
        data = {key : value}

        create_webhook(self.bin_name, data)

        req = get_bin(self.bin_name)
        self.assertTrue(req.json()["request_count"] > 0)

        req=get_bin_requests(self.bin_name)
        self.assertEqual(req.json()[0]['path'], '/' + self.bin_name)
        self.assertTrue(req.json()[0]['headers']['Host'] in BASE_URL)
        self.assertTrue(key, value in str(req.json()[0]['raw']))
        self.assertTrue(key, value in str(req.json()[0]['form_data']))

