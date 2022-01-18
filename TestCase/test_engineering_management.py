# !/usr/bin python3                                 
# encoding   :   utf-8 -*-                            
# author     :   浮川                              
# File       :   Test_engineering management.py
# Date       :   2021/10/18 18:23
import order
import requests
import pytest
import time
from datetime import datetime, timedelta
import json
import allure
import uuid
from pytest_check import check
from Business.common import MyTools


# time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# time_stamp1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# time_stamp2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))


mt = MyTools()


@allure.feature("""工程管理-设备管理列表""")
def test_getVoiceDeviceList_128():

    query_params ={
        "access_token" : mt.get_token(),
        "order" :"-id",
        "offset" : 1,
        "limit" : 10,
        "account_ids" : "",
        "org_code" : ""
    }
    r = requests.get(url=mt.data_url+"/v1/oper/device/getVoiceDeviceList",params=query_params)

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000


@pytest.mark.run(order=1)
@allure.story('设备管理-创建设备')
def test_addVoiceDevice_129():

    query_params = {
        "access_token" : mt.get_token()
    }
    JsonDic = {"accountId" : mt.test_org_list()['account_ids'],"bankOrgCodes" : mt.test_org_list()['bank_code'],"deviceCode" :"9527","deviceName" :"测试设备——勿删！！！！",
               "deviceType" : 1,"freeswitchId" : 9527,"ip" : "192.168.181.227","portNum" : "9527","relBankOrgCodes" :mt.test_org_list()['bank_code'],
               "switchMachineIp" : "127.0.0.1"
               }
    r= requests.post(url=mt.data_url+"/v1/oper/device/addVoiceDevice",params = query_params,data=json.dumps(JsonDic))

    print(r.json())
    print(mt.test_org_list()['bank_code'])
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000


@allure.story('设备管理-操作-编辑设备')
@pytest.mark.run(order=2)
def test_addVoiceDevice_130():

    query_params = {
        "access_token" : mt.get_token()
    }
    JsonDic = {"accountId" : 213,"bankOrgCodes" : mt.test_org_list()['bank_code'],"deviceCode" :"9527","deviceName" :"测试设备——勿删！！！！",
               "deviceType" : 1,"freeswitchId" : "921ed526-3264-4c87-9058-92404fa16dc6","id" : mt.test_getVoiceDeviceList_128()['equipment_id'],"ip" : "192.168.181.227","portNum" : "9527","relBankOrgCodes" :mt.test_org_list()['bank_code'],
               "switchMachineIp" : "127.0.0.1"
               }
    r= requests.put(url=mt.data_url+"/v1/oper/device/updateVoiceDevice/"+str(mt.test_getVoiceDeviceList_128()['equipment_id']),params = query_params,data=json.dumps(JsonDic))

    print(r.json())
    print( mt.test_org_list()['bank_code'])
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000


