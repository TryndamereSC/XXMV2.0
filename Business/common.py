# !/usr/bin python3                                 
# encoding   :   utf-8 -*-                            
# author     :   浮川                              
# File       :   commom.py
# Date       :   2021/6/2 17:07

import requests
import pytest
import uuid
import jsonpath
from datetime import datetime, timedelta



class Parameter:
    """基础类，公共参数存放"""

    endTime = datetime.today()
    startTime = (endTime - timedelta(days=365))


    #时间格式
    dateFormatDict = {
        "pure_num": "%Y%m%d%H%M%S",
        "std_date": "%Y-%m-%d %H:%M:%S",
        "only_day": "%Y-%m-%d"

    }

    data_url = 'http://test.xxm.mjoys.com/api'  #测试环境
    username = "Tester"
    password = "e31fc8d5c257fd3db1ccc6dd03e4160312163086"

    # data_url = 'http://guangdong.xxm.mjoys.com/api' #广东预发
    # username = "admin"
    # password = "ad6980fe2ca92669557eef21e5d7f9a322ad6c27"


    # data_url = 'http://jiangsu.xxm.mjoys.com/api' #江苏预发
    # username = "admin"
    # password = "ad6980fe2ca92669557eef21e5d7f9a322ad6c27"

    # data_url = 'http://xxm.mjoys.com/api'  # SaaS
    # username = "mjoys"
    # password = "e31fc8d5c257fd3db1ccc6dd03e4160312163086"



    UserAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    sessionId = uuid.uuid1()


