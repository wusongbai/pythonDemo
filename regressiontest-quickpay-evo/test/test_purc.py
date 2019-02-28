# coding: utf-8
from src.component.response import TestResponse
from src.purc.purc import TestPurc
from src.component.basemessage import BaseMessage
import pytest

class TestPurcCases(object):
    """
    测试类
    """
    lists = ["msgId", "orderNum", "storeId", "termId", "respCode", "errorDetail", 'transAmt', 'transCurrency', 'billingAmt', 'billingCurrency', 'billingExchangeRate','consumerAccount', 'consumerId', 'convTransAmt', 'convTransCurrency','convTransExchangeRate', 'convRateDate',
             'payTime', 'paymentBrand', "channelOrderNum", "merTransTime", "sysTransTime", 'attach', "sign"]
    inprocess = []
    success = ['channelOrderNum', 'paymentBrand', 'consumerAccount', 'consumerId', 'payTime']
    # others = ['respCode', 'errorDetail', 'merTransTime', 'sysTransTime', 'origTransType']
    others = ['respCode', 'errorDetail', 'sysTransTime', 'merTransTime']
    req_list = ['orderNum', 'msgId', 'transAmt', 'transCurrency', ]


    # 运行client相关cases  包含取值为空, 非空
    client_expect = [('', lists, inprocess, success, others, req_list, '00'),  ('abc123', lists, inprocess, success, others, req_list, '00')]
    @pytest.mark.parametrize('client,lists,in_process, success, others, req_list, expected',client_expect)
    def test_client(self, client,lists,in_process, success, others, req_list, expected):
        print('\n******   check [client] of [purc],client=%s'%client + '   ******')
        trade_type = "purc"
        test = TestPurc()
        payload = test.init_request()
        req_message = BaseMessage()
        payload = req_message.update_body_(payload, "clientVer", client)
        headers = test.init_header(trade_type, payload)
        response = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists,in_process, success, others, req_list,payload, response, expected) == True


    # 运行transCurrency相关cases  包含取值为空, 币种2位，4位，非门店币种
    currency_expect = [('', lists, inprocess, success, others, req_list, 'YA'), ('HK', lists, inprocess, success, others, req_list, 'YB'), ('HHKD', lists, inprocess, success, others, req_list, 'YB'), ('RMB', lists, inprocess, success, others, req_list, 'J2'), ('156', lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('currency,lists,in_process, success, others, req_list, expected',currency_expect)
    def test_currency(self, currency,lists,in_process, success, others, req_list, expected):
        print('\n******   check [transCurrency] of [purc],transCurrency=%s'%currency + '   ******')
        trade_type = "purc"
        test = TestPurc()
        payload = test.init_request()
        req_message = BaseMessage()
        payload = req_message.update_body_(payload, "transCurrency", currency)
        headers = test.init_header(trade_type, payload)
        response = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists,in_process, success, others, req_list,payload, response, expected) == True


    # 运行goodsList相关cases  包含取值为空, 非空
    goodslist_expect = [('', lists, inprocess, success, others, req_list, '00'), ('HK', lists, inprocess, success, others, req_list, '00')]
    @pytest.mark.parametrize('goodslist,lists,in_process, success, others, req_list, expected',goodslist_expect)
    def test_goodslist(self, goodslist, lists,in_process, success, others, req_list, expected):
        print('\n******   check [goodsList] of [purc],goodsList=%s'%goodslist + '   ******')
        trade_type = "purc"
        test = TestPurc()
        payload = test.init_request()
        req_message = BaseMessage()
        payload = req_message.update_body_(payload, "goodsList", goodslist)
        headers = test.init_header(trade_type, payload)
        response = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists,in_process, success, others, req_list,payload, response, expected) == True

    # 运行msgId相关cases  包含取值为空，特殊字符， 长度为12位，33位
    msgid_expected = [('', lists, inprocess, success, others, req_list, 'YA'), (u'&*美丽', lists, inprocess, success, others, req_list, '00'), (12, lists, inprocess, success, others, req_list, '00'), (33, lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('msgid,lists,in_process, success, others, req_list, expected', msgid_expected)
    def test_msgid(self, msgid, lists, in_process, success, others, req_list, expected ):
        print('\n******   check [msgId] of [purc],msgId=%s'%msgid + '   ******')
        trade_type = 'purc'
        test = TestPurc()
        payload = test.init_request(msgid=msgid)
        headers = test.init_header(trade_type, payload)
        canc_resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, in_process, success, others,
                       req_list, payload, canc_resp, expected) == True


     # 所有取值都取正常值
    expected = [(lists, inprocess, success, others, req_list, '00')]
    @pytest.mark.parametrize('lists,in_process, success, others, req_list, expected', expected)
    def test_normal(self, lists, in_process, success, others, req_list, expected):
        print('\n******   check [nomal] of [purc]   ******')
        trade_type = 'purc'
        test = TestPurc()
        payload = test.init_request()
        headers = test.init_header(trade_type, payload)
        canc_resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, in_process, success, others,
                       req_list, payload, canc_resp, expected) == True


     # 运行orderNum相关cases  包含取值为空，特殊字符， 长度为12位，32位,11位,33位
    order_expected = [('', lists, inprocess, success, others, req_list, 'YA'), (u'&*美丽', lists, inprocess, success, others, req_list, 'YB'), (12, lists, inprocess, success, others, req_list, '00'), (32, lists, inprocess, success, others, req_list, '00'), (11, lists, inprocess, success, others, req_list, 'YB'), (33, lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('order,lists,in_process, success, others, req_list, expected', order_expected)
    def test_order(self, order, lists, in_process, success, others, req_list, expected ):
        print('\n******   check [order] of [purc],order=%s'%order + '   ******')
        trade_type = 'purc'
        test = TestPurc()
        payload = test.init_request(order=order)
        headers = test.init_header(trade_type, payload)
        canc_resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, in_process, success, others,
                       req_list, payload, canc_resp, expected) == True

    # 运行scanCode相关cases  包含取值为空，非数字， 长度为1，32位,33位
    scancode_expected = [('', lists, inprocess, success, others, req_list, 'YA'), ('aaa', lists, inprocess, success, others, req_list, 'Y0'), ('1', lists, inprocess, success, others, req_list, 'Y0'), (30, lists, inprocess, success, others, req_list, '00'), (31, lists, inprocess, success, others, req_list, '00')]
    @pytest.mark.parametrize('scancode,lists,in_process, success, others, req_list, expected', scancode_expected)
    def test_scancode(self, scancode, lists, in_process, success, others, req_list, expected ):
        print('\n******   check [scanCodeId] of [purc],scanCodeId=%s'%scancode + '   ******')
        trade_type = 'purc'
        test = TestPurc()
        payload = test.init_request(scancode=scancode)
        headers = test.init_header(trade_type, payload)
        canc_resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, in_process, success, others,
                       req_list, payload, canc_resp, expected) == True

    # 运行termid相关cases，包含termid为空 ，termid特殊字符，temid长度是1位，20位，21位
    termid_expected = [('', lists, inprocess, success, others, req_list, '00'), (u'%$中', lists, inprocess, success, others, req_list, 'YB'), ('a', lists, inprocess, success, others, req_list, '00'),('12345678901234567890', lists, inprocess, success, others, req_list, '00'),('123456789012345678901', lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('termid, lists, inprocess, success, others, req_list, expected', termid_expected)
    def test_termid(self, termid, lists, inprocess, success, others, req_list, expected ):
        print('\n******   check [termid] of [canc],termid=%s'%termid + '   ******')
        trade_type =  'purc'
        test = TestPurc()
        payload = test.init_request()
        req_message = BaseMessage()
        payload = req_message.update_body_(payload, 'termId', termid)
        headers = test.init_header(trade_type, payload)
        canc_resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, inprocess, success, others,
                       req_list, payload, canc_resp, expected) == True


     # 运行transAmt相关cases，包含取值为空 ，0，长度12位，999999999999，000000002475  11位：09090909011
    transamt_expected = [('', lists, inprocess, success, others, req_list, 'YB'), ('0', lists, inprocess, success, others, req_list, 'YB'), ('000000000010', lists, inprocess, success, others, req_list, '00'),('999999999999', lists, inprocess, success, others, req_list, '00'),('000000002475', lists, inprocess, success, others, req_list, '00'),('09090909011', lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('transamt, lists, inprocess, success, others, req_list, expected', transamt_expected)
    def test_transamt(self, transamt, lists, inprocess, success, others, req_list, expected ):
        print('\n******   check [transAmt] of [purc],transamt=%s'%transamt + '   ******')
        trade_type =  'purc'
        test = TestPurc()
        payload = test.init_request()
        req_message = BaseMessage()
        payload = req_message.update_body_(payload, 'transAmt', transamt)
        headers = test.init_header(trade_type, payload)
        canc_resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, inprocess, success, others,
                       req_list, payload, canc_resp, expected) == True


    # 运行mertransTime相关cases，包含取值为空 ，0，时区为:0800 ，月份为00
    trans_time_expected = [('', lists, inprocess, success, others, req_list, 'YA'), ('20180624073122:0800', lists, inprocess, success, others, req_list, 'YB'), ('20180024073122+0800', lists, inprocess, success, others, req_list, 'YB')]
    @pytest.mark.parametrize('trans_time,lists,in_process, success, others, req_list, expected', trans_time_expected)
    def test_mer_trans_time(self, trans_time, lists, in_process, success, others, req_list, expected ):
        print('\n******   check [mertransTime] of [purc],merTransTime=%s'%trans_time + '   ******')
        trade_type =  'purc'
        test = TestPurc()
        payload = test.init_request(mertranstime=trans_time)
        headers = test.init_header(trade_type, payload)
        canc_resp = test.req_post(trade_type, payload, headers)
        rsp = TestResponse()
        assert rsp.assert_rsp(lists, in_process, success, others,
                       req_list, payload, canc_resp, expected) == True