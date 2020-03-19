#Author: ls Liu
import unittest
from Opertion import interfaceTest
from Opertion import readConfig
from Opertion import ExcelOpertion

filePath = readConfig.readConf().getExcelInfo()
caselist = ExcelOpertion.excelTest(filePath).readExcel()


class azqdController(unittest.TestCase):
    def setUp(self):
        pass

    def test_getAzqdById(self):
        self.url = caselist[2][6]
        self.method = caselist[2][5]
        self.headers = caselist[2][7]
        self.data = caselist[2][8]

        interfaceTest.APITest2(self.url, self.method, self.headers, self.data).testApi()

    def test_getAzqdById2(self):
        self.url = caselist[2][6]
        self.method = caselist[2][5]
        self.headers = caselist[2][7]
        self.data = caselist[2][8]

        interfaceTest.APITest2(self.url, self.method, self.headers, self.data).testApi()

    def test_getAzqdById3(self):
        self.url = caselist[2][6]
        self.method = caselist[2][5]
        self.headers = caselist[2][7]
        self.data = caselist[2][8]

        interfaceTest.APITest2(self.url, self.method, self.headers, self.data).testApi()

    def tearDown(self):
        pass