# coding:utf-8
from src.component.instance import TestBase
from src.refd.refd_message import RefdReqMsg
from src.purc.purc import TestPurc
import requests

class TestRefd(TestBase):

    def init_request(
            self,
            orig_num=None,
            order=None,
            msgid=None,
            mertranstime=None,
            order_lenth=None,
            msgid_lenth=None
    ):
        req_message = RefdReqMsg()
        if order is None:
             # 默认生成18位订单号
            order = req_message.get_order()
        elif isinstance(order, int):
            order = req_message.get_order(length=order)
        elif order== '':
            pass
        else:
            order = req_message.get_order() + order

        if msgid is None:
           msgid = req_message.get_msgid()
        elif isinstance(msgid,int):
            msgid = req_message.get_msgid(length=msgid)
        else:
            msgid = msgid

        if mertranstime is None:
            mertranstime = req_message.get_mer_trans_time()
        else:
            mertranstime = mertranstime

        if orig_num is None:
            # 组正向交易发请求，取其orderNum为逆向交易的originOrderNum
            purc_test = TestPurc()
            trade_purc = 'purc'
            payload = purc_test.init_request()
            headers = purc_test.init_header(trade_purc, payload)
            dict = purc_test.init(trade_purc)
            url = dict.get("url", "")
            requests.post(url, json=payload, headers=headers)
            orig_num = payload['orderNum']

        elif orig_num == '':
            pass
        elif isinstance(orig_num, int):
            purc_test = TestPurc()
            trade_purc = 'purc'
            payload = purc_test.init_request(order=orig_num)
            headers = purc_test.init_header(trade_purc, payload)
            dict = purc_test.init(trade_purc)
            url = dict.get("url", "")
            requests.post(url, json=payload, headers=headers)
            orig_num = payload['orderNum']
        else:
            purc_test = TestPurc()
            trade_purc = 'purc'
            payload = purc_test.init_request( order=orig_num)
            headers = purc_test.init_header(trade_purc, payload)
            dict = purc_test.init(trade_purc)
            url = dict.get("url", "")
            requests.post(url, json=payload, headers=headers)
            orig_num = payload['orderNum']

        req_message.update_body("orderNum", order)
        req_message.update_body("msgId", msgid)
        req_message.update_body("merTransTime", mertranstime)
        req_message.update_body("origOrderNum",orig_num)

        payload = req_message.body
        return payload



