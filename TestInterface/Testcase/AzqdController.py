#Author: ls Liu

import unittest
from mainMethod import interfaceTest
from Common import getCaselistInfo


class azqdController(unittest.TestCase):
    def setUp(self):
        pass

    def test_getAzqdById001(self):
        i = getCaselistInfo.isFuncNameExistsList("test_getAzqdById001")
        if i:
            # print("该接口在list中第%d是行"%i)
            self.url = getCaselistInfo.caselist[i][6]
            self.method = getCaselistInfo.caselist[i][5]
            self.headers = getCaselistInfo.caselist[i][7]
            self.data = getCaselistInfo.caselist[i][8]
            interfaceTest.APITest2(self.url, self.method, self.headers, self.data).testApi()
        else:
            pass
            # print("接口不存在List中")

    def test_getDaglHxx001(self):
        i = getCaselistInfo.isFuncNameExistsList("test_getDaglHxx001")
        if i:
            self.url = getCaselistInfo.caselist[i][6]
            self.method = getCaselistInfo.caselist[i][5]
            self.headers = getCaselistInfo.caselist[i][7]
            self.data = getCaselistInfo.caselist[i][8]
            interfaceTest.APITest2(self.url, self.method, self.headers, self.data).testApi()

    def test_getCfQlrxx001(self):
        i = getCaselistInfo.isFuncNameExistsList("test_getCfQlrxx001")
        if i:
            self.url = getCaselistInfo.caselist[i][6]
            self.method = getCaselistInfo.caselist[i][5]
            self.headers = getCaselistInfo.caselist[i][7]
            self.data = getCaselistInfo.caselist[i][8]

        interfaceTest.APITest2(self.url, self.method, self.headers, self.data).testApi()

    def tearDown(self):
        pass

