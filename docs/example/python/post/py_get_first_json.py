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

url = 'http://localhost:8000/api/v1/datas/?data=first'

auth=('admin', 'Aa1234567890')

response = requests.get(url, auth=auth)
data = response.json()
print(data)
