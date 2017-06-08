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
from base64 import b64encode

userAndPass = b64encode(b"admin:Aa1234567890").decode("ascii")
headers = {'Authorization':'Basic %s' % userAndPass}

auth=('admin', 'Aa1234567890')

datas = urllib.urlencode({'element_id_1':'a', 'value_1':10, 'api_key':'311b9c68f7e64bdfb77aab1e4d53aaf04378a463'})

conn = httplib.HTTPConnection("localhost", 8000)
conn.request("POST", "/api/v1/datas/", datas, headers)

response = conn.getresponse()

print response.status, response.reason

print response.read()

