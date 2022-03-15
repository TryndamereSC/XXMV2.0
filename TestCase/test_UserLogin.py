# !/usr/bin python3                                 
# encoding   :   utf-8 -*-                            
# author     :   浮川                              
# File       :   Test_topic.py
# Date       :   2021/6/2 15:18

import requests
import json
import pytest
import os
import allure
from pytest_check import check
from Business.common import MyTools


mt = MyTools()

@allure.feature('登录')
def test_uesrLogin_01():
    """用户登录"""
    data_url = mt.data_url
    UserAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    query_params = {
        "client_id":"ROBOT",
        "client_secret":"1",
        "grant_type":"password",
        "remember":"1",
        "username": mt.username,
        "password":mt.password
    }
    r = requests.post(data_url+"/oauth/token/getAccessToken",data = query_params)

    print(r.json())
    with check:
        assert r.status_code == 200



@allure.story('密码为空')
def test_uesrLogin_02():
    """用户登录-密码为空"""
    data_url = mt.data_url
    UserAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    query_params = {
        "client_id":"ROBOT",
        "client_secret":"1",
        "grant_type":"password",
        "remember":"1",
        "username": mt.username,
        "password":""

    }
    r = requests.post(data_url+"/oauth/token/getAccessToken",data = query_params)

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['message'] == '密码错误'



@allure.story('账户为空')
def test_uesrLogin_03():
    """用户登录-用户为空"""
    data_url = mt.data_url
    UserAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    query_params = {
        "client_id":"ROBOT",
        "client_secret":"1",
        "grant_type":"password",
        "remember":"1",
        "username": "",
        "password":mt.password

    }
    r = requests.post(data_url+"/oauth/token/getAccessToken",data = query_params)

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['message'] == '用户不存在'



@allure.story('密码账号都为空')
def test_uesrLogin_04():
    """用户登录-用户账号密码为空"""
    data_url = mt.data_url
    UserAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    query_params = {
        "client_id":"ROBOT",
        "client_secret":"1",
        "grant_type":"password",
        "remember":"1",
        "password": "5522f9375743e21e363aa4588d437a8653e7f053"

    }
    r = requests.post(data_url+"/oauth/token/getAccessToken",data = query_params)

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['message'] == '用户不存在'
