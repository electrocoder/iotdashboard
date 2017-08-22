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

    The MIT License (MIT)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    import requests
    import json
    import urllib
    import urllib2
    import random
    import pprint

    headers = {'Content-type': 'application/json'}
    url = 'http://localhost:8000/api/v1/datas/'
    auth=('iottestuser', 'iot12345**')

    

    for i in range(30):
        data = {'api_key':'c791e11-d9ab779','name_id':'test', 'value':'45'}

        data_json = json.dumps(data)
        

        response = requests.post(url, data=data_json, headers=headers, auth=auth)
        pprint.pprint(response.json())
        

Post Api Requests.Post iotdashboard
===================================

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

    The MIT License (MIT)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    import requests
    import json
    import urllib
    import urllib2
    import random
    import pprint
    headers = {'Content-type': 'application/json'}
    url = 'http://iotdashboard.pythonanywhere.com/api/v1/datas/'
    
    auth=('admin', 'Aa1234567890')

    for i in range(10):
        data={
            'api_key':'8030e69da8b049d98807c443407f94594b558d3e',
            'element_1':'1', 'value_1':i*10,
            }

    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=headers, auth=auth)
    print(response)
    print(response.json())
    time.sleep(5)

Post Api Requests.Post with C# iotdashboard
===========================================

C# ile POST örneği.
Bu örneğe Github: https://github.com/AsocialCoder/CSharp_Webrequest adresinden ulaşabilirsiniz.

.. code-block:: c#

   /*
   Iot dashboard POST example

   iot-dashboard
   IoT: Platform for Internet of Things

   Iotdashboard source code is available under the MIT License

   Online iot dashboard test and demo http://ihook.xyz

   Online iot dashboard https://iothook.com
   
   You can find project details on our project page https://iothook.com and wiki https://iothook.com

    The MIT License (MIT)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
   */
   
    using System;
    using System.Collections.Generic;
    using System.ComponentModel;
    using System.Data;
    using System.Drawing;
    using System.Linq;
    using System.Text;
    using System.Threading.Tasks;
    using System.Windows.Forms;
    using System.IO;
    using System.Net;
    using System.Collections.Specialized;
    using System.Windows.Forms.DataVisualization.Charting;
    using System.Web.Script.Serialization;
    using Newtonsoft.Json.Linq;
    using System.Threading;
    using Newtonsoft.Json;

    String url = "http://iotdashboard.pythonanywhere.com/api/v1/datas";

    CookieContainer cookies = new CookieContainer();
    var webRequest = (HttpWebRequest)WebRequest.Create(url);
    webRequest.Method = "POST";
    webRequest.CookieContainer = cookies;
    webRequest.ContentType = "application/json";
    webRequest.UserAgent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1";
    webRequest.Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
    string autorization = "admin" + ":" + "Aa1234567890";
    byte[] binaryAuthorization = System.Text.Encoding.UTF8.GetBytes(autorization);
    autorization = Convert.ToBase64String(binaryAuthorization);
    autorization = "Basic " + autorization;
    webRequest.Headers.Add("AUTHORIZATION", autorization);
    webRequest.SendChunked = true;

    using (var streamWriter = new StreamWriter(webRequest.GetRequestStream()))
    {
    MessageBox.Show("burada");
    var json = new System.Web.Script.Serialization.JavaScriptSerializer().Serialize(new
    {
    api_key = 8030e69da8b049d98807c443407f94594b558d3e,
    value_1 = "15",
    value_2 = "12",
    value_3 = "25",
    value_4 = "85",
    value_5 = "10",

    });

    streamWriter.Write(json);

    MessageBox.Show("Değerler başarılı bir şekilde yüklendi.");
    streamWriter.Flush();
    streamWriter.Close();
    webRequest.Abort();
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

    The MIT License (MIT)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    import requests
    import json

    headers = {'Content-type': 'application/json'}
    url = 'http://localhost:8000/api/v1/datas/'
    auth=('iottestuser', 'iot12345**')

    data = {'api_key':'c791e11-d9ab779','name_id':'test', 'value':'45'}

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

    The MIT License (MIT)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    import requests
    import json
    import urllib
    import urllib2
    import random
    import pprint

    headers = {'Content-type': 'application/json'}
    url = 'http://localhost:8000/api/v1/datas/'
    auth=('iottestuser', 'iot12345**')

    data = {'api_key':'c791e11-d9ab779','name_id':'test', 'value':'45'}

    data_json = json.dumps(data)

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

    The MIT License (MIT)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    import requests
    import json
    import urllib
    import urllib2
    import random

    headers = {'Content-type': 'application/json'}
    url = 'http://localhost:8000/api/v1/datas/'
    auth=('iottestuser', 'iot12345**')

    data = {'api_key':'c791e11-d9ab779','name_id':'test', 'value':'45'}

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

    The MIT License (MIT)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    import httplib, urllib

    headers = {'Content-type': 'application/json'}
    url = 'http://localhost:8000/api/v1/datas/'
    auth=('iottestuser', 'iot12345**')

    data = {'api_key':'c791e11-d9ab779','name_id':'test', 'value':'45'}

    conn = httplib.HTTPConnection("localhost", 8000)
    conn.request("POST", "/api/v1/datas/" + API_KEY, datas, headers)

    response = conn.getresponse()

    print response.status, response.reason

    print response.read()
