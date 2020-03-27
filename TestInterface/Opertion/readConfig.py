#Author: ls Liu
import os
import configparser
from common import  commFunc

class readConf(object):
    def __init__(self,conf=None):
        self.conf = conf
        self.conf = configparser.ConfigParser()       #初始化实例 configparser用于操作配置文件
        self.conf.read(self.getConfPath(), encoding='utf-8')  # 读取配置文件
        # return self.conf

    #获得conf配置文件路径
    def getConfPath(self):
        currentFileDir = os.path.realpath(__file__)  # 获取当前py所在绝对路径
        # print("当前py文件路径为："+currentFileDir)
        fileParPath = os.path.dirname(os.path.dirname(currentFileDir))  # 获取当前py所在的父目录（不包括当前文件）
        # print("当前py文件父目录为："+fileParPath)
        configPath = os.path.join(fileParPath, "conf\conf.ini")
        # print("配置文件路径为："+configPath)
        return configPath

    def getHttpInfo(self):
        s = self.conf.sections()         # 获取所有sections,列表返回
        #print(type(s), s)          #<class 'list'> ['HTTP', 'EXCEL', 'LOG', 'DATABASE', 'EMAIL']
        o = self.conf.options("HTTP")   # 获取指定section 的options，列表返回
        #print(o)                   #['ip', 'port1', 'port2']
        httpInfo = self.conf.items("HTTP")  # 获取指定section 的配置信息  会把sections下k-v输出
        #print(httpInfo)            #[('ip', '172.0.0.103'), ('port1', '1100'), ('port2', '1103')]
        IP = httpInfo[0][1]         # 获取服务器IP
        #print(type(IP), IP)
        PORT = httpInfo[1][1]      # 获取登记系统后端端口号
        #print(PORT)

        reqURL = 'http://' + IP + ':' + PORT
        #print(reqURL)
        return reqURL

    def getExcelInfo(self):
        try:
            e = self.conf.items("EXCEL")  # 获取指定section 的配置信息  会把sections下k-v输出
            filePath = e[0][1]              # 获取测试用例路径
            #logger.info("测试用例路径为：%s", filePath)
            #print(type(filePath), filePath)
        except Exception as e:
            print(e)
        finally:
            return filePath

    def getEmailInfo(self):
        try:
            e = self.conf.items("EMAIL")
            senderAccount = e[0][1]
            # print(senderAccount, type(senderAccount))
            senderPasswd = e[1][1]
            # print(senderPasswd, type(senderPasswd))
            receiverUser = e[2][1]     #str
            receiverUser = commFunc.strToList(receiverUser)  #list
            # print (receiverUser,type(receiverUser))
        except Exception as e:
            print(e)
        finally:
            return  receiverUser

    def getDbInfo(self):
        pass

    def getTestReportPath(self):
        try:
            e =self.conf.items("Report")
            testReportPath = e[0][1]
        except Exception as e:
            print(e)
        finally:
            return testReportPath



# readConf().readConf()
# readConf().getHttpInfo()
# readConf().getEXCEL()
readConf().getEmailInfo()


