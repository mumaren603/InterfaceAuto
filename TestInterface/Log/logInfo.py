import logging
import datetime
# from conf import readConfig

#获取配置文件中定义的log日志路径
# def logPath():
#     confFilePath = readConfig.confFilePath()
#     print(confFilePath)
#     # logPath = readConfig.readConf(confFilePath).getLog()
#     # print(logPath)
#     return logPath
# # logPath()

#获取当前年月日，并以年月日作为日志存放目录名
def Foo():
    currentYear = datetime.datetime.now().year
    currentMonth =datetime.datetime.now().month
    currentDay = datetime.datetime.now().day

    if currentMonth < 10:
        currentMonth="0"+str(currentMonth)
        DirName = str(currentYear)+currentMonth+str(currentDay)
    else:
        DirName = str(currentYear) + str(currentMonth) + str(currentDay)
    return DirName
Foo()



class Logger():
    def __init__(self,logLevel):
        #创建一个Logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        # self.logFormat = logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #创建一个handler,用于输出到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        # 创建一个handler,用于将日志写入文件
        file_handler = logging.FileHandler("test.log",mode='a',encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        #定义handler的输出格式
        log_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #设置handler输出格式
        stream_handler.setFormatter(log_format)
        file_handler.setFormatter(log_format)

        #给logger添加handler
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    def getLog(self):
        return self.logger

