import logging
from datetime import datetime
import threading,os
from tableOpertion import tableExecute

def logPath():
    aa = os.path.realpath(__file__)
    parPath=os.path.dirname(os.path.dirname(aa))
    print(parPath)
    currentTime = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    resultExcelName = '测试结果'+currentTime
    logPath = os.path.join(parPath,resultExcelName)
    print(logPath)
logPath()

class Log(object):
    def __init__(self,logLevel):
        self.logLevel = logLevel
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler('log.txt',mode='a')
    file_handler.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    self.logger.addHandler(file_handler)
    self.logger.addHandler(stream_handler)