#Author: ls Liu
import json
def strToDict(str):
    dictRes = json.loads(str)
    return dictRes

def strToList(str):
    listRes = str.split(",")
    return listRes