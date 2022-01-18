# !/usr/bin python3                                 
# encoding   :   utf-8 -*-                            
# author     :   浮川                              
# File       :   Test_Scene management.py
# Date       :   2021/6/21 18:51

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


@allure.feature('获取异常场景')
def test_get_disable_business_13():

    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/oper/get_disable_business", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('机构列表')
def test_list_14():

    query_params = {
        "access_token": mt.get_token(),
        "query": "",
        "is_manage": "0",
        "is_check_biz": "1"

    }
    r = requests.get(url=mt.data_url + "/v1/bank/org/list", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('场景列表')
def test_businesses_15():

    query_params = {
        "access_token": mt.get_token(),
        "business_type": "2"
    }
    r = requests.get(url=mt.data_url + "/v1/oper/businesses", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('场景搜索')
def test_businesse_16():

    query_params = {
        "access_token": mt.get_token(),
        "page": 1,
        "pageSize": 10,
        "orderBy": "time_create desc",
        "query": "",
        "business_type": "",
        "biz_robot_type": "",
        "org_code": "",
        "parent_robot_id": ""
    }
    r = requests.get(url=mt.data_url + "/v1/oper/businesses", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('话术完整性检查"')
def test_robot_id_17():

    query_params = {
        "access_token" : mt.get_token()
    }
    r = requests.get(url= mt.data_url+"/v1/voicerobot/robot/verifyRobotIntegrality/"+str(mt.get_robot_dict()["robot_id"]),params= query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取场景作业状态')
def test_get_biz_state_18():

    query_params = {
        "access_token": mt.get_token(),
        "biz_uni_key": mt.get_robot_dict()['biz_uni_key'],
        "is_sync": 0
    }
    r = requests.get(url=mt.data_url + "/v1/robot/sync_data/get_biz_state", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('批次详情')
def test_batch_data_19():

    query_params = {
        "access_token": mt.get_token(),
        "biz_uni_key": mt.get_robot_dict()['biz_uni_key'],
        "is_sync" : 1,
        "page" : 1,
        "pageSize" : 10
    }
    r = requests.get(url= mt.data_url+"/v1/robot/sync_data/batch_data",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('卡口详情')
def test_card_data_20():

    query_params = {
        "access_token": mt.get_token(),
        "biz_uni_key": mt.get_robot_dict()['biz_uni_key'],
        "is_sync": 1,
        "page": 1,
        "pageSize": 10
    }
    r = requests.get(url=mt.data_url + "/v1/robot/sync_data/card_data", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   #无卡口数据


@allure.story('拨打数据回流-场景列表')
def test_businesses_flow_21():

    query_params = {
        "access_token": mt.get_token(),
        "business_type": "2"
    }
    r = requests.get(url=mt.data_url + "/v1/oper/businesses", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取该场景下的用户分类')
def test_getClassifyOpt_22():

    query_params = {
        "bizId" : mt.get_robot_dict()['bizId'],
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/robot/report/getClassifyOpt", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('查找分类')
def test_get_result_23():

    query_params = {
        "biz_uni_key": mt.get_robot_dict()['biz_uni_key'],
        "access_token": mt.get_token(),
        "with_default" : 1
    }
    r = requests.get(url=mt.data_url + "/v1/robot/robot_result_status/get_result", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('批次详情')
def test_batch_data_24():

    query_params = {
        "biz_uni_key": mt.get_robot_dict()['biz_uni_key'],
        "access_token": mt.get_token(),
        "is_sync" : 0,
        "page" : 1,
        "pageSize" : 10
    }
    r = requests.get(url=mt.data_url + "/v1/robot/sync_data/batch_data", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000


@allure.story('场景报表')
def test_itemId_25():

    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/oper/business/"+str(mt.get_robot_dict()['bizId']), params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000


@allure.story('场景开关状态-关闭')
def test_OFF_26():

    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.put(url=mt.data_url + "/v1/oper/business/" +str(mt.get_robot_dict()['bizId'])+ "/0",
                     data=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('场景开关状态-开启')
def test_ON_27():

    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.put(url=mt.data_url + "/v1/oper/business/" +str(mt.get_robot_dict()['bizId'])+ "/1",
                     data=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('话术测试--【重新开始对话】')
def test_start_28():

    query_params = {
        "access_token": mt.get_token(),
        "sessionId": mt.sessionId,
        "robotId": mt.get_robot_dict()['robotId'],
    }
    r = requests.get(url=mt.data_url + "/v1/dm/test/start", params=query_params)
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



#@allure.story('话术测试')
# def test_input_29():

#     query_params = {
#         "access_token": mt.get_token(),
#         "sessionId" : mt.sessionId,
#         "robotId" : mt.get_robot_dict()['robotId'],
#         "input" : "你好",
#         "bizUniKey" : mt.get_robot_dict()['biz_uni_key']
#     }
#     r = requests.get(url=mt.data_url + "/v1/dm/test/input", params=query_params)
#     print(r.json())
#     print(r.url)
#     with check:
# 	      assert r.status_code == 200
# 	      assert r.json()['code'] == 20000
#


@allure.story('话术测试--【结束对话】')
def test_end_30():

    query_params = {
        "access_token": mt.get_token(),
        "sessionId": mt.sessionId,
        "robotId": mt.get_robot_dict()['robotId'],
        "bizUniKey": mt.get_robot_dict()['biz_uni_key']
    }
    r = requests.get(url=mt.data_url + "/v1/dm/test/end", params=query_params)
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



#@allure.story('计费设置-不计费')
# def test_save_biz_data_31():
#
#     query_params = {
#         "access_token": mt.get_token()
#     }
#
#     jsonDic = {"online_time": time_stamp1, "fee_type": 0, "id": mt.get_robot_dict()['bizId'], "fee_time_begin": "", "fee_time_end": ""}
#
#     r = requests.post(url=mt.data_url + "/v1/oper/save_biz_data", params=query_params, data=json.dumps(jsonDic))
#     # r = requests.post(url= mt.data_url + "/v1/oper/save_biz_data",data=query_params,json={"online_time": time_stamp1, "fee_type": 0, id: 803, "fee_time_begin": "null", "fee_time_end": "null"})
#     print(r.json())
#     print(r.url)
#     with check:
# 	      assert r.status_code == 200
# 	      assert r.json()['code'] == 20000
#


@allure.story('计费设置-有效时间')
# def test_save_biz_data_32():
#
#     query_params = {
#         "access_token": mt.get_token()
#     }
#
#     jsonDic = {"online_time": time_stamp1, "fee_type": 1, "id": mt.get_robot_dict()['bizId'], "fee_time_begin": time_stamp1,
#                "fee_time_end": time_stamp1}
#
#     r = requests.post(url=mt.data_url + "/v1/oper/save_biz_data", params=query_params, data=json.dumps(jsonDic))
#     # r = requests.post(url= mt.data_url + "/v1/oper/save_biz_data",data=query_params,json={"online_time": time_stamp1, "fee_type": 0, id: 803, "fee_time_begin": "null", "fee_time_end": "null"})
#     print(r.json())
#     print(r.url)
#     with check:
# 	      assert r.status_code == 200
# 	      assert r.json()['code'] == 20000
#

#
#@allure.story('计费设置-接通次数')
# def test_save_biz_data_33():
#
#     query_params = {
#         "access_token": mt.get_token()
#     }
#
#     jsonDic = {"online_time": time_stamp1, "fee_type": 2, "id": mt.get_robot_dict()['bizId'], "fee_time_begin": "",
#                "fee_time_end": "","fee_times": 10000}
#
#     r = requests.post(url=mt.data_url + "/v1/oper/save_biz_data", params=query_params, data=json.dumps(jsonDic))
#     # r = requests.post(url= mt.data_url + "/v1/oper/save_biz_data",data=query_params,json={"online_time": time_stamp1, "fee_type": 0, id: 803, "fee_time_begin": "null", "fee_time_end": "null"})
#     print(r.json())
#     with check:
# 	      assert r.status_code == 200
#  	      assert r.json()['code'] == 20000
#


@allure.story('场景导出')
def test_export_biz_34():

    query_params = {
        "biz_id": mt.get_robot_dict()['bizId'],
        "access_token": mt.get_token()
    }

    r = requests.get(url=mt.data_url + "/v1/oper/export_biz", params=query_params)
    with open("python.zip", "wb") as pyth:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pyth.write(chunk)
    print(r.text)
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000 #导出场景无code码返回




@allure.story('添加外呼任务')
def test_getDataSourceBatchList_35():

    query_params = {
        "access_token": mt.get_token(),
        "pageSize" : 10,
        "page" : 1,
        "orderBy" : "time_create desc",
        "business_id" : mt.get_robot_dict()['bizId']
    }
    r = requests.get(url=mt.data_url + "/v1/oper/datasource/getDataSourceBatchList",params=query_params)
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('场景快照-场景概括')
def test_batch_data_36():

    query_params = {
        "access_token": mt.get_token(),
        "biz_uni_key": mt.get_robot_dict()['biz_uni_key'],
        "is_sync" : 0,
        "page" : 1,
        "pageSize" : 10
    }
    r = requests.get(url= mt.data_url+"/v1/robot/sync_data/batch_data",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('场景接入')
def test_findRobotList_37():

    query_params = {
        "access_token" : mt.get_token(),
        "offset" : 1,
        "limit" : 15,
        "order" : ""
    }
    r = requests.get(url=mt.data_url +"/v1/voicerobot/robot/findRobotList",params= query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('场景详情')
def test_itemId_38():

    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/oper/business/"+str(mt.get_robot_dict()['bizId']), params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取场景流程')
def test_RobotId_39():

    query_params = {
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/robot/robotFlow/getRobotFlowByRobotId/" + str(mt.get_robot_dict()['robotId']),params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('场景-外呼详情列表-全部')
def test_getDataSourceBatchList_40():

    query_params = {
        "access_token": mt.get_token(),
        "pageSize": 10,
        "page": 1,
        "orderBy": "time_create desc",
        "business_id": mt.get_robot_dict()['bizId'],
        "is_join_call_plan" : 1
    }
    r = requests.get(url=mt.data_url + "/v1/oper/datasource/getDataSourceBatchList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取对话标签')
def test_getDialogLabels_41():

    query_params = {
        "access_token" : mt.get_token(),
        "robotId" : mt.get_robot_dict()['robotId']
    }
    r = requests.get(url=mt.data_url + "/v1/voicerobot/robot/getDialogLabels",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000 or 20003



@allure.story('场景-外呼详情列表-进行中')
def test_getDataSourceBatchList_42():

    query_params = {
        "access_token": mt.get_token(),
        "pageSize": 10,
        "page": 1,
        "orderBy": "time_create desc",
        "business_id": mt.get_robot_dict()['bizId'],
        "is_join_call_plan" : 1,
        "is_complete" : 0
    }
    r = requests.get(url=mt.data_url + "/v1/oper/datasource/getDataSourceBatchList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000  #外呼详情无数据



@allure.story('场景-外呼详情列表-已完成')
def test_getDataSourceBatchList_43():
    query_params = {
        "access_token": mt.get_token(),
        "pageSize": 10,
        "page": 1,
        "orderBy": "time_create desc",
        "business_id": mt.get_robot_dict()['bizId'],
        "is_join_call_plan" : 1,
        "is_complete" : 1
    }
    r = requests.get(url=mt.data_url + "/v1/oper/datasource/getDataSourceBatchList", params=query_params)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('场景-外呼详情列表-拨打详情')
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



@allure.story('全局防骚扰设置')
def test_call_rule_list_45():

    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url+"/v1/robot/call_rule/list",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取卡口列表')
def test_getCardSlotList_46():

    query_params = {
        "access_token": mt.get_token(),
        "org_code" : mt.getDataSourceBatchList()['data_source_batch_id'],
        "business_type" : 1,
        "status" : 1,
        "device_status" : 1
    }
    r = requests.get(url=mt.data_url+"/v1/oper/device/getCardSlotList",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000  #未配置线路无卡口



@allure.story('查找场景防骚扰规则')
def test_get_biz_rule_47():

    query_params ={
        "biz_id" : mt.get_robot_dict()['bizId'],
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url+"/v1/robot/call_rule/get_biz_rule",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   # 未配置防骚扰策略



@allure.story('获取场景跟进')
def test_get_biz_push_receiver_48():

    query_params = {
        "biz_id": mt.get_robot_dict()['bizId'],
        "access_token": mt.get_token(),
        "biz_push_type" : 1
    }
    r = requests.get(url=mt.data_url + "/v1/oper/get_biz_push_receiver", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   #该场景无跟进人员



@allure.story('场景列表')
def test_businesses_49():

    query_params = {
        "access_token": mt.get_token(),
        "org_code": ""
    }
    r = requests.get(url=mt.data_url + "/v1/oper/businesses", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('场景拨打设置--授权机构')
def test_biz_bank_orgs_50():

    query_params = {
        "biz_id": mt.get_robot_dict()['bizId'],
        "access_token": mt.get_token(),
    }
    r = requests.get(url=mt.data_url + "/v1/bank/biz_bank_orgs", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000  #拨打设置授权机构可能为空


@allure.story('基本信息配置-银行选择')
def test_account_51():

    query_params = {
        "is_manage" : 0,
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/uac/account", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('保存场景防骚扰规则')
def test_save_biz_rule_52():

    query_params = {
        "access_token" : mt.get_token()

    }
    jsonDic = {"biz_id": mt.get_robot_dict()['bizId'], "enable_global_call_rule": "true", "period_time": "P1D", "status": "1",
               "times": 1,"type" : 3}

    r = requests.post(url=mt.data_url + "/v1/robot/call_rule/save_biz_rule", params=query_params, data=json.dumps(jsonDic))
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('查找分类')
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
        assert r.json()['code'] == 20000



@allure.story('主话术流程-异常检测')
def test_verifyRobotFlow_robotId_54():

    query_params = {
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/robot/robotFlow/verifyRobotFlow/"+str(mt.get_robot_dict()['robotId']), params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取所有QA列表')
def test_getRobotQaList_55():

    query_params = {
        "access_token": mt.get_token(),
        "offset" : 1,
        "int_inner_type" : "",
        "limit" : 50,
        "order" : "-uid",
        "source" : "",
        "robotId" : mt.get_robot_dict()['robotId']
    }
    r = requests.get(url=mt.data_url + "/v1/robot/getRobotQaList", params=query_params)
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000


@allure.story('获取场景知识库--场景QA列表')

def test_getRobotQaList_56():

    query_params = {
        "access_token": mt.get_token(),
        "offset" : 1,
        "int_inner_type" : "",
        "limit" : 50,
        "order" : "-uid",
        "source" : 2,
        "robotId" : mt.get_robot_dict()['robotId']
    }
    r = requests.get(url=mt.data_url + "/v1/robot/getRobotQaList", params=query_params)
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000


@allure.story('获取场景知识库--通用QA列表')
def test_getRobotQaList_57():

    query_params = {
        "access_token": mt.get_token(),
        "offset" : 1,
        "int_inner_type" : "",
        "limit" : 50,
        "order" : "-uid",
        "source" : 1,
        "robotId" : mt.get_robot_dict()['robotId']
    }
    r = requests.get(url=mt.data_url + "/v1/robot/getRobotQaList", params=query_params)
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000


@allure.story('获取场景知识库--知识库QA列表')
def test_getRobotQaList_58():

    query_params = {
        "access_token": mt.get_token(),
        "offset" : 1,
        "int_inner_type" : "",
        "limit" : 50,
        "order" : "-uid",
        "source" : 3,
        "robotId" : mt.get_robot_dict()['robotId']
    }
    r = requests.get(url=mt.data_url + "/v1/robot/getRobotQaList", params=query_params)
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('场景知识库--兜底QA列表')
def test_getBasicConfig_robotId_59():

    query_params = {
        "access_token" : mt.get_token(),
        "robot_id" : mt.get_robot_dict()['robotId']
    }
    r = requests.get(url=mt.data_url+"/v1/robot/basicConfig/getBasicConfig/"+str(mt.get_robot_dict()['robotId']),params=query_params)
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取场景话术文本列表')
def test_getRobotSpeechTemp_60():

    query_params = {
        "access_token": mt.get_token(),
        "robotId": mt.get_robot_dict()['robotId'],
        "offset" : 1,
        "limit" : 10,
        # "order" : ""
    }
    r = requests.get(url=mt.data_url+"/v1/robotTemplate/getRobotSpeechTemp",params=query_params)
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('意图列表')
def test_intention_list_61():

    query_params = {
        "access_token" : mt.get_token(),
        "biz_use" : 1,
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "",
        "name" : ""
    }
    r = requests.get(url=mt.data_url+"/v1/nlu/intention/list",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('场景知识库导出')
def test_robotExportQAContentXls_robotId_62():

    query_params = {
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url+"/v1/robot/robotExportQAContentXls/"+str(mt.get_robot_dict()['robotId']),params=query_params)
    print(r.url)
    print(r.text)
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('获取话术文本变量')
def test_get_speech_content_var_63():
    query_params = {
        "access_token" : mt.get_token(),
        "robot_id" : mt.get_robot_dict()['robotId']
    }
    r = requests.get(url=mt.data_url+"/v1/robotTemplate/get_speech_content_var",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('TTS配置')
def test_get_tts_conf_64():

    query_params = {
        "access_token" : mt.get_token(),
        "robot_id" : mt.get_robot_dict()['robotId'],
        "tts_type" : 7
    }
    r = requests.get(url=mt.data_url+"/v1/oper/get_tts_conf",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取全局ASR和TTS资源配置')
def test_get_asr_tts_global_65():

    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/oper/get_asr_tts_global", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('场景语音--导出文本')
def test_robotTemplateExport_robot_id_66():

    query_params = {
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url + "/v1/robotTemplate/robotTemplateExport/"+str(mt.get_robot_dict()['robotId']), params=query_params)
    print(r.text)
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000



@allure.story('合成语音配置')
def test_set_tts_conf_67():

    query_params = {
        "access_token" : mt.get_token(),
        "robot_id" : mt.get_robot_dict()['robotId'],
        "voice" : "Aixia",
        "volume" : 50,
        "speech_rate" : 0,
        "ttsType" : 7,
        "pitch_rate" : 0,
        "tts_type" : 7
    }
    r = requests.get(url=mt.data_url + "/v1/oper/set_tts_conf", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语态设置-获取全部语态列表')
def test_getRobotBehaviourList_68():

    query_params = {
        "access_token" : mt.get_token(),
        "robotId" : mt.get_robot_dict()['robotId'],
        "offset" : 1,
        "limit" : 10,
        "order" : ""
    }
    r = requests.get(url=mt.data_url + "/v1/robot/behaviour/getRobotBehaviourList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语态设置-获取通用语态列表')
def test_getRobotBehaviourList_69():

    query_params = {
        "access_token" : mt.get_token(),
        "robotId" : mt.get_robot_dict()['robotId'],
        "offset" : 1,
        "limit" : 10,
        "order" : "",
        "source" : 1,
        "special_value" : 0
    }
    r = requests.get(url=mt.data_url + "/v1/robot/behaviour/getRobotBehaviourList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语态设置-获取知识库语态列表')
def test_getRobotBehaviourList_70():

    query_params = {
        "access_token": mt.get_token(),
        "robotId": mt.get_robot_dict()['robotId'],
        "offset": 1,
        "limit": 10,
        "order": "",
        "source": 3,
        "special_value": 0
    }
    r = requests.get(url=mt.data_url + "/v1/robot/behaviour/getRobotBehaviourList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语态设置-获取场景语态列表')
def test_getRobotBehaviourList_71():

    query_params = {
        "access_token": mt.get_token(),
        "robotId": mt.get_robot_dict()['robotId'],
        "offset": 1,
        "limit": 10,
        "order": "",
        "source": 2,
        "special_value": 0
    }
    r = requests.get(url=mt.data_url + "/v1/robot/behaviour/getRobotBehaviourList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   #无数据



@allure.story('语态设置-获取特殊语态列表')
def test_getRobotBehaviourList_72():

    query_params = {
        "access_token": mt.get_token(),
        "robotId": mt.get_robot_dict()['robotId'],
        "offset": 1,
        "limit": 10,
        "order": "",
        "special_value": 1
    }
    r = requests.get(url=mt.data_url + "/v1/robot/behaviour/getRobotBehaviourList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000  #无数据



@allure.story('语态设置-语态搜索')
def test_getRobotBehaviourList_73():

    query_params = {
        "access_token": mt.get_token(),
        "robotId": mt.get_robot_dict()['robotId'],
        "offset": 1,
        "limit": 10,
        "order": "",
        "special_value": 0,
        "toneAttitude" : ""
    }
    r = requests.get(url=mt.data_url + "/v1/robot/behaviour/getRobotBehaviourList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语态设置-重置')
def test_getRobotBehaviourList_74():

    query_params = {
        "access_token": mt.get_token(),
        "robotId": mt.get_robot_dict()['robotId'],
        "offset": 1,
        "limit": 10,
        "order": "",
        "special_value": 0,
        "toneAttitude" : ""
    }
    r = requests.get(url=mt.data_url + "/v1/robot/behaviour/getRobotBehaviourList", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语态设置-引用内置语态')
def test_intention_list_75():

    query_params = {
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "",
        "type" : 3,
        "source" : 1
    }
    r = requests.get(url=mt.data_url + "/v1/nlu/intention/list", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语态设置-引用知识库语态-QA仓库')
def test_intention_list_76():

    query_params = {
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "",
        "type" : 1,
        "source" : 3
    }
    r = requests.get(url=mt.data_url + "/v1/nlu/intention/list", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语态设置-引用知识库语态-语态仓库')
def test_intention_list_77():

    query_params = {
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "",
        "type" : 3,
        "source" : 3
    }
    r = requests.get(url=mt.data_url + "/v1/nlu/intention/list", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('用户分类-模板基础信息')
def test_getRobotInfo_robotId_78():

    query_params = {
        "robotId" : mt.get_robot_dict()['robotId'],
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url+"/v1/voicerobot/robot/getRobotInfo/"+str(mt.get_robot_dict()['robotId']),params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取意向规则名')
def test_get_intention_rule_79():

    query_params = {
        "robot_id": mt.get_robot_dict()['robotId'],
        "access_token": mt.get_token()
    }
    r = requests.get(url=mt.data_url+"/v1/robot/basicConfig/get_intention_rule",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('获取场景基础分类')
def test_get_biz_result_status_80():

    query_params = {
        "access_token" : mt.get_token(),
        "biz_robot_type" : 3
    }
    r = requests.get(url=mt.data_url + "/v1/robot/robot_result_status/get_biz_result_status", params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



