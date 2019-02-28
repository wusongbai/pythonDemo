# coding: utf-8
import random
import time


class BaseMessage(object):
    def __init__(self):
        """        定义json格式的headers和body
        """
        self.body = {}
        self.header = {
            "Authorization": "",
            "content-type": "application/json",
            "signType": "SHA256",
            "DateTime": ""
        }

    def get_order(self, length=32):
        """ 随机数生成32位订单号
        """
        chars = '0123456789'
        order = ''
        for i in range(length):
            index = random.randint(0, len(chars)) - 1
            order += chars[index]
        # print(order)
        return order


    def get_date_time(self):
        """        生成datetime
        """
        now = time.strftime("%Y%m%d%H%M%S")
        date_time = now + "+0800"
        # print(mer_trans_time)
        return date_time

    def get_mer_trans_time(self):
        """
        """
        now = time.strftime("%Y%m%d%H%M%S")
        mer_trans_time = now + "+0800"
        # print(mer_trans_time)
        return mer_trans_time

    def get_msgid(self, length=32):
        """ 生成msgId,随机生成32位字母数字组合
        """
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        msgid = ''
        for i in range(length):  # 循环32次
            index = random.randint(0, len(chars)) - 1
            msgid += chars[index]
        return msgid

    def get_scancode(self, length=16):
        """随机数生成16位条码，然后拼接70生成18位条码
        """
        chars = '0123456789'
        scancode = ''
        for i in range(length):
            index = random.randint(0, len(chars)) - 1
            scancode += chars[index]
        scancode = '70' + scancode
        # print(scancode)
        return scancode

    def update_body(self, key, value):
        """        重组报文
        """
        self.body[key] = value
        # print('body:',self.body)
        return self.body

    def update_body_(self, payload, key, value):
        """        处理报文选填项
        """
        # 将必填项写入body
        self.body = payload
        # 选填项传值
        self.body[key] = value
        # print('body:', self.body)
        return self.body

    def update_header(self, key, value):
        """        重组报文头
        """
        self.header[key] = value
        # print('body:',body)
        return self.header

