# coding:utf-8
from src.component.basemessage import BaseMessage
from src.component.response import TestResponse
from src.cancel.cancel import TestCancel
import pytest

class TestCancCases(object):
    """
    测试类
    """
    lists = ["msgId", "orderNum", 'origTransType', "storeId", "termId", "origOrderNum", "respCode", "errorDetail",
             "paymentBrand", "channelOrderNum", "merTransTime", "sysTransTime", "sign"]
    inprocess = []
    success = ['channelOrderNum']
    # others = ['respCode', 'errorDetail', 'merTransTime', 'sysTransTime', 'origTransType']
    others = ['respCode', 'errorDetail', 'sysTransTime', 'merTransTime']
    req_list = ['orderNum', 'msgId', 'origOrderNum']

    # 运行merTransTime相关cases  包含merTransTime为空， 时区表示形式:800, 月份为00
    trans_time_expected = [('', lists, inprocess, success, others, req_list, 'YA'), ('20180624073122:0800', lists, inprocess, success, others, req_list, 'YB'), ('20180024073122+0800', lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('trans_time,lists,in_process, success, others, req_list, expected', trans_time_expected)
    def test_mer_trans_time(self, trans_time, lists, in_process, success, others, req_list, expected ):
        print('\n******   check [mertransTime] of [canc],merTransTime=%s'%trans_time + '   ******')
        trade_type = 'canc'
        test = TestCancel()
        payload = test.init_request(mertranstime=trans_time)
        headers = test.init_header(trade_type, payload)
        resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, in_process, success, others,
                       req_list, payload, resp, expected) == True




    # 运行client相关cases，包含client为空 ，client非空
    client_expected = [('', lists, inprocess, success, others, req_list, '00'), (u'%$中', lists, inprocess, success, others, req_list, '00')]
    @pytest.mark.parametrize('client, lists, inprocess, success, others, req_list, expected', client_expected)
    def test_client(self, client, lists, inprocess, success, others, req_list, expected ):
        print('\n******   check [client] of [canc],client=%s'%client + '   ******')
        trade_type = 'canc'
        test = TestCancel()
        payload = test.init_request()
        req_message = BaseMessage()
        payload = req_message.update_body_(payload, 'clientVer', client)
        headers = test.init_header(trade_type, payload)
        resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, inprocess, success, others,
                       req_list, payload, resp, expected) == True



    # 运行msgId相关cases  包含取值为空，特殊字符， 长度为12位，33位
    msgid_expected = [('', lists, inprocess, success, others, req_list, 'YA'), (u'&*美丽', lists, inprocess, success, others, req_list, '00'), (12, lists, inprocess, success, others, req_list, '00'), (33, lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('msgid,lists,in_process, success, others, req_list, expected', msgid_expected)
    def test_msgid(self, msgid, lists, in_process, success, others, req_list, expected ):
        print('\n******   check [msgId] of [canc],msgId=%s'%msgid + '   ******')
        trade_type = 'canc'
        test = TestCancel()
        payload = test.init_request(msgid=msgid)
        headers = test.init_header(trade_type, payload)
        resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, in_process, success, others,
                       req_list, payload, resp, expected) == True




    # 运行orderNum相关cases  包含取值为空，特殊字符， 长度为12位，32位,11位,33位
    order_expected = [('', lists, inprocess, success, others, req_list, 'YA'), (u'&*美丽', lists, inprocess, success, others, req_list, 'YB'), (12, lists, inprocess, success, others, req_list, '00'), (32, lists, inprocess, success, others, req_list, '00'), (11, lists, inprocess, success, others, req_list, 'YB'), (33, lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('order,lists,in_process, success, others, req_list, expected', order_expected)
    def test_order(self, order, lists, in_process, success, others, req_list, expected ):
        print('\n******   check [order] of [canc],order=%s'%order + '   ******')
        trade_type = 'canc'
        test = TestCancel()
        payload = test.init_request(order=order)
        headers = test.init_header(trade_type, payload)
        resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, in_process, success, others,
                       req_list, payload, resp, expected) == True




    # 运行origOrderNum相关cases  包含取值为空，特殊字符， 长度为12位，32位,11位,33位
    orig_order_expected = [('', lists, inprocess, success, others, req_list, 'YA'), (u'&*美丽', lists, inprocess, success, others, req_list, 'YB'), (12, lists, inprocess, success, others, req_list, '00'), (32, lists, inprocess, success, others, req_list, '00'), (11, lists, inprocess, success, others, req_list, 'YB'), (33, lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('orig_order,lists,in_process, success, others, req_list, expected',  orig_order_expected)
    def test_orig_order(self, orig_order, lists, in_process, success, others, req_list, expected ):
        print('\n******   check [origOrderNum] of [canc],origOrderNum=%s'%orig_order + '   ******')
        trade_type = 'canc'
        test = TestCancel()
        payload = test.init_request(orig_num=orig_order)
        headers = test.init_header(trade_type, payload)
        resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, in_process, success, others,
                       req_list, payload, resp, expected) == True




    # 运行termid相关cases，包含termid为空 ，termid特殊字符，temid长度是1位，20位，21位
    termid_expected = [('', lists, inprocess, success, others, req_list, '00'), (u'%$中', lists, inprocess, success, others, req_list, 'YB'), ('a', lists, inprocess, success, others, req_list, '00'),('12345678901234567890', lists, inprocess, success, others, req_list, '00'),('123456789012345678901', lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('termid, lists, inprocess, success, others, req_list, expected', termid_expected)
    def test_termid(self, termid, lists, inprocess, success, others, req_list, expected ):
        print('\n******   check [termid] of [canc],termid=%s'%termid + '   ******')
        trade_type = 'canc'
        test = TestCancel()
        payload = test.init_request()
        req_message = BaseMessage()
        payload = req_message.update_body_(payload, 'termId', termid)
        headers = test.init_header(trade_type, payload)
        resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, inprocess, success, others,
                       req_list, payload, resp, expected) == True
