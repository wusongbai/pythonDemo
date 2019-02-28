#! coding:utf-8


class TestResponse(object):

    # 该方法判断响应字段取值是否等于请求报文的该字段取值
    def equal_request(self, req_list, response, request):
        # 当响应字段属于req_list且该响应字段的值等于请求报文的值返回true，其他情况返回false
        print ('##check some response fields if equal request fields##')
        flag = True
        if type(response) is not dict:
            response = response.json()
        for key in req_list:
            if request.has_key(key) is not True:
                flag = False
                print('%s of req_list is error' %key)
            elif response.has_key(key) and response[key] == request[key] or request[key] == '':
                continue
            elif response.has_key(key) == False:
                print('response has no key:%s' % key)
                flag = False
            else:
                print( 'request %s' % key + ':%s' % request[key] + ',response %s' % key + ':%s' % response[key])
                flag = False
        if flag == True:
            print('##success##')
            return True
        else:
            print('##fail##')
            return False



    def rsp_must_return(self, inprocess_list, success_list, other_list, response, expect_code):
        # 响应报文中的必返字段（除去同配置和同请求的）
        print ('##check response must return fields ##')
        flag = True
        if type(response) is not dict:
            response = response.json()
        # 检查必须返回的字段
        for key in other_list:
            # 检查应答码
            if key == 'respCode'and response.has_key(key) and response[key] != expect_code:
                flag = False
                print('expect response code is %s'%expect_code)
                print('actual response code is %s' %response[key])

            elif response.has_key(key) and response[key] != '':
                continue
            else:
                print(key + ' must return but not return')
                flag = False
        # 检查应答码是09才返回的字段
        if response.has_key('respCode') and response['respCode'] == '09':
            for key in inprocess_list:
                if response.has_key(key) and response[key] != '':
                    continue
                else:
                    print(key + ' must return but not return')
                    flag = False
        # 检查应答码是00才返回的字段
        if response.has_key('respcd') and response['respcd'] == '00':
            for key in success_list:
                if response.has_key(key) and response[key] != '':
                    continue
                else:
                    print(key + ' must return but not return')
                    flag = False
        if flag == False:
            print('##fail##')
            return False
        else:
            print('##success##')
            return True


    def rsp_is_except(sellf, response):
        # 判断响应是否异常
        print ('##check response if exception ##')
        if response is None:
            print('Response Exception')
            print('##fail##')
            return False
        else:
            print('##sucess##')
            return True


    def field_in_list(self, response, list):
        # 判断响应报文是否超出规范
        print('##check response fields if out range##')
        # print(list)
        if type(response) is not dict:
            response = response.json()
        key_list = response.keys()
        # print ('响应key：',key_list)
        for key in key_list:
            if key not in list:
                print(key + ' is not in response field')
                print('##fail##')
                return False
            else:
                continue
        print('##success##')
        return True


    def duplicat_order(self, rsp):
        """
        响应返回订单号重复，再重新生成一次订单号，重新请求
        :return:
        """
        if rsp["respcd"] == "19":
            print(u'订单号重复')

    def assert_rsp(self, lists, inprocess_list, success_list, other_list, req_list, request, response, expect_code):
        # lists 为规范的响应报文的抽象
        resault1 = self.rsp_is_except(response)
        resault2 = self.field_in_list(response, lists)
        resault3 = self.equal_request(req_list, response, request)
        resault4 = self.rsp_must_return(inprocess_list, success_list, other_list, response, expect_code)
        resault = resault1 and resault2 and resault3 and resault4
        # if resault == False:
        #     print("********Response Message********")
        #     print(response)
        #     print('\n')
        return resault


if __name__ == '__main__':

        rsp = TestResponse()
        # request = {'attach': 'abc', 'transAmt': '000000000001', 'orderNum': '123456', 'origOrderNum': '0123456'}
        # req_list = ['attach', 'transAmt', 'orderNum']
        # response1 = {'attach': 'abc', 'transAmt': '000000000001'}
        # response2 = {'attach': 'abc', 'transAmt': '000000000001', 'orderNum': '123456'}
        # response3 = {'attach': 'abc', 'transAmt': '000000000001', 'orderNum': '123'}
        # response4 = {'attach': 'abc', 'transAmt': '000000000001', 'orderNum': '123456', 'name': 'sunny'}
        # # rsp.equal_request(req_list, response1, request)
        # rsp.equal_request(req_list, response2, request)
        # rsp.equal_request(req_list, response3, request)
        # rsp.equal_request(req_list, response4, request)


        # check rsp_must_return
        inprocess = ['qrcode']
        success = ['channelOrderNum', 'payTime']
        others = ['respcd', 'errDetail', 'systime']
        response5 = {'respcd':'00'}
        response6 = {'respcd':'09', 'qrcode':'2000000'}
        response7 = {'respcd':'00','channelOrderNum':'200', 'payTime':'2019-01-01'}
        response8 = {'respcd':'00', 'errDetail':'sucess', 'systime':'20180106'}
        code1 = '00'
        code2 = '09'
        print '\ncode pass,其余fail'
        rsp.rsp_must_return(inprocess, success, others, response5, code1)
        print '\n都fail'
        rsp.rsp_must_return(inprocess, success, others, response5, code2)
        print '\ninprocess sucess'
        rsp.rsp_must_return(inprocess, success, others, response6, code2)
        print '\nsuccess sucess'
        rsp.rsp_must_return(inprocess, success, others, response7, code1)
        print '\nother success'
        rsp.rsp_must_return(inprocess, success, others, response8, code2)