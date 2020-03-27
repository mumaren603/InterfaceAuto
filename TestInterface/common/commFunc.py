#Author: ls Liu
import json

#字符串转字典
def strToDict(str):
    dictRes = json.loads(str)
    return dictRes

#字符串转列表，主要用于邮箱收件人操作
def strToList(str):
    listRes = str.split(",")
    return listRes
