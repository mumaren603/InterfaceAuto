#Author: ls Liu
import unittest
from lib import HTMLTestRunner
from mainMethod.readConfig import readConf
from time import strftime
from LogConf.loggerConf import loggerConf
from Common import getLatestReport
from Email import sendEmail

logger = loggerConf().getLog()

if __name__ == '__main__':
    # 设置待执行用例的目录
    testCasePath = readConf().getTestCasePath()

    # 定义测试报告路径格式
    testReportPath = readConf().getTestReportPath()
    file_name = '\Report_' + strftime('%Y%m%d_%H%M%S') + '.html'
    testReportName = testReportPath+file_name
    logger.debug("生成的测试报告全路径为：%s" %testReportName)

    #用例执行
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testCasePath,pattern="case*.py")

    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)

    #生成报告
    fp = open(testReportName,'wb')
    runner= HTMLTestRunner.HTMLTestRunner(
                                          stream=fp,
                                          title=u'接口测试报告',
                                          description=u'详细执行情况请查看服务器执行日志。'
                                            )
    runner.run(testunit)
    fp.close()

    #调用邮件服务，发送邮件
    new_report_mail = getLatestReport.latest_report(testReportPath)
    logger.debug("最新报告为：%s" %new_report_mail)
    sendEmail.send_email(new_report_mail)












