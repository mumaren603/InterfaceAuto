#Author: ls Liu
import xlrd
import requests
import json
filePath = "F:\python s14\InterfaceSuits\测试用例.xlsx"
case_list=[]
def readExcel(filePath):
    try:
        book = xlrd.open_workbook(filePath)
        print(book.sheet_names())
    except Exception as e:
        print("Excel文件不存在或者路径不正确！")
        return e
    else:
        sheet = book.sheet_by_index(0)  #获取第一个sheet页
        rows = sheet.nrows      #取这个sheet页所有行数(有记录行数，不统计空白行)
        print(rows)             #3
        #case_list = []         #列表 用来保存每一条case
        for i in range(rows): #3
            if i:
                case_list.append(sheet.row_values(i))


testRes = []
def eachTestCase(case_list):
    for case in case_list:
        print("请求信息")
        print(case)
        try:
            request_method = "".join(case[4])   #将元祖转换为字符串
            print("==========================")
            #print(type(request_method),request_method)
            request_url = case[5]               #请求URL
            http ="http://172.0.0.103:1100"
            request_url = http+request_url
            request_headers = case[6]           #请求头
            request_params = case[7]            #请求报文
            if request_headers:
                request_headers = strToDict(case[6])
            print(type(request_headers),request_headers)
            print(type(request_params),request_params)
            # request_headers = strToDict(case[6])
            # print(type(request_headers), request_headers)
            # print(type(request_params), request_params)
            exceptRes = case[10]               #预期结果
            print(type(case[10]),case[10])
        except Exception as e:
            print('测试用例格式不正确！%s' %e)
        if request_method.upper() == 'GET':
            print(request_method,request_url,request_headers,request_params)
            getResponse = requests.get(url=request_url,headers=request_headers,params=request_params)
            print(getResponse.text)
        elif request_method.upper() == 'POST':
            request_url='http://172.0.0.103:1103/public/bdcxx/fwzkxx'
            print(request_method,request_url, request_headers,request_params)
            postResponse = requests.post(url=request_url, headers=request_headers, data=request_params)
            print(postResponse.text)
        else:
            print("illigal opertion")

def strToDict(str):
    dictRes = json.loads(str)
    return dictRes


readExcel(filePath)
eachTestCase(case_list)

from xlutils import copy
import time
def copy_excel(filePath):
    #打开要读的xls
    book = xlrd.open_workbook(filePath)
    #复制为新的xls
    new_book = copy.copy(book)
    #获取新xls的sheet1
    sheet = new_book.get_sheet(0)
    #写入数据
    sheet.write(1,1,'22')
    sheet.write(1,2, '对外查询')
    #保存数据
    new_book.save('%s_测试结果.xls'%time.strftime('%Y%m%d%H%M%S'))

#copy_excel(filePath)