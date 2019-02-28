# coding: utf-8
import json
import hashlib

class Sign(object):
    """
    签名类
    """
    def get_signstr_e(self,http_mothod, url_string, datetime, key, body):
        '''
        拼签名字符串
        '''
        list = []
        list.append(http_mothod)
        list.append(url_string)
        list.append(datetime)
        list.append(key)
        # 将字典转换为字符串
        body = json.dumps(body)
        list.append(body)
        string = '\n'.join(list)
        # print('\n*****SignString*****')
        # print(string)
        return string


    def sha256(self,sign_string):
        '''
        调用sha256，生成签名
        :param sign_string:
        :return:
        '''
        sha256 = hashlib.sha256()
        sha256.update(sign_string.encode('utf-8'))
        sign_value = sha256.hexdigest()
        # print ("sign value：" + sign_value)
        return sign_value


    def sha1(self,sign_string):
        """
        使用sha1加密算法，返回str加密后的字符串
        """
        sha1 = hashlib.sha1()
        sha1.update(sign_string.encode('utf-8'))
        sign_value = sha1.hexdigest()
        # print("签名sha1加密结果：" + sign_value)
        return sign_value
