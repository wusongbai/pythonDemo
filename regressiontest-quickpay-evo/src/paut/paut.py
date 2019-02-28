# coding:utf-8
from src.component.instance import TestBase
from src.paut.paut_message import PautReqMsg


class TestPaut(TestBase):

    def init_request(
            self,
            order=None,
            msgid=None,
            mertranstime=None,
            order_lenth=None,
            msgid_lenth=None
    ):
        req_message = PautReqMsg()
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

        req_message.update_body("orderNum", order)
        req_message.update_body("msgId", msgid)
        req_message.update_body("merTransTime", mertranstime)
        payload = req_message.body
        return payload



