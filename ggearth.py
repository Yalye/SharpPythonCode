# -*- coding: utf-8 -*-
# @Time : 2021/11/18 17:30
# @Author : nobody
# @File : ggearth.py
# @Software: PyCharm

import ee

import os
import requests

proxy = 'http://127.0.0.1:58591'

os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

def get_location():
    resp_data = requests.get('http://ip-api.com/json').json()
    print(resp_data)

get_location()

# ee.Authenticate()

# ee.Authenticate("4/1AX4XfWhk04hsLO-zD_m7Pgki6fJI4uNKIxJRDH9i2uJ7xS1Yl_ZfYjSlhBY")

# ee.Initialize()




