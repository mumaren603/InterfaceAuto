#Author: ls Liu
import os

def latest_report(report_path):
    report_list = os.listdir(report_path)  #列出所有测试报告
    print("目录下所有测试报告：%s" %report_path)
    latest_report =os.path.join(report_path,report_list[-1])
    print("最新的测试报告为：%s" %latest_report)
    return latest_report