@allure.story('工程管理-设备管理-操作-状态off')
def test_updateVoiceDeviceStatusById_id_131():

    query_params = {
        "access_token" : mt.get_token(),
        "status" : 0
    }
    r = requests.get(url=mt.data_url+"/v1/oper/device/updateVoiceDeviceStatusById/"+str(mt.test_getVoiceDeviceList_128()['equipment_id']),params=query_params)

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('设备管理-操作-卡口配置列表')
def test_getCardSlotList_132():

    query_params = {
        "access_token" : mt.get_token(),
        "device_id" : mt.test_getVoiceDeviceList_128()['equipment_id'],
        "order" : "+code",
        "offset" : 1,
        "limit" : 16
    }
    r = requests.get(url=mt.data_url+"/v1/oper/device/getCardSlotList",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000   新建设备没有卡口



@allure.story('工程管理-设备管理-操作-卡口配置-新增卡口-区分外呼地区')
def test_addCardSlots_133():

    query_params = {
        "access_token" : mt.get_token()
    }
    JsonDic = {"cityStatus": 1," code": "0571", "cardNum": 1, "gangyinStatus": 1, "fanjiStatus": 1, "dialInterval": 15,"city":"云南-楚雄",
               "deviceCode" : mt.test_getVoiceDeviceList_128()['Device_Code'],"code" : "110"
               }
    r = requests.post(url=mt.data_url+"/v1/oper/device/addCardSlots",params = query_params,data=json.dumps(JsonDic))

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('程管理-设备管理-操作-卡口配置-新增卡口-不区分外呼地区')
def test_addCardSlots_134():

    query_params = {
        "access_token" : mt.get_token()
    }
    JsonDic = {"cityStatus": 0, "cardNum": 1, "gangyinStatus": 1, "fanjiStatus": 1, "dialInterval": 15,
               "deviceCode" : mt.test_getVoiceDeviceList_128()['Device_Code'],"code" : "120"
               }
    r = requests.post(url=mt.data_url+"/v1/oper/device/addCardSlots",params = query_params,data=json.dumps(JsonDic))

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('程管理-设备管理-操作-卡口配置-新增卡口-打开巡检配置')
def test_getPhoneLineCheckSetting_135():

    query_params = {
        "access_token": mt.get_token()
    }
    r = requests.get(
        url=mt.data_url + "/v1/oper/device/getPhoneLineCheckSetting/" + str(mt.test_getCardSlotList_132()['Bayone_id']),
        params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20003




@allure.story('工程管理-设备管理-操作-卡口配置-新增卡口-打开巡检配置-巡检配置-【配置/编辑保存】')
def test_updatePhoneLineCheckSetting_136():

    query_params = {
        "access_token": mt.get_token()
    }
    JsonDic = [{"phone": "16657121119", "time": "17:17:16"}]
    r = requests.post(url=mt.data_url + "/v1/oper/device/updatePhoneLineCheckSetting/" + str(mt.test_getCardSlotList_132()['Bayone_id']),
                      params = query_params,data=json.dumps(JsonDic))

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('工程管理-设备管理-操作-卡口配置-新增卡口-删除卡口')
def test_delCardSlot_137():

    query_params = {
        "access_token" : mt.get_token(),
        "card_ids" : mt.test_getCardSlotList_132()['Bayone_id']
    }
    r = requests.get(url=mt.data_url+"/v1/oper/device/delCardSlot",params=query_params)

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('工程管理-设备管理-操作-状态ON')
def test_updateVoiceDeviceStatusById_id_138():

    query_params = {
        "access_token" : mt.get_token(),
        "status" : 1
    }
    r = requests.get(url=mt.data_url+"/v1/oper/device/updateVoiceDeviceStatusById/"+str(mt.test_getVoiceDeviceList_128()['equipment_id']),params=query_params)

    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('设备管理-删除设备')
def test_deleteVoiceDevice_139():

    query_params ={
        "access_token" : mt.get_token()
    }
    r = requests.delete(url=mt.data_url+"/v1/oper/device/deleteVoiceDevice/"+str(mt.test_getVoiceDeviceList_128()['equipment_id']),params = query_params)
    print(r.json())
    print(r.url)
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('音服务设置-阿里公有云*2')
def test_set_asr_tts_global_140():

    query_params = {
        "access_token" : mt.get_token(),
        "asr_type" : 7,
        "tts_type" : 7
    }
    r = requests.post(url=mt.data_url+"/v1/oper/set_asr_tts_global",data=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语音服务设置-思必驰私有云*2')
def test_set_asr_tts_global_141():

    query_params = {
        "access_token" : mt.get_token(),
        "asr_type" : 8,
        "tts_type" : 8
    }
    r = requests.post(url=mt.data_url+"/v1/oper/set_asr_tts_global",data=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语音服务设置-思必驰私有云and阿里公有云')
def test_set_asr_tts_global_142():

    query_params = {
        "access_token" : mt.get_token(),
        "asr_type" : 8,
        "tts_type" : 7
    }
    r = requests.post(url=mt.data_url+"/v1/oper/set_asr_tts_global",data=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语音服务设置-阿里公有云and思必驰私有云')
def test_set_asr_tts_global_143():

    query_params = {
        "access_token" : mt.get_token(),
        "asr_type" : 7,
        "tts_type" : 8
    }
    r = requests.post(url=mt.data_url+"/v1/oper/set_asr_tts_global",data=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('语音服务设置-阿里公有云*2')
def test_set_asr_tts_global_144():

    query_params = {
        "access_token" : mt.get_token(),
        "asr_type" : 7,
        "tts_type" : 7
    }
    r = requests.post(url=mt.data_url+"/v1/oper/set_asr_tts_global",data=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('防骚扰策略列表')
def test_call_rule_list_145():

    query_params = {
        "access_token" : mt.get_token()
    }
    r= requests.get(url=mt.data_url+"/v1/robot/call_rule/list",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('防骚扰策略-ON')
def test_call_rule_save_146():

    query_params = {
        "access_token": mt.get_token()
    }
    JsonDic = [{"period_time": "P1M", "times": 50001, "status": 1, "type": 0}]
    r = requests.post(url=mt.data_url + "/v1/robot/call_rule/save", params=query_params, data=json.dumps(JsonDic))
    print(r.url)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('防骚扰策略-OFF')
def test_call_rule_save_147():

    query_params = {
        "access_token": mt.get_token()
    }
    JsonDic = [{"period_time": "P1M", "times": 50001, "status": 0, "type": 0}]
    r = requests.post(url=mt.data_url + "/v1/robot/call_rule/save", params=query_params, data=json.dumps(JsonDic))
    print(r.url)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000










