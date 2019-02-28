# coding:utf-8
from src.component.instance import TestBase
from src.purc.purc_message import PurcReqMsg


class TestPurc(TestBase):

    def init_request(
            self,
            order=None,
            msgid=None,
            mertranstime=None,
            scancode=None,
            order_lenth=None,
            msgid_lenth=None,
            scan_code_length=None

    ):
        req_message = PurcReqMsg()
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

        if scancode is None:
            scancode = req_message.get_scancode()
        elif isinstance(scancode, int):
            scancode = req_message.get_scancode(length=scancode)
        else:
            scancode = scancode

        if mertranstime is None:
            mertranstime = req_message.get_mer_trans_time()
        else:
            mertranstime = mertranstime

        req_message.update_body("orderNum", order)
        req_message.update_body("msgId", msgid)
        req_message.update_body("merTransTime", mertranstime)
        req_message.update_body("scanCodeId", scancode)
        payload = req_message.body
        return payload

