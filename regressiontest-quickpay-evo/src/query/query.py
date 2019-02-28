# coding:utf-8
from src.component.instance import TestBase
from src.query.query_message import QueryReqMsg
from src.purc.purc import TestPurc
import requests


class TestQuery(TestBase):
    def init_request(
            self,
            orig_num=None,
            order=None,
            msgid=None
    ):
        req_message = QueryReqMsg()

        if order == 'normal':
            # 默认生成18位订单号
            order = req_message.get_order()
            req_message.update_body("orderNum", order)
        elif isinstance(order, int):
            order = req_message.get_order(length=order)
            req_message.update_body("orderNum", order)
        elif order is None:
            # del req_message.body["orderNum"]
            pass
        elif order == '':
            req_message.update_body("orderNum", order)
        else:
            order = req_message.get_order() + order
            req_message.update_body("orderNum", order)

        if msgid is None:
            msgid = req_message.get_msgid()
            req_message.update_body("msgId", msgid)
        elif isinstance(msgid, int):
            msgid = req_message.get_msgid(length=msgid)
            req_message.update_body("msgId", msgid)
        else:
            msgid = msgid
            req_message.update_body("msgId", msgid)

        if orig_num is None:
            # 组正向交易发请求，取其orderNum为逆向交易的originOrderNum
            purc_test = TestPurc()
            trade_purc = 'purc'
            payload = purc_test.init_request()
            headers = purc_test.init_header(trade_purc, payload)
            dict = purc_test.init(trade_purc)
            url = dict.get("url","")
            requests.post(url, json=payload, headers=headers)
            # purc_test.req_post(trade_purc, payload, headers)
            orig_num = payload.get("orderNum", "")
            req_message.update_body("origOrderNum", orig_num)

        elif orig_num == '':
            pass
        # 要保证正向交易的订单号是整数
        elif isinstance(orig_num, int):
            purc_test = TestPurc()
            trade_purc = 'purc'
            payload = purc_test.init_request(order=orig_num)
            headers = purc_test.init_header(trade_purc, payload)
            dict = purc_test.init(trade_purc)
            url = dict.get("url","")
            requests.post(url, json=payload, headers=headers)
            # purc_test.req_post(trade_purc, payload, headers)
            orig_num = payload.get("orderNum", "")
            req_message.update_body("origOrderNum", orig_num)
        # orig_num为特殊字符、中文等case
        else:
            purc_test = TestPurc()
            trade_purc = 'purc'
            payload = purc_test.init_request(order=orig_num)
            headers = purc_test.init_header(trade_purc, payload)
            dict = purc_test.init(trade_purc)
            url = dict.get("url","")
            requests.post(url, json=payload, headers=headers)
            # purc_test.req_post(trade_purc, payload, headers)
            orig_num = payload.get("orderNum", "")
            req_message.update_body("origOrderNum", orig_num)

        return req_message.body
