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

API_KEY = "b3d7c6b-fe8beb1"
url = 'http://localhost:8000/api/v1/datas/' + API_KEY
auth=('iottestuser', 'iot12345**')

for i in range(2):
	data = {"name_id":"a", "value":i}

	data_json = json.dumps(data)
	headers = {'Content-type': 'application/json'}

	response = requests.post(url, data=data_json, headers=headers, auth=auth)
	pprint.pprint(response.json())

