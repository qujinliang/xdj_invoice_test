import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

test_dir = './report'


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    subject = '接口自动化测试报告'
    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename = "TestReport.html"'
    msg.attach(msg_html)

    msg['Subject'] = Header(subject,'utf-8')
    msg['from'] = 'qujinliang@uknower.com'


    smtp = smtplib.SMTP_SSL()
    smtp.connect("smtp.exmail.qq.com")
    smtp.login("qujinliang@uknower.com", "JEDnX7EXn6da6LZx")
    smtp.sendmail("qujinliang@uknower.com", "qujinliang@uknower.com", msg.as_string())

    smtp.quit()
    print('email has send out !')


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    file_path = new_report('./report')
    send_mail(file_path)