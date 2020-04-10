#Author: ls Liu
import os

def latest_report(report_path):
    report_list = os.listdir(report_path)  #获取该目录下所有测试报告
    latest_report =os.path.join(report_path,report_list[-1])  #取最新的报告
    return latest_report

