# smtp.exmail.qq.com
# -*- coding: UTF-8 -*-

import smtplib
import codecs
import time
import sys
from email.utils import formataddr
from email.mime.text import MIMEText

sender = 'tangqingchang@julanling.com'  # 发件人邮箱账号
password = sys.argv[1]  # 发件人邮箱密码

file = codecs.open('./conf/mail_to.txt', encoding='utf-8')
data = file.read().strip()
array = data.split('\r\n')

to = []
users = []

for string in array:
    arr = string.split("=")
    to.append(formataddr(arr))
    users.append(arr[1])

to = ";".join(to)

smtp = 'smtp.exmail.qq.com'
port = 465


def from_file(path):
    file = codecs.open(path, encoding='utf-8')
    data = file.read()
    file.close()
    return data


def mail(sub, content):
    result = True
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = sender  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = to  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = sub  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL(smtp, port)  # 发件人邮箱中的SMTP服务器、端口
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(sender, users, msg.as_string())
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 result=False

        print(e)
        result = False
    return result


my_name = '唐庆昌'
dir = 'diary'

month = int(time.strftime("%m"))
day = int(time.strftime("%d"))
year = int(time.strftime("%Y"))
file_base_name = "{y}年{m}月{d}-{n}.txt".format(y=year, m=month, d=day, n=my_name)

path = dir + '/' + file_base_name

subject = "{m}月{d}实习生工作日报-{n}".format(m=month, d=day, n=my_name)

ret = mail(subject, from_file(path))
if ret is True:
    print("send success")
else:
    print("send failed")
