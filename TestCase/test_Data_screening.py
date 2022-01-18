# !/usr/bin python3                                 
# encoding   :   utf-8 -*-                            
# author     :   浮川                              
# File       :   Test_Data screening.py
# Date       :   2021/10/26 16:36

import requests
import time
import json
import allure
from pytest_check import check
from Business.common import MyTools

time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
time_stamp1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time_stamp2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

mt = MyTools()


@allure.feature('数据看板-拨打详情展示')
def test_report_findCallLogList_114():

    query_params = {
        "access_token" : mt.get_token(),
        "startTime" : mt.startTime('pure_num'),
        "endTime" : mt.endTime('pure_num'),
        "offset" : 1,
        "limit" : 10,
        "order" : "",
        "duration" : "",
        "callStatusList" : "",
        "comment" : "",
        "resultTypeName" : "",
        "human_status" : "",
        "robotId" : "",
        "outboundNumber" : "",
        "round_count" : "",
        "phone" : "",
        "result_status_desc" : "",
        "manual_result_status_desc" : "",
        "bank_org" : ""
    }
    for bid in mt.business_ids:
        query_params["businessId"] = bid
        r = requests.get(url=mt.data_url+"/v1/robot/report/findCallLogList", params=query_params)
        data = r.json()["data"]
        if data:
            break
    print(r.json()['data'][0]["business_name"])
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('拨打详情-获取枚举名称列表')
def test_common_enum_enum_115():

    query_params = {
        "enumName" : "biz_flow_status",
        "access_token" : mt.get_token()
    }
    r = requests.get(url=mt.data_url+"/v1/robot/open/common_enum/enum",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('拨打详情-获取导出场景拓展表头')
def test_get_business_extra_header_116():

    query_params = {
        "access_token" : mt.get_token()
    }
    for bid in mt.business_ids:
        query_params["bid"] = bid
        r = requests.get(url=mt.data_url+"/v1/oper/get_business_extra_header", params=query_params)
        data = r.json()["data"]
        if data:
            break

    print(bid)
    print(r.text)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000



@allure.story('拨打详情-Excel导出')
def test_export_excelList_117():

    query_params = {
        "access_token" : mt.get_token()
    }
    JsonDic = {"callStatusList" : "","comment" : "" ,"endTime" : mt.endTime(),"human_status": "","is_all" : 1,"limit" :10,
    "manual_result_status_desc" : "","offset": 1,"order" : "","outboundNumber" : "","phone" :"","resultTypeName" : "",
    "result_id" : "null","result_ids" : "","result_status_desc" : "","robotId" : "","round_count" : "",
    "scheme" : "result_id 拨打详情ID,show_name 数据批次,phone 被叫号码,bank_name 机构名称,dail_time 拨打时间,call_status 通话状态,result_status_desc 用户分类,resultTypeName 对话标签,round_count 对话轮次,call_time 通话时长,flow_up_status 跟进状态,bank_manager 客户经理,comment 备注",
    "showName" : "null","startTime":mt.startTime(),"with_speech_flow" : 0}
    for bid in mt.business_ids:
        JsonDic["businessId"] = bid
        r = requests.post(url=mt.data_url+"/v1/robot/report/export_excelList", params=query_params,data = json.dumps(JsonDic))
        if r.text:
            break
    print(r.text)
    print(mt.endTime())
    # print(r.json())   #下载文件非json格式
    with check:
        assert r.status_code == 200
    # assert r.json()['code'] == 20000  #下载文件是乱码




@allure.story('数据看板-拨打详情(回流)"')
def test_report_findCallLogList_118():

    query_params = {
        "access_token" : mt.get_token(),
        "startTime" : mt.startTime('pure_num'),
        "endTime" : mt.endTime('pure_num'),
        "offset" : 1,
        "limit" : 10,
        "order" : "",
        "duration" : "",
        "callStatusList" : "",
        "comment" : "",
        "resultTypeName" : "",
        "human_status" : "",
        "robotId" : "",
        "outboundNumber" : "",
        "round_count" : "",
        "seq": "",
        "phone" : "",
        "result_status_desc" : "",
        "manual_result_status_desc" : "",


    }
    for bid in mt.business_ids:
        query_params["businessId"] = bid
        r = requests.get(url=mt.data_url+"/v1/robot/sync/list", params=query_params)
        data = r.json()["data"]
        if data:
            break
    print(r.json()['data'][0]["business_name"])
    print(r.json())
    with check:
        assert r.status_code == 200
        # assert r.json()['code'] == 20000  #只有SaaS环境有数据




@allure.story('拨打概况-按场景搜索')
def test_dial_report_batch_day_119():

    query_params = {
        "access_token" : mt.get_token(),
        "org_code" :" ",
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "",
        "time_begin" : mt.startTime(),
        "time_end" : mt.endTime(),
        "is_sync" : 0,
        "data_source_ids" : "",
        "group" :"business_id",
        "is_show_disable" : 0     #弃用分类开关显示   0/关
    }
    for bid in mt.business_ids:
        query_params["businessId"] = bid
        r = requests.get(url=mt.data_url + "/v1/robot/report/dial/dial_report_batch_day", params=query_params)
        data = r.json()["data"]
        if data :
            break
    print(r.json()['data'][0]['business_id'])
    print(r.json()['data'][0]["business_name"])
    print(r.json())
    with check:
        assert r.status_code ==200



@allure.story('拨打概况-按场景-导出')
def test_dial_export_day_report_120():

    query_params = {
        "access_token": mt.get_token(),
        "org_code": "",
        "business_id": mt.test_dial_report_batch_day_119()['business_ID'],
        "time_begin": mt.startTime(),
        "time_end": mt.endTime(),
        "is_sync": 0,
        "data_source_ids": "",
        "biz_robot_types": "",
        "group": "business_id",
        "scheme": "business_name 场景名称,dial_sum 实际拨打次数,connect_count 接通次数,接通率 接通率,意向用户数 意向用户数,意向率 意向率,无意向Y 无意向Y,有意向 有意向,可能有意向T 可能有意向T"
    }
    r = requests.get(url=mt.data_url + "/v1/robot/report/dial/export_day_report", params=query_params)
    print(r.text)
    print(mt.test_dial_report_batch_day_119()['business_ID'])
    with check:
        assert r.status_code ==200




@allure.story('拨打概况-按分类搜索拨打数据')
def test_dial_report_batch_day_121():

    query_params = {
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "",
        "time_begin" : mt.startTime(),
        "time_end" : mt.endTime(),
        "is_sync" : 0,
        "data_source_ids" : "",
        "biz_types" : "",
        "biz_robot_types" : "",
        "group" : "business_id",
        "is_show_disable" : 0
    }
    for bank_org_code in mt.bank_org_code:
        query_params['org_code'] = bank_org_code
        r= requests.get(url=mt.data_url+"/v1/robot/report/dial/dial_report_batch_day",params=query_params)
        data = r.json()['data']
        if data:
            break

    print(r.json())
    print(r.json()['data'][0]["business_name"])
    with check:
        assert r.status_code ==200



@allure.story('拨打概况-按分类搜索-拨打数据导出excel')
def test_export_day_report_122():

    query_params = {
        "access_token" : mt.get_token(),
        "org_code" : mt.test_dial_report_batch_day_121()['code'],
        "time_begin" : mt.startTime(),
        "time_end" : mt.endTime(),
        "is_sync" : 0,
        "data_source_ids" : "",
        "biz_types" : "",
        "biz_robot_types" : "",
        "group" : "business_id",
        "scheme": "business_name 场景名称,dial_sum 实际拨打次数,connect_count 接通次数,接通率 接通率,未承诺还款 未承诺还款,回访失败 回访失败,愿意还款 愿意还款,有意向 有意向,可能有意向 可能有意向,回访成功 回访成功,通知到并承诺履行 通知到并承诺履行,通知中断 通知中断,无意向 无意向,非本人 非本人,已还款 已还款,通知到未承诺履行 通知到未承诺履行"
    }
    r = requests.get(url=mt.data_url+"/v1/robot/report/dial/export_day_report",params=query_params)

    print(r.text)
    with check:
        assert r.status_code == 200




@allure.story('拨打概况(回流)-按场景搜索')
def test_dial_report_batch_day_123():

    query_params = {
        "access_token" : mt.get_token(),
        "org_code" :" ",
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "",
        "time_begin" : mt.startTime(),
        "time_end" : mt.endTime(),
        "is_sync" : 1,
        "data_source_ids" : "",
        "group" :"business_id",
        "is_show_disable" : 0     #弃用分类开关显示   0/关
    }
    for bid in mt.business_ids:
        query_params["businessId"] = bid
        r = requests.get(url=mt.data_url + "/v1/robot/report/dial/dial_report_batch_day", params=query_params)
        data = r.json()["data"]
        if data :
            break
    print(r.json()['data'][0]['business_id'])
    print(r.json()['data'][0]["business_name"])
    print(r.url)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('拨打概况（回流）-按场景-导出')
def test_dial_export_day_report_124():

    query_params = {
        "access_token": mt.get_token(),
        "org_code": "",
        "business_id": mt.test_dial_report_batch_day_119()['business_ID'],
        "time_begin": mt.startTime(),
        "time_end": mt.endTime(),
        "is_sync": 1,
        "data_source_ids": "",
        "biz_robot_types": "",
        "group": "business_id",
        "scheme": "business_name 场景名称,dial_sum 实际拨打次数,connect_count 接通次数,接通率 接通率,意向用户数 意向用户数,意向率 意向率,无意向Y 无意向Y,有意向 有意向,可能有意向T 可能有意向T"
    }
    r = requests.get(url=mt.data_url + "/v1/robot/report/dial/export_day_report", params=query_params)
    print(r.text)
    print(mt.test_dial_report_batch_day_119()['business_ID'])
    with check:
        assert r.status_code ==200




@allure.story('拨打概况（回流）-按分类搜索拨打数据')
def test_dial_report_batch_day_125():

    query_params = {
        "access_token" : mt.get_token(),
        "page" : 1,
        "pageSize" : 10,
        "orderBy" : "",
        "time_begin" : mt.startTime(),
        "time_end" : mt.endTime(),
        "is_sync" : 1,
        "data_source_ids" : "",
        "biz_types" : "",
        "biz_robot_types" : "",
        "group" : "business_id",
        "is_show_disable" : 0
    }
    for bank_org_code in mt.bank_org_code:
        query_params['org_code'] = bank_org_code
        r= requests.get(url=mt.data_url+"/v1/robot/report/dial/dial_report_batch_day",params=query_params)
        data = r.json()['data']
        if data:
            break

    print(r.json())
    print(r.json()['data'][0]["business_name"])
    print(r.json()['data'][0]["business_name"])
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000




@allure.story('拨打概况（回流）-按分类搜索-拨打数据导出excel')
def test_export_day_report_126():

    query_params = {
        "access_token" : mt.get_token(),
        "org_code" : mt.test_dial_report_batch_day_121()['code'],
        "time_begin" : mt.startTime(),
        "time_end" : mt.endTime(),
        "is_sync" : 1,
        "data_source_ids" : "",
        "biz_types" : "",
        "biz_robot_types" : "",
        "group" : "business_id",
        "scheme": "business_name 场景名称,dial_sum 实际拨打次数,connect_count 接通次数,接通率 接通率,未承诺还款 未承诺还款,回访失败 回访失败,愿意还款 愿意还款,有意向 有意向,可能有意向 可能有意向,回访成功 回访成功,通知到并承诺履行 通知到并承诺履行,通知中断 通知中断,无意向 无意向,非本人 非本人,已还款 已还款,通知到未承诺履行 通知到未承诺履行"
    }
    r = requests.get(url=mt.data_url+"/v1/robot/report/dial/export_day_report",params=query_params)

    print(r.text)
    with check:
        assert r.status_code == 200



@allure.story('数据看板-线路使用报表')
def test_card_cardUsedReport_127():

    query_params ={
        "access_token" : mt.get_token(),
        "limit" : 10,
        "offset" : 1
    }
    r = requests.get(url=mt.data_url+"/v1/robot/report/card/cardUsedReport",params=query_params)
    print(r.json())
    with check:
        assert r.status_code == 200
        assert r.json()['code'] == 20000

