#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''This is a module for uploading app to pgyer.com.
	You should config your uKey,_api_key,app_name before use.
'''

__author__ = 'Johnny Copper'

import requests
import time

url = "http://www.pgyer.com/apiv1/app/upload"
update_url = "http://www.pgyer.com/apiv1/app/update"
uKey = "xxxxx"
_api_key = "xxxxx"

app_base_name = "安邦物业app"
update_file_name = "每日bug.txt"
upload_file_name = "app.apk"

def _read_text(s):
	file = open(s)
	string = file.read()
	file.close()
	return string

# upload to pgy
def upload_to_pgy(update_file_name, upload_file_name):
	
	files = {'file': open(upload_file_name, 'rb')}

	payload = {"_api_key":_api_key, "uKey":uKey}

	upload_request = requests.post(url, data=payload, files=files)

	return upload_request.json()

# update app name
def update_app_in_pgy(appKey, appName, updateDescription):

	payload = {"_api_key":_api_key, "uKey":uKey, "aKey":appKey, "appName":appName, "appUpdateDescription":updateDescription}

	update_request = requests.post(update_url, data=payload)
	
	return update_request.json()

# upload to pgy then update the app name and its update description
def upload_then_update_to_pgy_using_default_config(app_base_name, update_file_name, upload_file_name):

	response = upload_to_pgy(update_file_name, upload_file_name)
	appKey = response['data']['appKey']
	app_name = app_base_name + time.strftime("%Y%m%d", time.localtime())
	updateDescription = _read_text(update_file_name)

	response = update_app_in_pgy(appKey,app_name,updateDescription)
	print(response)
	return response

def main():
	upload_then_update_to_pgy_using_default_config(app_base_name, update_file_name, upload_file_name)
	pass

if __name__ == '__main__':
	main()
	