class MyTools(Parameter):
    """
    我的工具类
    """

    # "type = " 为不同的格式获取时间参数
    def startTime(self, type="pure_num"):
        return Parameter.startTime.strftime(Parameter.dateFormatDict[type])

    def endTime(self, type="pure_num"):
        return Parameter.endTime.strftime(Parameter.dateFormatDict[type])

    def get_token(self, username=None, password=None):
        """
        获取token值
        如果参数为空，取父类值
        :param username: 传入username
        :param password: 传入password
        :return: String
        """
        if username is None:
            username = self.username
        if password is None:
            password = self.password

        query_params = {
            "client_id": "ROBOT",
            "client_secret": "1",
            "grant_type": "password",
            "remember": "1",
            "username": username,
            "password": password

        }
        try:
            r = requests.post(url=self.data_url + "/oauth/token/getAccessToken", data=query_params)
            # print(r.json())
            return r.json()['access_token']
        except Exception as e:
            return e


    def get_robot_dict(self):
        """
        获取robot_id、biz_push_result_status、biz_uni_key、org_code、parent_path值
        :return: dict
        """
        query_params = {
            "access_token": self.get_token(),
            "page": 1,
            "pageSize": 10,
            "orderBy": "time_create desc",
            "query": "",
            "business_type": "",
            "biz_robot_type": "",
            "org_code": "",
            "parent_robot_id": ""
        }
        r = requests.get(url=self.data_url + "/v1/oper/businesses", params=query_params)

        if r.json()["code"] == 20000:
            data = r.json()["data"][0]
            message = {
                "robot_id": data["robot_id"],
                "biz_push_result_status": data["biz_push_result_status"],
                "biz_uni_key": data["biz_uni_key"],
                "org_code": data["org_code"],
                "parent_path": data["parent_path"],
                "bizId" : data["id"],
                "robotId" :data["robot_id"]
            }
            return message

        return "未获取到接口参数，请检查"


    def getDataSourceBatchList(self):
        """获取data_source_batch_id（批次编号ID）"""
        query_params = {
            "access_token" : self.get_token(),
            "business_id" : self.get_robot_dict()['bizId'],
            "pageSize" : 10,
            "page" : 1,
            "orderBy" : "time_create desc",
            "is_join_call_plan" : 1,
            "is_complete" : ""
        }
        r1 = requests.get(url=self.data_url+"/v1/oper/datasource/getDataSourceBatchList",params=query_params)

        if r1.json()["code"] == 20000:
            data = r1.json()["data"][0]
            
            message = {
                "data_source_batch_id" : data['id']
            }

            return message

        return "未获取到接口参数，请检查"

    def test_list_biz(self):
        """获取biz_id"""
        query_params = {
            "access_token": self.get_token(),
            "query": "",
            "org_code": "",
            "page": 1,
            "pageSize": 10,
            "orderBy": ""
        }
        r2 = requests.get(url=self.data_url + "/v1/biz/followup/list_biz", params=query_params)

        if r2.json()['code'] ==20000:
            data = r2.json()["data"][0]

            message = {
                "biz_id": data['biz_id']
            }

            return message

        return "未获取到接口参数，请检查"

    # def test_get_result(self):
    #     """获取uni_key值到client_classify"""
    #     query_params = {
    #         "biz_uni_key": self.get_robot_dict()['biz_uni_key'],
    #         "access_token": self.get_token(),
    #         "with_default": 0
    #     }
    #     r3 = requests.get(url=self.data_url + "/v1/robot/robot_result_status/get_result", params=query_params)
    #
    #     if r3.json()['code'] == 20000:
    #         data = r3.json()["data"][1]
    #
    #         message = {
    #             "client_classify": data['uni_key']
    #         }
    #         print("整段返回参数-->",r3.text)
    #         # print("data【1】-->",data)
    #         # print("uni_key-->",message)
    #         print("get_robot_dict-->",self.get_robot_dict()['biz_uni_key'])
    #         return message
    #
    #     return "未获取到接口参数，请检查"


    def findRobotList(self):
        """获取场景模板第一个模板robot_id"""
        query_params = {
            "access_token" :  self.get_token(),
            "offset" : 1,
            "limit" : 15,
            "order" : "",
            "robot_label" : "",
            "biz_follow_type" : "",
            "robot_name" : "",
            "biz_robot_type" : ""
        }
        r3 = requests.get(url=self.data_url+"/v1/voicerobot/robot/findRobotList",params=query_params)

        if r3.json()['code'] ==20000:
            data = r3.json()["data"][0]

            message = {
                "robotID": data['robot_id']
            }

            return message

        return "未获取到接口参数，请检查"

    def test_entry_bank_list(self):
        """内置词库-词库列表"""
        query_params = {
            "access_token": self.get_token(),
            "page": 1,
            "pageSize": 10,
            "orderBy": "time_modified desc",
            "type": 1,
            "source": 1
        }
        r4 = requests.get(url=self.data_url + "/v1/nlu/entry_bank/list", params=query_params)

        if r4.json()['code'] ==20000:
            data = r4.json()['data'][0]

            message = {
                "bank_id" : data['id']
            }

            return message

        return "未获取到接口参数，请检查"


    def test_intention_list(self):
        """知识仓库-QA列表-新增意图id提取"""
        query_params = {
            "access_token": self.get_token(),
            "page" : 1,
            "pageSize" : 10,
            "orderBy" : "time_modifed desc",
            "type" : 1,
            "source" : 3
        }

        r5 = requests.get(url=self.data_url+"/v1/nlu/intention/list",params=query_params)

        if r5.json()['code'] ==20000:
            data = r5.json()['data'][0]

            message = {
                "QA_list_id" : data['id']
            }

            return message

        return "未获取到接口参数，请检查"

    def test_intention_list_103(self):
        """知识管理-知识仓库 -语料管理，获取意图语料id"""
        query_params = {
            "access_token": self.get_token(),
            "page": 1,
            "pageSize": 10,
            "orderBy": "time_modifed desc",
            "type": 1,
            "source": 3
        }
        r6 = requests.get(url=self.data_url + "/v1/nlu/intention/list", params=query_params)

        if r6.json()['code'] ==20000:
            data = r6.json()['data'][1]

            message = {
                "int_id" : data['id']
            }

            return message

        return "未获取到接口参数，请检查"

    def test_intention_list_104(self):
        """知识管理-知识仓库-获取语态仓库意图id"""
        query_params = {
            "access_token": self.get_token(),
            "page": 1,
            "pageSize": 10,
            "orderBy": "time_modifed desc",
            "type": 3,
            "source": 3
        }
        r7 = requests.get(url=self.data_url + "/v1/nlu/intention/list", params=query_params)
        if r7.json()['code'] ==20000:
            data = r7.json()['data'][0]

            message = {
                "intention_id" : data['id']
            }

            return message

        return "未获取到接口参数，请检查"

    def test_dial_report_batch_day_119(self):
        """拨打概况-按场景导出-获取导出场景business_id"""
        query_params = {
            "access_token": self.get_token(),
            "org_code": " ",
            "page": 1,
            "pageSize": 10,
            "orderBy": "",
            "time_begin": self.startTime(),
            "time_end": self.endTime(),
            "is_sync": 0,
            "data_source_ids": "",
            "group": "business_id",
            "is_show_disable": 0
        }
        for bid in self.business_ids:
            query_params["businessId"] = bid
            r8 = requests.get(url=self.data_url + "/v1/robot/report/dial/dial_report_batch_day", params=query_params)
            data = r8.json()["data"]
            if data:
                break
        if r8.json()['code'] ==20000:
            data = r8.json()['data'][0]

            message = {
                "business_ID" : data['business_id']
            }

            return message

        return "未获取到接口参数，请检查"

    def test_dial_report_batch_day_121(self):
        """拨打概况-按分类搜索拨打数据-导出提取有数据的银行code"""
        query_params = {
            "access_token": self.get_token(),
            "page": 1,
            "pageSize": 10,
            "orderBy": "",
            "time_begin": self.startTime(),
            "time_end": self.endTime(),
            "is_sync": 0,
            "data_source_ids": "",
            "biz_types": "",
            "biz_robot_types": "",
            "group": "business_id",
            "is_show_disable": 0
        }
        for bank_org_code in self.bank_org_code:
            query_params['org_code'] = bank_org_code
            r11 = requests.get(url=self.data_url + "/v1/robot/report/dial/dial_report_batch_day", params=query_params)
            data = r11.json()['data']
            if data:
                break

        if r11.json()['code'] == 20000:
            data = r11.json()['data'][0]

            message = {
            "code": data['org_code']
        }

            return message

        return "未获取到接口参数，请检查"




    def test_org_list(self):
        """获取设备管理-新建设备所属机构"""
        query_params = {
            "access_token" : self.get_token()
        }
        r12 = requests.get(url=self.data_url+"/v1/bank/org/list",params=query_params)
        if r12.json()['code'] == 20000:
            data = r12.json()['data']

            message = {
            "bank_code" : data[0]['code'],
            "account_ids": data[0]['account_id']
        }

            return message

        return "未获取到接口参数，请检查"


    def test_getVoiceDeviceList_128(self):
        """工程管理-设备管理列表-获取设备编号"""
        query_params = {
            "access_token": self.get_token(),
            "order": "-id",
            "offset": 1,
            "limit": 10,
            "account_ids": self.test_org_list()['account_ids'],
            "org_code": ""
        }
        r13 = requests.get(url=self.data_url + "/v1/oper/device/getVoiceDeviceList", params=query_params)
        if r13.json()['code'] == 20000:
            data = r13.json()['data']

            message = {
            "equipment_id" : data[0]['id'],
            "Device_Code" : data[0]['device_code'],
        }
            return message

        return "未获取到接口参数，请检查"

    def test_getCardSlotList_132(self):
        """设备管理-操作-卡口配置列表-获取卡口ID"""
        query_params = {
            "access_token": self.get_token(),
            "device_id": self.test_getVoiceDeviceList_128()['equipment_id'],
            "order": "+code",
            "offset": 1,
            "limit": 16
        }
        r14= requests.get(url=self.data_url + "/v1/oper/device/getCardSlotList", params=query_params)
        if r14.json()['code'] == 20000:
            data = r14.json()['data']

            message = {
            "Bayone_id" : data [0]['id']
        }
            return message
        return "未获取到接口参数，请检查"




    @property
    def business_ids(self):
        """提取拨打详情场景id"""
        query_params = {
            "access_token" : self.get_token(),
            "org_code" : ""
        }
        r9 = requests.get(url=self.data_url+"/v1/oper/businesses",params=query_params)

        if r9.json()['code'] ==20000:
            data = r9.json()['data']
            return [v["id"] for v in data]

        return "未获取到接口参数，请检查"

    @property
    def bank_org_code(self):
        """提取所有银行code"""
        query_params = {
            "access_token" : self.get_token(),
            "query" : "",
            "is_manage" : 0,
            "is_check_biz" :1
        }
        r10 = requests.get(url=self.data_url+"/v1/bank/org/list",params=query_params)

        if r10.json()['code'] ==20000:
            data = r10.json()['data']
            return [v['code'] for v in data]

        return "未获取到接口参数，请检查"


    def test_need_flow(self):
        """获取有跟进客户数据的场景"""
        query_params = {
            "access_token": self.get_token(),
            "query": "",
            "org_code": "",
            "page": 1,
            "pageSize": 10,
            "orderBy":""

        }
        r15 = requests.get(url=self.data_url + "/v1/robot/crm/biz_list", params=query_params)
        data = r15.json()['data']
        need_flow = jsonpath.jsonpath(data, '$..[?(@.need_flow>1)]')

        need_f = need_flow[0]['biz_id']

        return need_f


    def test_robot_crm_list(self):
        query_params ={
        "access_token" : self.get_token(),
        "page" : 1,
        "pageSize": 10,
        "orderBy": "alloc_time desc",
        "biz_id" : self.test_need_flow()
    }
        r16 = requests.get(url=self.data_url+"/v1/robot/crm/list",params=query_params)

        if r16.json()['code'] == 20000:
            data = r16.json()['data']
            message = {
            "cont_id" : data[0]['crm_cont_id'],
            "busin_name" : data[0]['business_name']
        }
            return message

        return "未获取到接口参数，请检查"








