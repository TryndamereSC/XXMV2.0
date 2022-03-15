# !/usr/bin python3                                 
# encoding   :   utf-8 -*-                            
# author     :   浮川                              
# File       :   Customer follow-up.py
# Date       :   2021/7/20 15:45
import allure
import requests
import time
import json
import pytest
from pytest_check import check
from Business.common import MyTools


mt = MyTools()


@allure.feature('主页面客户跟进列表')
def test_robot_crm_biz_list_148():
    query_params = {
        "access_token": mt.get_token(),
        "query": "",
        "org_code": "",
        "page": 1,
        "pageSize": 10,
        "orderBy": ""

    }
    r = requests.get(url=mt.data_url + "/v1/robot/crm/biz_list", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('主页面客户跟进搜索')
def test_robot_biz_list_149():
    query_params = {
        "access_token": mt.get_token(),
        "query": "建行",
        "org_code": "",
        "page": 1,
        "pageSize": 10,
        "orderBy": ""

    }
    r = requests.get(url=mt.data_url + "/v1/robot/crm/biz_list", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('场景内客户列表展示')
def test_robot_crm_list_150():
    query_params ={
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize": 10,
        "orderBy": "alloc_time desc",
        "biz_id" : mt.test_need_flow()
    }
    r = requests.get(url=mt.data_url+"/v1/robot/crm/list",params=query_params)
    print(r.json())
    with check:
        assert r.status_code ==200
        assert r.json()['code'] ==20000


@allure.story('直营银行-短信发送')
def test_send_shortmsg_151():
    query_params = {
        "access_token" : mt.get_token(),
        "receiver" : 16657121119,
        "content" : "【摸象科技】这是一条实时发送短信，内容承接电话外呼。"
    }
    r = requests.get(url=mt.data_url+"/v1/send/shortmsg" ,params =query_params)
    print(r.json)
    with check:
        assert r.status_code == 200
        assert r.json() ['code'] == 20000



@allure.story('客户属性列表')
def test_customer_attr_list_152():
    query_params = {
        "access_token": mt.get_token(),

    }
    r =requests.get(url=mt.data_url+"/v1/robot/crm/customer_attr_list" ,params=query_params)
    print(r.json)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000


@allure.story('客户详情')
def test_contact_log_list_153():
    query_params = {
        "access_token": mt.get_token(),
        "page" : 1,
        "pageSize":10,
        "orderBy": "cont_time desc",
        "mobile" : "",
        "crm_cont_id" : mt.test_robot_crm_list()['cont_id'],
        "biz_name" : mt.test_robot_crm_list()['busin_name']
    }
    r = requests.get(url= mt.data_url + "/v1/robot/crm/contact_log_list" , params = query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000






