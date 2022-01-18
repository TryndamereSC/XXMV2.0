# !/usr/bin python3                                 
# encoding   :   utf-8 -*-                            
# author     :   浮川                              
# File       :   Test Scene template.py
# Date       :   2021/8/27 10:44
import allure
import requests
import time
import json
from pytest_check import check
from Business.common import MyTools

time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
time_stamp1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time_stamp2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

mt = MyTools()
@allure.feature('获取场景模板列表-全部')
def test_findRobotList_90():

    query_params = {
        "access_token" : mt.get_token(),
        "offset" : 1,
        "limit" : 15,
        "order" : "",
        "biz_robot_type": ""
    }
    r = requests.get(url=mt.data_url + "/v1/voicerobot/robot/findRobotList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000


@allure.story('获取场景模板列表-短信')
def test_findRobotList_91():

    query_params = {
        "access_token" : mt.get_token(),
        "offset" : 1,
        "limit" : 15,
        "order" : "",
        "robot_label" : "",
        "biz_follow_type" : 1,
        "robot_name" : "",
        "biz_robot_type": ""
    }
    r = requests.get(url=mt.data_url + "/v1/voicerobot/robot/findRobotList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取场景模板列表-人工跟进')
def test_findRobotList_92():

    query_params = {
        "access_token" : mt.get_token(),
        "offset" : 1,
        "limit" : 15,
        "order" : "",
        "robot_label" : "",
        "biz_follow_type" : 2,
        "robot_name" : "",
        "biz_robot_type": ""
    }
    r = requests.get(url=mt.data_url + "/v1/voicerobot/robot/findRobotList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取场景模板列表-短信+人工跟进')
def test_findRobotList_93():

    query_params = {
        "access_token" : mt.get_token(),
        "offset" : 1,
        "limit" : 15,
        "order" : "",
        "robot_label" : "",
        "biz_follow_type" : 3,
        "robot_name" : "",
        "biz_robot_type": ""
    }
    r = requests.get(url=mt.data_url + "/v1/voicerobot/robot/findRobotList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('获取场景模板列表-短信')
def test_findRobotList_94():

    query_params = {
        "access_token" : mt.get_token(),
        "offset" : 1,
        "limit" : 15,
        "order" : "",
        "robot_label" : "",
        "biz_follow_type" : 1,
        "robot_name" : "",
        "biz_robot_type": ""
    }
    r = requests.get(url=mt.data_url + "/v1/voicerobot/robot/findRobotList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('模板检测')
def test_verifyRobotIntegrality_robotId_95():

    query_params = {
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url+"/v1/voicerobot/robot/verifyRobotIntegrality/"+str(mt.findRobotList()['robotID']),params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('场景模板-复制模板')
def test_copyRobotTemplate_96():

    query_params = {
        "access_token" : mt.get_token()
    }
    jsonDic = {"copy_robot_id": 1283, "robot_name": "test", "create_user_id": 1}
    r = requests.post(url=mt.data_url+"/v1/voicerobot/robot/copyRobotTemplate",params = query_params,data=json.dumps(jsonDic))
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story(' 场景模板-模板编辑-获取场景类型标签')
def test_getRobotLabels_97():

    query_params = {
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url+"/v1/voicerobot/robot/getRobotLabels",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000




















