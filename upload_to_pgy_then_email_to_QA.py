#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''This is a module for daily build and email QA.
	You should config your from_addr,password,to_addr before use.
'''

__author__ = 'Johnny Copper'

import daily_email_to_QA
import upload_to_pgy

app_base_name = "安邦物业app"
update_file_name = "每日bug.txt"
upload_file_name = "app.apk"

def main():

	response = upload_to_pgy.upload_then_update_to_pgy_using_default_config(app_base_name, update_file_name, upload_file_name)
	app_name = response['data']['appName']
	app_addr = 'https://www.pgyer.com/' + response['data']['appShortcutUrl']
	app_update_info = response['data']['appUpdateDescription']

	daily_email_to_QA.send(app_name,app_addr,app_update_info)
	pass

if __name__ == '__main__':
	main()