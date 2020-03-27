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
    # 定义测试报告路径、格式
    file_name = '\Report_' + strftime('%Y%m%d_%H%M%S') + '.html'
    testReportPath = readConfig.readConf().getTestReportPath()
    print("测试报告所在目录为：%s" %testReportPath)
    testReportName = testReportPath+file_name
    print("生成的测试报告全路径为：%s" %testReportName,type(testReportName))

    fp = open(testReportName,'wb')
    suite = unittest.makeSuite(testAzqdController.azqdController)
    runner=HTMLTestRunner.HTMLTestRunner(fp,title=u'AzqdController_Report',description=u'This is a report test')
    runner.run(suite)

    new_report_mail = getLatestReport.latest_report(testReportPath)
    print("发送路径：%s" %new_report_mail,type(new_report_mail))
    # new_report_mail2="F:\python_s14\TestInterface\Report\Report_20200323_112011.html"
    # print("打印路径：%s" %new_report_mail2)
    sendEmail.send_email(new_report_mail)
    # sendEmail.send_email(new_report_mail2)

    fp.close()

'''
遗留问题
1、当用例分步在多个模块时  执行没有问题 生成报告存在问题
2、如果用例很多，如何并行执行用例呢，提高效率 ？
'''

