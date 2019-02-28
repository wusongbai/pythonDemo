# coding: utf-8

from src.component.basemessage import BaseMessage


class QueryReqMsg(BaseMessage):

    def __init__(self):
        # super(RefdReqMsg, self).__init__()
        self.body = {
            "msgId": "",
            # "orderNum": "",
            "origOrderNum": ""
        }
        self.headers = {
            "Authorization": "",
            "content-type": "application/json",
            "signType": "SHA256",
            "DateTime": ""
        }
