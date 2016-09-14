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

headers = {'content-type': 'application/json'}

API_KEY = "c791e11-d9ab779"
url = 'http://localhost:8000/api/v1/datas/' + API_KEY

auth=('iottestuser', 'iot12345**')

datas = urllib.urlencode({"name_id":"test", "value":"45", })

conn = httplib.HTTPConnection("localhost", 8000)
conn.request("POST", "/api/v1/datas/" + API_KEY, datas, headers)

response = conn.getresponse()

print response.status, response.reason

print response.read()

