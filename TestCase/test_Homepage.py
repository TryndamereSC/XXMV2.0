# !/usr/bin python3                                 
# encoding   :   utf-8 -*-                            
# author     :   浮川                              
# File       :   Test_Homepage.py
# Date       :   2021/6/21 9:57


import allure
import requests
import time
from pytest_check import check
from Business.common import MyTools

time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))

mt = MyTools()


@allure.feature('首页数据')
def test_Homepage_02():
    """"首页数据"""
    query_params = {
        "access_token": mt.get_token(),
        "order": "+dorder",
        "appcode": "ROBOT",
        "userid": "1"
    }

    r = requests.get(url=mt.data_url+"/v1/uac/user/pagefunctiontree", params=query_params)

    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200




@allure.story('场景运行状态')
def test_Business_status_03():
    """场景运行状态"""
    query_params = {
        "access_token": mt.get_token(),
        "business_type": "1"
    }
    r = requests.get(url=mt.data_url+"/v1/oper/businesses", params=query_params)

    print(r.json())
    with check:
        assert r.status_code == 200




@allure.story('页面功能树')
def test_pagefunctiontree_04():
    """"页面功能树"""
    query_params = {
        "access_token" : mt.get_token(),
        "order" : "+dorder",
        "appcade" : "ROBOT",
        "userid" : "1"
    }
    r = requests.get(url= mt.data_url+"/v1/uac/user/pagefunctiontree",params=query_params)

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('异常场景展示')
def test_get_disable_business_05():
    """"异常场景展示"""
    query_params = {
        "access_token" : mt.get_token()
    }
    r = requests.get(url= mt.data_url+"/v1/oper/get_disable_business",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('外呼线路运行设备信息')
def test_get_device_count_info_06():
    """"外呼线路运行设备信息"""
    query_params = {
     "access_token" : mt.get_token()
    }
    r = requests.get(url= mt.data_url+"/v1/oper/device/get_device_count_info",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000  #存在无异常场景情况



@allure.story('获取当前登录用户的所有场景跟进列表')
def test_todo_07():
    """获取当前登录用户的所有场景跟进列表"""
    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/biz/followup/todo", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   #该账号未分配跟进数据





@allure.story('获取正在拨打场景')
def test_get_calling_biz_08():
    """获取正在拨打场景"""
    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/oper/get_calling_biz", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   #部分场景没有在作业中




@allure.story('获取用户标签统计')
def test_get_result_status_count_09():
    """获取用户标签统计"""
    time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    query_params = {
        "access_token": mt.get_token(),
        "business_type" : "1",
        "begin_time" : time_stamp,
        "end_time" : time_stamp
    }
    r = requests.get(url=mt.data_url + "/v1/robot/dial_result_count/get_result_status_count", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   #无用户标签数据




@allure.story('获取高意向用户标签按时间统计')
def test_get_select_result_status_count_time_10():
    """获取高意向用户标签按时间统计"""
    # time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    query_params = {
        "access_token": mt.get_token(),
        "business_type" : "1",
        "begin_time" : time_stamp,
        "end_time": time_stamp,
        "graph" : "true"
    }
    r = requests.get(url=mt.data_url + "/v1/robot/dial_result_count/get_select_result_status_count_time", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000




@allure.story('获取异常场景')
def test_get_disable_business_11():
    """获取异常场景"""
    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/oper/get_disable_business", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('场景列表')
def test_businesses_12():
    """场景列表"""
    query_params = {
        "access_token": mt.get_token(),
        "business_type" : "2"
    }
    r = requests.get(url=mt.data_url + "/v1/oper/businesses", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



