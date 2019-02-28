# coding:utf-8
"""
预下单请求报文类，继承base

"""
from src.component.basemessage import BaseMessage


class PautReqMsg(BaseMessage):
    """
    :rtype: object
        """

    def __init__(self):
        """
        初始化所有必填项，不包含选填项
        :return:
        """
        # super(PautReqMsg, self).__init__()
        self.body = {
            "msgId": "",
            "orderNum": "",
            "backUrl" : "https://www.baidu.com",
            "paymentBrand": "TST",
            "transAmt": "000000000010",
            "transCurrency": "HKD",
            "merTransTime": ""
        }
        self.header = {
            "Authorization": "",
            "content-type": "application/json",
            "signType": "SHA256",
            "DateTime": ""
        }

