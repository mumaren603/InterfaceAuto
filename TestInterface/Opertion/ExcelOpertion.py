#Author: ls Liu
import xlrd
from Opertion import readConfig

filePath = readConfig.readConf().getExcelInfo()

class excelTest(object):
    def __init__(self,filePath):
        self.filePath = filePath

    def readExcel(self):
        openExcel = xlrd.open_workbook(self.filePath)
        print("表格sheet页：%s" %openExcel.sheet_names())
        sheetContent= openExcel.sheet_by_index(0)        #获取第一个sheet页
        print("sheet1:",sheetContent)
        rowsNum = sheetContent.nrows
        print("表格中行数为：%s" %rowsNum)
        caseList= []
        for row in range(rowsNum):
            if row:
                print("这是第%s行", row)
                caseList.append(sheetContent.row_values(row))
        # print(caseList)
        return caseList

    def writeExcel(self):
        pass


excelTest(readConfig.readConf().getExcelInfo()).readExcel()