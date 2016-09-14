# -*- coding: utf-8 -*-
"""
Iot dashboard GET example

iot-dashboard
IoT: Platform for Internet of Things

Iotdashboard source code is available under the MIT License

Online iot dashboard test and demo http://ihook.xyz

Online iot dashboard https://iothook.com

You can find project details on our project page https://iothook.com and wiki https://iothook.com
"""

import requests
import httplib, urllib
from requests.auth import HTTPDigestAuth
import json
import matplotlib.pyplot as plt

API_KEY = "c791e11-d9ab779"

url = 'http://localhost:8000/api/v1/datas/' + API_KEY

myResponse = requests.get(url, auth=('iottestuser', 'iot12345**'), verify=True)
print (myResponse.status_code)

d= []

if(myResponse.ok):
    jData = json.loads(myResponse.content)
    for i in jData:
        print i['value']
        d.append(i['value'])
    plt.plot(d)
    plt.show()
else:
    myResponse.raise_for_status()
