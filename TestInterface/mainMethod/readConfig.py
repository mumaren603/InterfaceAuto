#Author: ls Liu
import os
import configparser
from Common.dataTypeTransformation import strToList
from LogConf.loggerConf import loggerConf

logger = loggerConf().getLog()

class readConf():
    def __init__(self,conf=None):
        self.conf = conf
        self.conf = configparser.ConfigParser()       #初始化实例 configparser用于操作配置文件
        self.conf.read(self.getConfPath(), encoding='utf-8')  # 读取配置文件

    #获取配置文件
    def getConfPath(self):
        # 获取当前py所在绝对路径
        currentFileDir = os.path.realpath(__file__)

        #获取当前py所在的父目录（不包括当前文件）
        fileParPath = os.path.dirname(os.path.dirname(currentFileDir))
        configPath = os.path.join(fileParPath, "conf\conf.ini")
        return configPath

    #获取服务器主机和端口号
    def getServicesInfo(self):
        try:
            # conf_sections = self.conf.sections()
            # logger.debug("配置文件配置项为：%s" % conf_sections)
            #
            # conf_options_SERVICES = self.conf.options("SERVICES")
            # logger.debug("HTTP配置项小类为：%s" % conf_options_SERVICES)

            conf_items_SERVICES = self.conf.items("SERVICES")
            logger.debug("服务配置项小类详细信息：%s" % conf_items_SERVICES)

            server_SCHEMA = conf_items_SERVICES[0][1]
            logger.debug("服务协议为：%s" % server_SCHEMA)

            server_IP = conf_items_SERVICES[1][1]
            logger.debug("服务IP为：%s" % server_IP)

            server_PORT = conf_items_SERVICES[2][1]
            logger.debug("服务端口为：%s" % server_PORT)

            reqURL = server_SCHEMA+ '://' + server_IP + ':' + server_PORT
            logger.info("请求URL为：%s" % reqURL)
            return reqURL
        except Exception as e:
            logger.error("测路服务配置信息异常",e)

    #获取接口数据存放文件路径（excel）
    def getExcelInfo(self):
        try:
            conf_items_EXCEL = self.conf.items("EXCEL")
            excelPath = conf_items_EXCEL[0][1]
            logger.info("接口数据Excel路径为：%s" % excelPath)
            return  excelPath
        except Exception as e:
            logger.error("接口数据路径异常",e)

    #获取邮件服务信息
    def getEmailInfo(self):
        try:
            conf_items_EMAIL = self.conf.items("EMAIL")
            senderAccount = conf_items_EMAIL[0][1]
            senderPasswd = conf_items_EMAIL[1][1]
            receiverUser = conf_items_EMAIL[2][1]             #str
            receiverUser = strToList(receiverUser)   #转化为list
            logger.info("邮件发件人为：%s,邮件接受人为：%s" %(senderAccount,receiverUser))
            return senderAccount, senderPasswd, receiverUser
        except Exception as e:
            logger.error("邮件初始化异常",e)

    #获取测试报告路径
    def getTestReportPath(self):
        try:
            conf_items_REPORT =self.conf.items("REPORT")
            testReportPath = conf_items_REPORT[0][1]
            logger.info("测试报告路径为：%s" % testReportPath)
            return testReportPath
        except Exception as e:
            logger.error("测试报告配置异常",e)

    #获取日志存放路径（bug）
    def getLogPath(self):
        try:
            conf_items_LOG =self.conf.items("LOG")
            logPath = conf_items_LOG[0][1]
            logger.info("测试日志路径为：%s" % logPath)
            return logPath
        except Exception as e:
            logger.error("测试日志配置异常", e)

    #获取测试用例路径
    def getTestCasePath(self):
        try:
            conf_items_TESTCASE =self.conf.items("TESTCASE")
            testCasePath = conf_items_TESTCASE[0][1]
            logger.info("测试用例路径为：%s" % testCasePath)
            return testCasePath
        except Exception as e:
            logger.error("测试用例路径配置异常", e)

    def getDbInfo(self):
        pass


#调试
# readConf().getServicesInfo()

