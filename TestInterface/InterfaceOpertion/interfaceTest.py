#Author: ls Liu
import requests
from tableOpertion import tableExecute
from Opertion import readConfig
from common import commFunc   #有问题需修改
from Log import logInfo

#实例化logger对象
logger = logInfo.Logger('DEBUG').getLog()

def getCaselist():
    global  caselist
    try:
        filePath = tableExecute.getCasesuitPath()
        logger.info("测试用例路径为：%s", filePath)
        # print(filePath)
        caselist = tableExecute.Table(filePath).readExcel()
        logger.info("测试用例内容为：%s", caselist)
        # print(caselist)
        return caselist
    except Exception as e:
        print(e)
case = getCaselist()

def getHttp():
    confFile = readConfig.getConf()
    readConfig.readConf(confFile).readHttpConf
    httpInfo = readConfig.readConf(confFile).getHTTP()
    print(httpInfo)
    logger.info("请求URL为：%s", httpInfo)
    return httpInfo

httpInfo = getHttp()

class interfaceTest():
    for i in range(len(case)):
        # print(i)
        logger.info("这是第%s个用例", i)
        request_model = case[i][1]            #请求模块
        request_method = case[i][4]           #请求方法
        print(type(request_method),request_method)
        request_url = case[i][5]              #方法URL
        if request_model == "登记平台":
            request_url = httpInfo[0]+request_url
            print(type(request_url), request_url)
        elif request_model == "登记簿":
            request_url = httpInfo[1]+request_url
            print(type(request_url), request_url)
        else:
            print("测试用例表格模块没有，程序终止！")
            break
        request_headers = case[i][6]
        print(type(request_headers), request_headers)
        request_params = case[i][7]
        print(type(request_params), request_params)
        if request_headers:
            request_headers = commFunc.strToDict(request_headers)
        print(type(request_headers), request_headers)
        if request_method.upper() == 'GET':
            getResponse = requests.get(url=request_url,headers=request_headers,params=request_params)
            print(getResponse.text)
        elif request_method.upper() == 'POST':
            postResponse = requests.post(url=request_url,headers=request_headers,data=request_params)
            print(postResponse.text)
        else:
            print("请求的方式不正确")

aa = interfaceTest()

