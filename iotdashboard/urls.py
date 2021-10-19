"""
Iotdashboard project
Django 3.1
Python 3.8

Author: Sahin MERSIN

Demo: http://iotdashboard.pythonanywhere.com
Source: https://github.com/electrocoder/iotdashboard

https://iothook.com/
http://mesebilisim.com

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

from django.urls import path, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from rest_framework import routers

from devices import views as devices

from datas import views as datas

router = routers.DefaultRouter()

urlpatterns = i18n_patterns(
    # dashboard panels index page
    path('', devices.index, name='index'),

    # device api key
    path('key/list/', devices.key_list, name='key_list'),
    path('key/generate/<str:id>/', devices.generate_key, name='generate_key'),

    # add device
    path('device/add/', devices.device_add, name='device_add'),
    path('device/list/', devices.device_list, name='device_list'),
    path('device/edit/<str:id>/', devices.device_edit, name='device_edit'),
    path('device/delete/<str:id>/', devices.device_delete, name='device_delete'),

    # data query
    path('datas/', datas.datalist, name='datas'),
    path('datas/chart/<str:id>/', datas.data_chart, name='data_chart'),
    path('datas/chart/ajax/<str:id>/', datas.data_chart_ajax, name='data_chart_ajax'),

    # export xls
    path('export/<str:model>/', devices.export, name='export'),

    # django admin page
    path('admin/', admin.site.urls),
)

urlpatterns += [
    # REST framework
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/datas/', datas.DataList.as_view(), name='api_data'),
    path('api/datas/<int:pk>/', datas.DataDetail.as_view(), name='api_data_detail'),
]

urlpatterns += [
    path('media/<str:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<str:path>/', serve, {'document_root': settings.STATIC_ROOT, }),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
