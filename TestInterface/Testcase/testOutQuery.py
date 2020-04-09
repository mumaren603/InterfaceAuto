#Author: ls Liu
import unittest
from mainMethod.interfaceTest import APITest
from Common.getCaselistInfo import isFuncNameExistsList
from Common.getCaselistInfo import caselist
from LogConf.loggerConf import loggerConf

logger = loggerConf().getLog()

#外部查询接口
class testOutQuery(unittest.TestCase):
    def setUp(self):
        pass

    #土地信息查询
    def test_getTdxx001(self):
        i = isFuncNameExistsList("test_getTdxx001")
        #caselist中第一行是index 0
        if i or i== 0:
            logger.debug("该接口在list中下标是：%d" %i)
            self.apiName = caselist[i][3]
            self.url = caselist[i][6]
            self.method = caselist[i][5]
            self.headers = caselist[i][7]
            self.data = caselist[i][8]
            self.expectRes = caselist[i][9]
            actualRes = APITest(self.url, self.method, self.headers, self.data).testApi()
            logger.debug("%s接口响应信息为:%s" %(self.apiName,actualRes))  #tuple
            self.assertIn(self.expectRes,actualRes[1])
        else:
            logger.error("%s接口不存在List中" %self.apiName)

    #抵押信息查询
    def test_getDyxx001(self):
        i = isFuncNameExistsList("test_getDyxx001")
        if i or i == 0:
            logger.debug("接口在list中下标是：%d" % i)
            self.apiName = caselist[i][3]
            self.url = caselist[i][6]
            self.method = caselist[i][5]
            self.headers = caselist[i][7]
            self.data = caselist[i][8]
            self.expectRes = caselist[i][9]
            actualRes = APITest(self.url, self.method, self.headers, self.data).testApi()
            logger.debug("%s接口响应信息为:%s" %(self.apiName,actualRes))  # tuple
            self.assertIn(self.expectRes, actualRes[1])
        else:
            logger.error("%s接口不存在List中" %self.apiName)

    #预告信息查询（商品房）
    def test_getYgxx001(self):
        i = isFuncNameExistsList("test_getYgxx001")
        if i or i == 0:
            logger.debug("该接口在list中下标是：%d" % i)
            self.apiName = caselist[i][3]
            self.url = caselist[i][6]
            self.method = caselist[i][5]
            self.headers = caselist[i][7]
            self.data = caselist[i][8]
            self.expectRes = caselist[i][9]
            actualRes = APITest(self.url, self.method, self.headers, self.data).testApi()
            logger.debug("%s接口响应信息为:%s" %(self.apiName,actualRes))  # tuple
            self.assertIn(self.expectRes, actualRes[1])
        else:
            logger.error("%s接口不存在List中" %self.apiName)

    # 预告信息查询（存量）
    def test_getYgxx002(self):
        i = isFuncNameExistsList("test_getYgxx002")
        if i or i == 0:
            logger.debug("该接口在list中下标是：%d"  % i)
            self.apiName = caselist[i][3]
            self.url = caselist[i][6]
            self.method = caselist[i][5]
            self.headers = caselist[i][7]
            self.data = caselist[i][8]
            self.expectRes = caselist[i][9]
            actualRes = APITest(self.url, self.method, self.headers, self.data).testApi()
            logger.debug("%s接口响应信息为:%s" %(self.apiName,actualRes))  # tuple
            self.assertIn(self.expectRes, actualRes[1])
        else:
            logger.error("%s接口不存在List中" %self.apiName)

    def tearDown(self):
        pass
