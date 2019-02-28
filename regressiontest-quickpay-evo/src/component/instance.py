# coding:utf-8
from src.component.basemessage import BaseMessage
from src.component.request import *


class TestBase(object):

    # def __init__(self,trade_type, sid=None):
    #     self.key = "qV3rPz4UBenRTjUJE19nt4eKhVLSDMeq"
    #     self.sid = "978015600000001"
    #     self.trade_type = trade_type
    #     self.url_string ="/scanpay/mer/" + self.sid+ "/" +self.trade_type+ "/v0"
    #     # print (self.url_string)

    def init(self, trade_type, sid=None):
        key = "d39330b7659649cf6304052458502a1e"
        sid = "S005247"
        trade_type = trade_type
        url_string ="/scanpay/mer/" + sid + "/" + trade_type + "/v0"
        TEST_URL = "https://test.everonet.com"
        url = TEST_URL + url_string
        dicts = {}
        dicts["url"] = url
        dicts["key"] = key
        dicts["url_string"] = url_string
        return dicts

    def init_header(self, trade_type, payload):
        req_message = BaseMessage()
        test = TestBase()
        dicts = test.init(trade_type)
        key = dicts["key"]
        url_string = dicts["url_string"]
        auth = test.init_sign(key, url_string, payload)
        datetime = req_message.get_date_time()
        req_message.update_header("Authorization", auth)
        req_message.update_header("DateTime", datetime)
        headers = req_message.header
        return headers

    def init_sign(self, key, url_string, payload, method="POST"):
        sign_ = Sign()
        req_message = BaseMessage()
        datetime = req_message.get_date_time()
        sign_str = sign_.get_signstr_e(
            method, url_string, datetime, key, payload)
        sha256 = sign_.sha256(sign_str)
        return sha256

    def req_post(self, trade_type, payload, headers):
        req_ = Request()
        test = TestBase()
        dicts_ = test.init(trade_type)
        url = dicts_["url"]
        print("****** url ******")
        print(url)
        print("****** headers ******")
        print(headers)
        print("****** Request Message ******")
        print(payload)
        rsp_ = req_.http_post(url, payload, headers)
        print("********Response Message********")
        print (rsp_.content)
        rsp_ = rsp_.json()
        return rsp_


