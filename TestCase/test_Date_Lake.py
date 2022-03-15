# !/usr/bin python3
# encoding   :   utf-8 -*-
# author     :   浮川
# File       :   Test_Data_Lake.py
# Date       :   2022/3/15 15:08

import requests
import time
import json
import allure
from pytest_check import check
from Business.common import MyTools

mt= MyTools()

@allure.feature('数据湖列表')
def test_getDataSourceBatchList_154():

    query_params = {
        "access_token" : mt.get_token(),
        "pageSize" : 10,
        "page" : 1,
        "orderBy" : "time_create desc"
    }
    r = requests.get(url= mt.data_url+"/v1/oper/datasource/getDataSourceBatchList",params=query_params)

    print(r.json())
    with check:
        assert r.json()['code'] == 20000
        assert r.status_code == 200

