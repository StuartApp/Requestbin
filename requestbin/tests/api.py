import os
import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

def create_bin(data):
    url = BASE_URL + "/api/v1/bins"
    req = requests.post(url=url, data=data)
    return req

def create_webhook(bin_name, data=None):
    url = BASE_URL + '/' + bin_name
    req = requests.post(url=url, data=data)
    return req

def get_bin(bin_name):
    url = BASE_URL + "/api/v1/bins/" + bin_name
    req = requests.get(url=url)
    return req

def get_bin_requests(bin_name):
    url = BASE_URL + '/api/v1/bins/' + bin_name + '/requests'
    req = requests.get(url=url)
    return req
