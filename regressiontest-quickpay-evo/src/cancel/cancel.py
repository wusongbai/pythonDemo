# coding:utf-8
from src.component.instance import TestBase
from src.cancel.cancel_message import CancelReqMsg
from src.purc.purc import TestPurc
import requests

class TestCancel(TestBase):
    # 请求报文只初始化 origOrderNum，orderNum，msgId，merTransTime这四个字段，需要请求其他字段时，先初始化以上四个字段再调用Message()类的update_body_()方法更新对应字段
    def init_request(
            self,
            orig_num=None,
            order=None,
            msgid=None,
            mertranstime=None
    ):
        req_message = CancelReqMsg()
        if order is None:
             # 默认生成18位订单号
            order = req_message.get_order()
        elif isinstance(order, int):
            order = req_message.get_order(length=order)
        elif order == '':
            order = order
        else:
            order =  req_message.get_order()+order

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


if __name__ == '__main__':

    cancel = TestCancel()
    num = [20, 'abc']
    for key in num:
        print cancel.init_request(orig_num=key)