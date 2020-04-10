#Author: ls Liu
import logging
import os
from time import strftime

class loggerConf():
    def __init__(self):
        #创建一个Logger
        logger = self.logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)               #设置总日志级别

        if not logger.handlers:
            #创建一个handler,用于输出到控制台
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)    #设置控制台输出日志级别

            # 定义handler的输出格式
            log_format = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

            #定义file_handler信息
            logFileDir = 'F:\python_s14\TestInterface\Result\log'
            if not os.path.isdir(logFileDir):
                logger.debug("日志文件夹 %s 不存在!" % logFileDir)
            else:
                logger.debug("日志文件夹 %s 存在!" % logFileDir)
            logFile = '\TestInterface_'+ strftime('%Y%m%d_%H%M%S') + '.log'
            logFileDir = logFileDir+logFile
            #创建一个handler,用于将日志写入文件
            file_handler = logging.FileHandler(logFileDir,mode='a',encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)    #设置文件输出日志级别

            #设置handler输出格式
            stream_handler.setFormatter(log_format)
            file_handler.setFormatter(log_format)

            #给logger添加handler
            logger.addHandler(stream_handler)
            logger.addHandler(file_handler)

    def getLog(self):
        return self.logger
