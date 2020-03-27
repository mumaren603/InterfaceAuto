#Author: ls Liu
from email.mime.text import MIMEText
from email.utils import formataddr
from Opertion import readConfig
import smtplib


#定义发件人，接收人信息
sender_account = '13338625696@163.com'    #发送者邮箱账号
sender_passwd = 'shan603'                   #发送者邮箱授权码，注意这里不是邮箱登录密码
receiver_users = readConfig.readConf().getEmailInfo()    #收件人邮箱账号
# print("收件人包括：%s" %receiver_users,type(receiver_users))

# portPath='F:\python_s14\TestInterface\Report\Report_20200320_145518.html'
# print("自定义路径：%s"%portPath,type(portPath))

def send_email(new_report):
    # 读取最新的测试报告内容
    print("传参路径：%s" %new_report,type(new_report))
    with open(new_report,'rb') as f:
        new_TestReport = f.read()
        print(new_TestReport)

    #定义第三方SMTP服务一些参数
    msg = MIMEText(new_TestReport, 'html', 'utf-8')

    msg['Subject'] = "接口自动化测试报告"             #邮件主题
    msg['From'] = formataddr(["liulinshan",sender_account])    # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    for i in range(len(receiver_users)):
        msg['To'] = formataddr(["leader",receiver_users[i]])       # 括号里的对应收件人邮箱昵称、收件人邮箱账号

    try:
        server = smtplib.SMTP_SSL("smtp.163.com",465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(sender_account,sender_passwd)   # 括号中对应的是发件人邮箱账号、授权码
        server.sendmail(sender_account,receiver_users,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")
    except Exception as e:
        print(e)
        print("Error:无法发送邮件")



# send_email(portPath)