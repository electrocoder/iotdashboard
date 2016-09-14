.. iotHook documentation master file, created by
   sphinx-quickstart on Tue Apr 12 04:35:14 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

POST Web API
============

Iotdashboard a Raspberry Pi gibi bir cihaz ile veri göndermek için kullanıcı adı ve şifre oluşturulmalıdır.

Kullanıcı adı ve şifre oluşturmak için ./manage.py createsuperuser komutu ile user oluşturulur.

.. code-block:: bash

    ./manage.py createsuperuser

Iotdashboard içerisindeki docs/example_db klasörü içerisinde örnek veritabanı dosyası bulunmaktadır.

Kullanıcı oluşturduktan sonra localhost üzerinde veya Raspberry Pi ye ip adresi ile veri gönderilebilir.

Post Yapısı
===========

.. code-block:: bash

   http -a USERNAME:PASSWORD --json POST http://localhost:8000/api/v1/datas/APIKEY/ name_id="ELEMENT_ID" value="VALUE"

Post Api
========

.. code-block:: bash

   http -a iottestuser:iot12345** --json POST http://localhost:8000/api/v1/datas/0cd76eb-5f3b179/ name_id="test" value="1"

veya

.. code-block:: bash

   http -a iottestuser:iot12345** --json POST http://127.0.0.1:8000/api/v1/datas/0cd76eb-5f3b179/ name_id="test" value="1"

veya

.. code-block:: bash

   http -a iottestuser:iot12345** --json POST http://ihook.xyz/api/v1/datas/0cd76eb-5f3b179/ name_id="test" value="1"

POST işleminin başarılı olduğu JSON olarak döner.

.. code-block:: bash

    $ http -a iottestuser:iot12345** --json POST http://127.0.0.1:8000/api/v1/datas/0cd76eb-5f3b179/ name_id="test" value="1"
    HTTP/1.0 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Language: tr
    Content-Type: application/json
    Date: Sat, 03 Sep 2016 23:16:38 GMT
    Server: WSGIServer/0.1 Python/2.7.12
    Vary: Accept, Accept-Language, Cookie
    X-Frame-Options: SAMEORIGIN

    {
        "channel": 6,
        "id": 12,
        "name_id": "test",
        "owner": 2,
        "pub_date": "2016-09-03T23:16:38.137353Z",
        "remote_address": "127.0.0.1&HTTPie/0.9.6&HTTP/1.1",
        "value": "1"
    }

POST başarısız ise şu mesaj alınır.

.. code-block:: bash

    $ http -a iottestuser:iot12345** --json POST http://127.0.0.1:8000/api/v1/datas/0cd76eb-5f3b179/ name_id="aaaaa" value="1"
    HTTP/1.0 404 Not Found
    Allow: GET, POST, HEAD, OPTIONS
    Content-Language: tr
    Content-Type: application/json
    Date: Sat, 03 Sep 2016 23:27:29 GMT
    Server: WSGIServer/0.1 Python/2.7.12
    Vary: Accept, Accept-Language, Cookie
    X-Frame-Options: SAMEORIGIN

    {
        "detail": "Bulunamadı."
    }

Post Api Requests.Post localhost
================================

Python ile POST örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

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

Post Api Requests.Post ihook
============================

Python ile POST örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

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

    API_KEY = "b64bc5c-7ec12c7"
    url = 'http://ihook.xyz/api/v1/datas/' + API_KEY
    auth=('iottestuser', 'iot12345**')

    for i in range(20):
        data = {"name_id":"test_element", "value":i}

        data_json = json.dumps(data)
        headers = {'Content-type': 'application/json'}

        response = requests.post(url, data=data_json, headers=headers, auth=auth)
        pprint.pprint(response.json())

Post Api Requests.Post localhost
================================

Python ile POST örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

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

    API_KEY = "c791e11-d9ab779"
    url = 'http://localhost:8000/api/v1/datas/' + API_KEY

    datas = {'name_id':'test','value':'66'}

    auth=('iottestuser', 'iot12345**')

    response = requests.post(url, data=datas, auth=auth)
    print response

Post Api Requests.Post headers
==============================

Python ile headers POST örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

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

    data = {"name_id":"test", "value":"45"}

    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}

    response = requests.post(url, data=data_json, headers=headers, auth=auth)
    pprint.pprint(response.json())


Post Api Requests.Post urllib
=============================

Python ile urllib POST örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

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

    API_KEY = "c791e11-d9ab779"
    url = 'http://localhost:8000/api/v1/datas/' + API_KEY
    auth=('iottestuser', 'iot12345**')

    data = {"name_id":"test", "value":"45"}

    data = urllib.urlencode(data)

    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)

    html = response.read()

    print html

Post Api Requests.Post httplib
==============================

Python ile httplib POST örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

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
