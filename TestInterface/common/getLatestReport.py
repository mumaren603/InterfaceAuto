#Author: ls Liu
import os

def latest_report(report_path):
    report_list = os.listdir(report_path)  #列出所有测试报告
    latest_report =os.path.join(report_path,report_list[-1])
    return latest_report

