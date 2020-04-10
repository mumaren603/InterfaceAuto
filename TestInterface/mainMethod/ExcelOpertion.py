#Author: ls Liu

import xlrd
from mainMethod.readConfig import readConf
from LogConf.loggerConf import loggerConf

logger = loggerConf().getLog()

class excelTest(object):
    def __init__(self,excelpath):
        self.excelpath = excelpath

    #读取Excel测试用例路径，保存到list[caselist]中
    def readExcel(self):
        openExcel = xlrd.open_workbook(self.excelpath)
        logger.debug("表格sheet页为：%s" %openExcel.sheet_names())

        sheetContent= openExcel.sheet_by_index(0)
        rowsNum = sheetContent.nrows
        logger.debug("表格中读取到行数为：%s" %rowsNum)

        caseList= []
        for row in range(rowsNum):
            if row:
                caseList.append(sheetContent.row_values(row))
        return caseList

    def writeExcel(self):
        pass