if __name__ == '__main__':

    test = MyTools()
    # token = test.get_token()
    # print(token)
    # biz_uni_key = test.get_robot_dict()
    # print(biz_uni_key)
    # id = test.getDataSourceBatchList()
    # print("id-->",id)
    # biz_id = test.test_list_biz()
    # print(biz_id)
    # bank_id =test.test_entry_bank_list()
    # print(bank_id)
    # id =test.test_intention_list()
    # print(id)
    # id = test.test_intention_list_103()
    # print(id)
    # id = test.test_intention_list_104()
    # print(id)
    # ids = test.business_ids
    # print(ids)
    # code = test.bank_org_code
    # print(code)
    #
    # business_id = test.test_dial_report_batch_day_119()
    # print(business_id)
    #
    # org_code = test.bank_org_code
    # print(org_code)
    # bank_code = test.bank_org_code
    # print(bank_code)
    # print(str(bank_code[0]))
    #
    #
    # equipment_id = test.test_getVoiceDeviceList_128()
    # print(equipment_id)
    #
    # Device_Code= test.test_getVoiceDeviceList_128()
    # print(Device_Code)
    # #
    # Bayone_id = test.test_getCardSlotList_132()
    # print(Bayone_id)
    #
    # robotId = test.get_robot_dict()
    # print(robotId)
    # print(uuid.uuid1())
    # need_flow = test.test_need_flow()
    # print(need_flow)
    # biz_id = test.test_need_flow()
    # print(biz_id)
    need_f = test.test_need_flow()
    print(need_f)
    cont_id = test.test_robot_crm_list()
    print(cont_id)


