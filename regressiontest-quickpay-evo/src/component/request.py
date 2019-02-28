# coding: utf-8
import json

import requests

from src.component.basemessage import BaseMessage
from src.component.sign import Sign

class Request(object):
    def http_post(self, url, payload, headers):
        """
        封装request.post()
        需要先将payload转换成字符串再请求
        :param url:
        :param payload:
        :param headers:
        :return:
        """

        try:
            payload = json.dumps(payload)
            # rsp = requests.post(url, headers=headers, data=payload) #会出现SSL:CERTIFICATE_VERIFY_FAILED错误
            rsp = requests.post(url, headers=headers, data=payload, verify=False)
            return rsp
        except Exception as errlog:
            print("Response Exception:%s" %errlog)

        finally:
            pass
            # print(rsp)

