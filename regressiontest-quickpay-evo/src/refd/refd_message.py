# coding: utf-8

from src.component.basemessage import BaseMessage


class RefdReqMsg(BaseMessage):

    def __init__(self):
        # super(RefdReqMsg, self).__init__()
        self.body = {
            "msgId": "",
            "orderNum": "",
            "origOrderNum": "",
            "transAmt": "000000000010",
            "merTransTime": ""
        }
        self.headers = {
            "Authorization": "",
            "content-type": "application/json",
            "signType": "SHA256",
            "DateTime": ""
        }
