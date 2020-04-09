#Author: ls Liu
'''
测试用例信息（接口url,method,params,headers）等 我们是一次性读取到caselist<list>中 ，但是我们在写测试用例时，如何知道我写的接口
和caselist里那一行对应呢？
通过接口名（即每一个测试用例函数名）与caselist中逐一匹配，匹配到即知道该接口对应信息在列表中位置，从而获取该接口请求详细信息。
'''

from mainMethod.readConfig import readConf
from mainMethod.ExcelOpertion import excelTest

#获取Excel中所有case信息
caselist =  excelTest(readConf().getExcelInfo()).readExcel()

#str接受函数名（即每个测试用例方法）
def isFuncNameExistsList(str):
    for i in range(len(caselist)):
        for j in range(len(caselist[i])):
            if caselist[i][j] == str:
                return i




