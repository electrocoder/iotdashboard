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

import httplib, urllib

# headers = {'content-type': 'application/json'}
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "application/json"}

API_KEY = "0cd76eb-5f3b179"
url = 'http://localhost:8000/api/v1/data/' + API_KEY

datas = urllib.urlencode({"username":"iottestuser", "password":"iot12345**", "name_id":"test", "value":"45", })
# datas = urllib.urlencode({"iottestuser":"iot12345**", "name_id":"test", "value":"45", })

conn = httplib.HTTPConnection("localhost", 8000)
conn.request("POST", "/api/v1/data/" + API_KEY, datas, headers)

response = conn.getresponse()

print response.status, response.reason

print response.read()

