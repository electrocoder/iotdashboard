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
import httplib, urllib

API_KEY = "0cd76eb-5f3b179"

url = 'http://localhost:8000/api/v1/data/' + API_KEY

datas = urllib.urlencode({"name_id":"test", "value":"45", })


resp = requests.post(url, data=datas, auth=('iottestuser', 'iot12345**'))

print resp

