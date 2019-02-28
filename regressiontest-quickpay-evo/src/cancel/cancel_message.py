# coding: utf-8

from src.component.basemessage import BaseMessage


class CancelReqMsg(BaseMessage):

    def __init__(self):
        # super(RefdReqMsg, self).__init__()
        self.body = {
            "msgId": "",
            "orderNum": "",
            "origOrderNum": "",
            # 取消请求报文transAmt不是必填项目，且响应报文不返transAmt
            # "transAmt": "000000000010",
            "merTransTime": ""
        }
        self.headers = {
            "Authorization": "",
            "content-type": "application/json",
            "signType": "SHA256",
            "DateTime": ""
        }
