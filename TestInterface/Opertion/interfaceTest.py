#Author: ls Liu
import requests
from Opertion import ExcelOpertion
from Opertion import readConfig
from common import commFunc
import unittest
filePath = readConfig.readConf().getExcelInfo()
reqUrl = readConfig.readConf().getHttpInfo()
caselist = ExcelOpertion.excelTest(filePath).readExcel()  #获取所有测试用例


'''
以下代码未测试用例一次性执行完毕，但是如何生成测试报告，还没想到如何解决
等待后续解决。

class APITest(object):
    def __init__(self):
        pass

    def testApi(self):
        for i in range(len(caselist)):
            print("这是第%s个用例" %(i+1))

            request_api_name = caselist[i][2]
            print("接口请求名为%s" % request_api_name, type(request_api_name))

            request_method = caselist[i][5]
            print("接口请求方式为%s" %request_method,type(request_method))

            request_url = reqUrl+caselist[i][6]
            print("接口请求URL为：%s" %request_url,type(request_url))

            request_headers = caselist[i][7]
            #print("接口请求头信息为%s" % request_headers,type(request_headers))

            request_body = caselist[i][8]
            print("接口请求报文为%s" % request_body,type(request_body))

            if request_method != None and request_method != '':
                if request_url != None and request_url != '':
                    if request_headers == '' or request_headers == None:
                        request_headers = {}
                        print("接口请求头信息为%s" % request_headers, type(request_headers))
                    else:
                        request_headers = commFunc.strToDict(request_headers)
                        print("接口请求头信息为%s" % request_headers, type(request_headers))
                else:
                    print("参数非法（请求地址为空）")
            else:
                print("参数非法（请求方法为空）")

            if request_method.upper() == 'GET':
                getResponse = requests.get(url=request_url, headers=request_headers, params=request_body)
                print(getResponse.text)
            elif request_method.upper() == 'POST':
                postResponse = requests.post(url=request_url, headers=request_headers, data=request_body)
                print(postResponse.text)
            else:
                print("请求方法未定义")
'''

# APITest().testApi()
'''***********************************************'''


'''接口请求的封装'''
class APITest2(object):
    def __init__(self,url,method,headers,data):
        self.request_url = url
        self.request_method = method
        self.request_headers = headers
        self.request_body = data

    def testApi(self):
        if self.request_method != None and self.request_method != '':
            if self.request_url != None and self.request_url != '':
                self.request_url = reqUrl+self.request_url
                if self.request_headers == '' or self.request_headers == None:
                    request_headers = {}
                    print("接口请求头信息为%s" % request_headers, type(request_headers))
                else:
                    request_headers = commFunc.strToDict(self.request_headers)
                    print("接口请求头信息为%s" % request_headers, type(request_headers))
            else:
                print("参数非法（请求地址为空）")
        else:
            print("参数非法（请求方法为空）")

        if self.request_method.upper() == 'GET':
            getResponse = requests.get(url=self.request_url, headers=request_headers, params=self.request_body)
            print(getResponse.text)
        elif self.request_method.upper() == 'POST':
            postResponse = requests.post(url=self.request_url, headers=request_headers, data=self.request_body)
            print(postResponse.text)
        else:
            print("请求方法未定义")



'''测试用例'''
class apiTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_getDaglHxx(self):
        self.url = caselist[0][6]
        self.method = caselist[0][5]
        self.headers = caselist[0][7]
        self.data = caselist[0][8]

        APITest2(self.url,self.method,self.headers,self.data).testApi()

    def test_getBdcdyxxById(self):
        self.url = caselist[1][6]
        self.method = caselist[1][5]
        self.headers = caselist[1][7]
        self.data = caselist[1][8]

        APITest2(self.url,self.method,self.headers,self.data).testApi()

    def test_getAzqdById(self):
        self.url = caselist[2][6]
        self.method = caselist[2][5]
        self.headers = caselist[2][7]
        self.data = caselist[2][8]

        APITest2(self.url,self.method,self.headers,self.data).testApi()

    def test_getFwqsj(self):
        self.url = caselist[3][6]
        self.method = caselist[3][5]
        self.headers = caselist[3][7]
        self.data = caselist[3][8]

        APITest2(self.url,self.method,self.headers,self.data).testApi()

    def test_getCfQlrxx(self):
        self.url = caselist[4][6]
        self.method = caselist[4][5]
        self.headers = caselist[4][7]
        self.data = caselist[4][8]

        APITest2(self.url,self.method,self.headers,self.data).testApi()
    def tearDown(self):
        pass


if __name__ =='__main__':
    suite = unittest.TestSuite()

    suite.addTest(apiTest("test_getDaglHxx"))
    suite.addTest(apiTest("test_getBdcdyxxById"))
    suite.addTest(apiTest("test_getAzqdById"))
    suite.addTest(apiTest("test_getFwqsj"))

    runner = unittest.TextTestRunner()

    runner.run(suite)

