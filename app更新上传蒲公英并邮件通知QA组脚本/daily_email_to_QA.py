#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''This is a module for sending email to QA group.
	You should config your from_addr,password,to_addr before use.
'''

__author__ = 'Johnny Copper'

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
import time

from_addr = 'a@ycode.cn'
password = 'password'
to_addr = ['zq@ycode.cn','b@ycode.cn']
smtp_server = 'smtp.exmail.qq.com'

app_name = '安邦app' + time.strftime("%Y%m%d", time.localtime())
app_address = 'http://www.pgyer.com/xxxx'
update_file_name = '每日bug.txt'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def _read_text(s):
	file = open(s)
	string = file.read()
	file.close()
	return string

def send(app_name, app_address, update_info):
	subject = app_name
	install_address = ('安装地址：%s\n' % app_address)
	update_info = '更新说明：\n' + update_info

	body = install_address + update_info
	msg = MIMEText(body, 'plain', 'utf-8')
	msg['From'] = _format_addr('云极客活雷锋 <%s>' % from_addr)
	msg['To'] = _format_addr('QA <%s>' % ','.join(to_addr))
	msg['Subject'] = Header(subject, 'utf-8').encode()

	server = smtplib.SMTP(smtp_server, 25)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, to_addr, msg.as_string())
	server.quit()
	pass

def main():
	send(app_name, app_address, _read_text(update_file_name))
	pass

if __name__ == '__main__':
	main()

	
