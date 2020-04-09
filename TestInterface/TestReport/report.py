#Author: ls Liu
import unittest
from lib import HTMLTestRunner
from mainMethod.readConfig import readConf
from time import strftime
from Testcase.testOutQuery import testOutQuery
from Common import getLatestReport
from Email import sendEmail
from LogConf.loggerConf import loggerConf

logger = loggerConf().getLog()

def raiseTestReport():
    # 定义测试报告路径、格式
    file_name = '\Report_' + strftime('%Y%m%d_%H%M%S') + '.html'
    testReportPath = readConf().getTestReportPath()
    logger.debug("测试报告所在目录为：%s" %testReportPath)
    testReportName = testReportPath+file_name
    logger.debug("生成的测试报告全路径为：%s" %testReportName)

    #生成报告
    fp = open(testReportName,'wb')
    suite = unittest.makeSuite(testOutQuery)
    runner= HTMLTestRunner.HTMLTestRunner(fp, title=u'OutQuery_Report', description=u'This is a report test')
    runner.run(suite)
    fp.close()

    #调用邮件服务，发送邮件
    new_report_mail = getLatestReport.latest_report(testReportPath)
    logger.debug("最新报告为：%s" %new_report_mail)
    sendEmail.send_email(new_report_mail)


'''
遗留问题
1、当用例分步在多个模块时  执行没有问题 生成报告存在问题
2、如果用例很多，如何并行执行用例呢，提高效率 ？
'''

