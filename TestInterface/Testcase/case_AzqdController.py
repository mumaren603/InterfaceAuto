#Author: ls Liu
import unittest
from mainMethod.interfaceTest import APITest
from Common.getCaselistInfo import isFuncNameExistsList
from Common.getCaselistInfo import caselist
from LogConf.loggerConf import loggerConf

logger = loggerConf().getLog()

class azqdController(unittest.TestCase):
    def setUp(self):
        pass

    def test_getAzqdById001(self):
        i = isFuncNameExistsList("test_getAzqdById001")
        if i or i== 0:
            logger.debug("该接口在list中下标是：%d" %i)
            self.apiName = caselist[i][3]
            self.url = caselist[i][6]
            self.method = caselist[i][5]
            self.headers = caselist[i][7]
            self.data = caselist[i][8]
            self.expectRes = caselist[i][9]
            try:
                actualRes = APITest(self.apiName,self.url, self.method, self.headers, self.data).testApi()
                self.assertIn(self.expectRes,actualRes[1])
                logger.debug("%s接口断言正确，响应信息为:%s" % (self.apiName, actualRes))  # tuple
            except AssertionError as e:
                logger.error("%s接口断言错误，错误信息为:%s" % (self.apiName, e))
                raise AssertionError
        else:
            logger.error("该接口不存在List中！" )
            raise IndexError


    def test_getDaglHxx001(self):
        i = isFuncNameExistsList("test_getDaglHxx001")
        if i or i== 0:
            logger.debug("该接口在list中下标是：%d" %i)
            self.apiName = caselist[i][3]
            self.url = caselist[i][6]
            self.method = caselist[i][5]
            self.headers = caselist[i][7]
            self.data = caselist[i][8]
            self.expectRes = caselist[i][9]
            try:
                actualRes = APITest(self.apiName,self.url, self.method, self.headers, self.data).testApi()
                self.assertIn(self.expectRes,actualRes[1])
                logger.debug("%s接口断言正确，响应信息为:%s" % (self.apiName, actualRes))  # tuple
            except AssertionError as e:
                logger.error("%s接口断言错误，错误信息为:%s" % (self.apiName, e))
                raise AssertionError
        else:
            logger.error("该接口不存在List中！")
            raise IndexError

    def test_getCfQlrxx001(self):
        i = isFuncNameExistsList("test_getCfQlrxx001")
        if i or i== 0:
            logger.debug("该接口在list中下标是：%d" %i)
            self.apiName = caselist[i][3]
            self.url = caselist[i][6]
            self.method = caselist[i][5]
            self.headers = caselist[i][7]
            self.data = caselist[i][8]
            self.expectRes = caselist[i][9]
            try:
                actualRes = APITest(self.apiName,self.url, self.method, self.headers, self.data).testApi()
                self.assertIn(self.expectRes,actualRes[1])
                logger.debug("%s接口断言正确，响应信息为:%s" % (self.apiName, actualRes))  # tuple
            except AssertionError as e:
                logger.error("%s接口断言错误，错误信息为:%s" % (self.apiName, e))
                raise AssertionError
        else:
            logger.error("该接口不存在List中！")
            raise IndexError


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main