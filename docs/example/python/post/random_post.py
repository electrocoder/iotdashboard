# -*- coding: utf-8 -*-
"""
Iot dashboard POST example

iot-dashboard
IoT: Platform for Internet of Things

Iotdashboard source code is available under the MIT License

Online iot dashboard test and demo http://ihook.xyz

Online iot dashboard https://iothook.com

You can find project details on our project page https://iothook.com and wiki https://iothook.com
"""

import requests
import json
import urllib
import urllib2
import random
import pprint

import time

url = 'http://localhost:8000/api/v1/datas/'

auth=('admin', 'Aa1234567890')

for i in range(30):
	data = {'api_key': '311b9c68f7e64bdfb77aab1e4d53aaf04378a463',
			 'element_id_1': 'a', 'value_1': 10,
			 'element_id_2': 'b', 'value_2': 20}

	data_json = json.dumps(data)
	headers = {'Content-type': 'application/json'}

	response = requests.post(url, data=data_json, headers=headers, auth=auth)
	pprint.pprint(response.json())
	time.sleep(5)

