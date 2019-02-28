# coding:utf-8
"""
请求报文类
定义类时用new-stype，传入object参数，old-stype无object参数
"""
from src.component.basemessage import BaseMessage


class PurcReqMsg(BaseMessage):
    """
    :rtype: object
        """

    def __init__(self):
        """
        初始化所有必填项，不包含选填项
        :return:
        """
        self.body = {
            "msgId": "",
            "orderNum": "",
            "transAmt": "000000000010",
            "transCurrency": "HKD",
            "scanCodeId": "",
            "merTransTime": ""
        }
        self.header = {
            "Authorization": "",
            "content-type": "application/json",
            "signType": "SHA256",
            "DateTime": ""
        }

