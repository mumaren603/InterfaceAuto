#Author: ls Liu
import unittest
from TestReport import HTMLTestRunner
# from Opertion import interfaceTest
from Opertion import readConfig
from time import strftime
from Testcase import testAzqdController
from common import getLatestReport
from Email import sendEmail

if __name__=='__main__':
    # suite=unittest.makeSuite(interfaceTest.apiTest)
    # 定义测试报告路径、格式
    file_name = '.\Report_' + strftime('%Y%m%d_%H%M%S') + '.html'
    testReportPath = readConfig.readConf().getTestReportPath()
    testReportName = testReportPath+file_name
    print(testReportName)

    fp = open(testReportName,'wb')
    suite = unittest.makeSuite(testAzqdController.azqdController)
    runner=HTMLTestRunner.HTMLTestRunner(fp,title=u'AzqdController_Report',description=u'This is a report test')
    runner.run(suite)

    new_report_mail = getLatestReport.latest_report(testReportPath)
    sendEmail.send_email(new_report_mail)

    fp.close()

'''
遗留问题
当用例分步在多个模块时  执行没有问题 生成报告存在问题
'''




