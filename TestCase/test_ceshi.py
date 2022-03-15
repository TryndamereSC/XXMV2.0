# !/usr/bin python3
# encoding   :   utf-8 -*-
# author     :   浮川
# File       :   test_ceshi.py
# Date       :   2021/6/21 15:00

import requests
import pytest
import time
from datetime import datetime, timedelta
import json
import jsonpath
import uuid
import allure
from pytest_check import check
from Business.common import MyTools

# time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# time_stamp1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# time_stamp2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))


mt = MyTools()

def test_get_result_53():

    query_params = {
        "biz_uni_key": mt.get_robot_dict()['biz_uni_key'],
        "access_token": mt.get_token(),
        "with_default" : 0
    }
    r = requests.get(url=mt.data_url + "/v1/robot/robot_result_status/get_result", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000 or 20003
