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


def test_findCallLogList_44():

    query_params = {
        "access_token": mt.get_token(),
        "startTime": mt.startTime(),
        "endTime": mt.endTime(),
        "offset": 1,
        "limit": 10,
        "order": "",
        "businessId": mt.get_robot_dict()['bizId'],
        "bank_org" : ""

    }
    r = requests.get(url=mt.data_url + "/v1/robot/report/findCallLogList", params=query_params)
    print(r.json())
    print(mt.startTime())
    print(mt.endTime())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   部分场景没有拨打详情



