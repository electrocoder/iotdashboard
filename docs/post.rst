.. iotHook documentation master file, created by
   sphinx-quickstart on Tue Apr 12 04:35:14 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

POST Web API
===================================

Iotdashboard a Raspberry Pi gibi bir cihaz ile veri göndermek için kullanıcı adı ve şifre oluşturulmalıdır.

Kullanıcı adı ve şifre oluşturmak için ./manage.py createsuperuser komutu ile user oluşturulur.

.. code-block:: bash

    ./manage.py createsuperuser

Iotdashboard içerisindeki docs/example_db klasörü içerisinde örnek veritabanı dosyası bulunmaktadır.

Kullanıcı oluşturduktan sonra localhost üzerinde veya Raspberry Pi ye ip adresi ile veri gönderilebilir.

Post Yapısı
===========

.. code-block:: bash

   http -a USERNAME:PASSWORD --json POST http://localhost:8000/api/v1/data/APIKEY/ name_id="ELEMENT_ID" value="VALUE"

Post Api
========

.. code-block:: bash

   http -a iottestuser:iot12345** --json POST http://localhost:8000/api/v1/data/0cd76eb-5f3b179/ name_id="test" value="1"

veya

.. code-block:: bash

   http -a iottestuser:iot12345** --json POST http://127.0.0.1:8000/api/v1/data/0cd76eb-5f3b179/ name_id="test" value="1"

veya

.. code-block:: bash

   http -a iottestuser:iot12345** --json POST http://ihook.xyz/api/v1/data/0cd76eb-5f3b179/ name_id="test" value="1"

POST işleminin başarılı olduğu JSON olarak döner.

.. code-block:: bash

    $ http -a iottestuser:iot12345** --json POST http://127.0.0.1:8000/api/v1/data/0cd76eb-5f3b179/ name_id="test" value="1"
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

    $ http -a iottestuser:iot12345** --json POST http://127.0.0.1:8000/api/v1/data/0cd76eb-5f3b179/ name_id="aaaaa" value="1"
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


