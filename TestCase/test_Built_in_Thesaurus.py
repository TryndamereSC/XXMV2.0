# !/usr/bin python3                                 
# encoding   :   utf-8 -*-                            
# author     :   浮川                              
# File       :   Test_Built in Thesaurus.py
# Date       :   2021/9/7 16:13


import requests
import time
from datetime import datetime
import json
import uuid
import allure
import pytest
from pytest_check import check
from Business.common import MyTools


time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
time_stamp1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time_stamp2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))


mt = MyTools()

@allure.feature('内置词库-词库标签列表')
def test_tag_81():

    query_params = {
       "access_token" : mt.get_token(),
        "type" : 1
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/list/tag",params=query_params)
    print(r.json())
    with check:
        assert r.status_code ==200
        assert r.json()['code'] ==20000




@allure.story('内置词库-通用词库-词库列表')
def test_entry_bank_list_82():

    query_params = {
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "time_modified desc",
        "type" : 1,
        "source" :1
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/entry_bank/list",params=query_params)
    print(r.json())
    with check:
        assert r.status_code ==200
        assert r.json()['code'] == 20000


@allure.story('内置词库-通用词库-词条管理')
def test_entry_list_83():

    query_params = {
        "access_token" : mt.get_token(),
        "bank_id" : mt.test_entry_bank_list()['bank_id'],
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "time_modified desc"
    }
    r = requests.get(url=mt.data_url + "/v1/nlu/entry/list", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('内置词库-新增词条')
def test_entry_add_84():

    query_params = {
        "entry_bank_id" : mt.test_entry_bank_list()['bank_id'],
        "access_token" : mt.get_token()
    }
    # print("bank_id", mt.test_entry_bank_list()['bank_id'])
    JsonDic =[{"standard_value": "测试", "raw_value": "测试", "status": 1,"edit" : "true","key" : 0
              }]
    r = requests.post(url=mt.data_url+"/v1/nlu/entry/add",params = query_params,data=json.dumps(JsonDic))
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('内置词库-通用词库-发布通用资源包')
def test_release_gen_90():

    query_params = {
        "access_token" : mt.get_token()
    }
    r = requests.post(url=mt.data_url+"/v1/voicerobot/robot/release_gen",data=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('内置词库-行业词库-词库标签列表')
def test_tag_91():

    query_params = {
       "access_token" : mt.get_token(),
        "type" : 2
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/list/tag",params=query_params)
    print(r.json())
    with check:
        assert r.status_code ==200
        # assert r.json()['code'] ==20000



@allure.story('内置词库-行业词库-词库列表')
def test_entry_bank_list_92():

    query_params = {
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "time_modified desc",
        "type" : 2,
        "source" :1
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/entry_bank/list",params=query_params)
    print(r.json())
    with check:
        assert r.status_code ==200
        # assert r.json()['code'] == 20000  #词库列表没有数据



@allure.story('内置词库-行业词库-新增词条')
def test_entry_add_93():

    query_params = {
        "access_token" : mt.get_token()
    }

    JsonDic = {"source": 1, "type": 2, "industry": 1, "name": "测试", "tag": "催收"}
    r = requests.post(url=mt.data_url+"/v1/nlu/entry/add",params = query_params,data=json.dumps(JsonDic))
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('内置词库-行业词库-词条管理')
def test_entry_list_94():

    query_params = {
        "access_token" : mt.get_token(),
        "bank_id" : mt.test_entry_bank_list()['bank_id'],
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "time_modified desc"
    }
    r = requests.get(url=mt.data_url + "/v1/nlu/entry/list", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('内置词库-行业词库-编辑')
def test_update_95():

    query_params = {
        "access_token" : mt.get_token()
    }
    JsonDic = {"source" :1, "type": 2, "name": "测试", "tag": "催收","industry": 1,"id": 1603}
    r = requests.post(url=mt.data_url+"/v1/nlu/entry_bank/update",params=query_params,data=json.dumps(JsonDic))
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('内置词库-行业词库-词条管理')
def test_entry_list_96():

    query_params = {
        "access_token" : mt.get_token(),
        "bank_id": mt.test_entry_bank_list()['bank_id'],
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "time_modified desc"
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/entry/list",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('内置意图-意图标签列表')
def test_intention_list_tag_97():

    query_params ={
        "access_token" : mt.get_token(),
        "type" : 1
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/intention/list/tag",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('内置意图-通用意图列表')
def test_intention_list_98():

    query_params = {
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "time_modifed desc",
        "type" : 1,
        "source" :1
    }
    r = requests.get(url=mt.data_url + "/v1/nlu/intention/list", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('内置意图-通用意图-新增意图')
def test_intention_add_99():

    query_params ={
        "access_token" : mt.get_token()
    }
    JsonDic = {"source": 1, "type": 1, "name": "测试", "default_answer": "测试", "tag": "测试"}
    r = requests.post(url=mt.data_url+"/v1/nlu/intention/add",params =query_params,data=json.dumps(JsonDic))
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000  #意图不能重复添加




#@allure.story('内置意图-通用意图-新增pattern语料')
# def test_pattern_save_100():
#     """内置意图-通用意图-新增pattern语料"""
#     query_params = {
#         "intention_id" : 58696,
#         "access_token" : mt.get_token()
#     }
#     JsonDic = {"bindings": [], "patterns": []}
#     r = requests.post(url=mt.data_url+"/v1/nlu/intention/pattern/save",params = query_params ,data=json.dumps(JsonDic))
#     print(r.json())
#     with check:
#         assert r.status_code == 200
#         assert r.json()['code'] == 20000
#


@allure.story('内置意图-导出意图Excel')
def test_export_com_excel_101():

    query_params = {
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/intention/export_com_excel",params=query_params)
    print(r.text)
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   # 文件导出



@allure.story('内置意图——通用意图-导出语义包')
def test_export_com_nlu_102():

    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/voicerobot/robot/export_com_nlu", params=query_params)
    print(r.text)
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   # 文件导出



@allure.story('知识管理-知识仓库 -QA仓库列表')
def test_intention_list_103():

    query_params = {
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "time_modifed desc",
        "type" : 1,
        "source" :  3
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/intention/list",params=query_params)
    print(r.json())
    with check:
        assert r.json()['code'] == 20000
        assert r.status_code == 200



@allure.story('知识管理-知识仓库-语态仓库列表')
def test_intention_list_104():

    query_params = {
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "time_modifed desc",
        "type" : 3,
        "source" :  3
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/intention/list",params=query_params)
    print(r.json())
    with check:
        assert r.json()['code'] == 20000
        assert r.status_code == 200



@allure.story('识仓库-QA仓库-新增意图')
def test_intention_add_105():

    query_params ={
        "access_token" : mt.get_token()
    }
    JsonDic = {"source": 3, "type": 1, "name": "测试", "default_answer": "脚本测试", "tag": "测试"}
    r = requests.post(url=mt.data_url+"/v1/nlu/intention/add",params =query_params,data=json.dumps(JsonDic))
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('知识仓库-QA仓库-编辑保存')
def test_intention_update_106():

    query_params = {
        "access_token" : mt.get_token()
    }
    JsonDic = {"source": 3, "type": 1, "name": "测试", "default_answer": "脚本测试1", "tag": "测试", "id": mt.test_intention_list()['QA_list_id']}
    r= requests.post(url=mt.data_url+"/v1/nlu/intention/update",params = query_params,data=json.dumps(JsonDic))
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('知识仓库-QA列表-删除新增意图')
def test_intention_status_107():

    query_params = {
        "access_token" : mt.get_token(),
        "id" : mt.test_intention_list()['QA_list_id'],
        "status" : -1
    }
    r = requests.post(url=mt.data_url+"/v1/nlu/intention/status",data=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('知识仓库-QA列表-语态管理-pattern语料')
def test_pattern_list_108():

    query_params = {

        "robot_id" : "",
        "orderBy" : "time_modifed desc",
        "int_id" : mt.test_intention_list_103()['int_id'],
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/nlu/intention/pattern/list", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('知识仓库-QA仓库-pattern语料管理-批量添加保存')
def test_pattern_save_109():

    query_params = {
        "intention_id" : mt.test_intention_list_103()['int_id'],
        "access_token" : mt.get_token()
    }
    JsonDic = {"bindings": [], "patterns": []}
    r= requests.post(url=mt.data_url+"/v1/nlu/intention/pattern/save",params = query_params,data=json.dumps(JsonDic))
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('知识仓库-QA仓库-语料管理-语义槽列表')
def test_entry_bank_binding_list_110():

    query_params ={
         "access_token" : mt.get_token(),
        "robot_id" : "",
        "orderBy" : "time_modifed desc",
        "int_id" : mt.test_intention_list_103()['int_id']
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/intention/entry_bank_binding/list",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000 #语义槽为空


@pytest.mark.run(order =1)
@allure.story('知识仓库-语态仓库-新增意图保存')
def test_intention_add_111():

    query_params = {
       "access_token" : mt.get_token()

    }
    JsonDic = {"source": 3, "type": 3, "name": "狂风绝息斩", "default_answer": "测试脚本", "intention_attr": 2, "tag": ""}
    r= requests.post(url=mt.data_url+"/v1/nlu/intention/add",params = query_params,data=json.dumps(JsonDic))
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@pytest.mark.run(order =2)
@allure.story('知识仓库-语态仓库-意图编辑保存')
def test_intention_update_112():

    query_params = {
        "access_token" : mt.get_token()
    }
    JsonDic = {"source": 3, "type": 3, "name": "狂风绝息斩", "default_answer": "测试脚本", "intention_attr": 2, "tag": "null", "id": mt.test_intention_list_104()['intention_id']}
    r = requests.post(url=mt.data_url + "/v1/nlu/intention/update", params=query_params, data=json.dumps(JsonDic))
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@pytest.mark.run(order =3)
@allure.story('知识仓库-语态仓库-新增意图删除')
def test_intention_status_113():

    query_params = {
        "access_token" : mt.get_token(),
        "id" : mt.test_intention_list_104()['intention_id'],
        "status" : "-1"
    }
    r = requests.post(url=mt.data_url+"/v1/nlu/intention/status",params = query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000
