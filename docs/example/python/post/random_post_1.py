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

API_KEY = "c791e11-d9ab779"
url = 'http://localhost:8000/api/v1/datas/' + API_KEY
auth=('iottestuser', 'iot12345**')

for i in range(30):
	data = {"name_id":"test", "value":i}

	data_json = json.dumps(data)
	headers = {'Content-type': 'application/json'}

	response = requests.post(url, data=data_json, headers=headers, auth=auth)
	pprint.pprint(response.json())

