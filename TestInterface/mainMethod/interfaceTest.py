#Author: ls Liu
# encoding= utf-8
import requests
from mainMethod.readConfig import readConf
from Common.dataTypeTransformation import strToDict
from LogConf.loggerConf import loggerConf


reqUrl = readConf().getServicesInfo()
logger = loggerConf().getLog()

'''接口请求的封装'''
class APITest(object):
    def __init__(self,url,method,headers,data):
        self.request_url = url
        logger.info("接口请求地址：%s" %self.request_url)

        self.request_method = method
        logger.info("接口请求方法：%s" %self.request_method)

        self.request_headers = headers
        logger.info("接口请求头：%s" %self.request_headers)

        self.request_body = data
        self.request_body = self.request_body.encode('utf-8')  #注意 入参会存在中文，需要转码处理
        logger.info("接口请求参数：%s" %self.request_body)

    def testApi(self):
        if self.request_method != None and self.request_method != '':
            if self.request_url != None and self.request_url != '':
                self.request_url = reqUrl+self.request_url
                if self.request_headers == '' or self.request_headers == None:
                    request_headers = {}
                    logger.debug("接口请求头信息为%s" % request_headers ) #<class 'dict'>
                else:
                    request_headers = strToDict(self.request_headers)
                    logger.debug("接口请求头信息为%s" % request_headers) #<class 'dict'>
            else:
                logger.error("参数非法（请求地址为空）")
        else:
            logger.error("参数非法（请求方法为空）")

        if self.request_method.upper() == 'GET':
            getResponse = requests.get(url=self.request_url, headers=request_headers, params=self.request_body)
            return getResponse.status_code,getResponse.text
        elif self.request_method.upper() == 'POST':
            postResponse = requests.post(url=self.request_url, headers=request_headers, data=self.request_body)
            return postResponse.status_code,postResponse.text
        else:
            logger.error("参数非法（请求方法为空）")



