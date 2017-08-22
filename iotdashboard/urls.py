# -*- coding: utf-8 -*-
"""
Iotdashboard project
Django 1.10.1
Python 2.7.6

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

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from rest_framework import routers

from channels import views as views_channels

from datas import views as views_datas
from datas import views_api_v1 as views_api_v1
from datas import views_api_v1_1 as views_api_v1_1

router = routers.DefaultRouter()

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='IoTdashboard API')


urlpatterns = i18n_patterns(
    # backoffice panels index page
    url(r'^$', views_channels.index, name='index'),

    # channel api key
    url(r'^key/list/$', views_channels.key_list, name='key_list'),
    url(r'^key/generate/(?P<id>[^/]*)/$', views_channels.generate_key, name='generate_key'),

    # add channel
    url(r'^channel/add/$', views_channels.channel_add, name='channel_add'),
    url(r'^channel/list/$', views_channels.channel_list, name='channel_list'),
    url(r'^channel/edit/(?P<id>[^/]*)/$', views_channels.channel_edit, name='channel_edit'),
    url(r'^channel/delete/(?P<id>[^/]*)/$', views_channels.channel_delete, name='channel_delete'),

    # data query
    url(r'^datas/$', views_datas.DataQueryList.as_view(), name='datas'),

    # chart
    # url(r'^chart-view/(?P<id>[^/]*)/$', views_datas.chart_view, name='chart_view'),

    # realtime chart
    # url(r'^chart-view/now/realtime/$', views_datas.chart_view_realtime, name='chart_view_realtime'),
    # url(r'^chart-view/now/realtime/now/$', views_datas.chart_view_realtime_now, name='chart_view_realtime_now'),

    # export xls
    url(r'^export/(?P<model>[\w-]+)/$', views_channels.export, name='export'),

    # django admin page
    url(r'^admin/', admin.site.urls),

    # rest api docs
    url(r'^api-docs/$', schema_view),
)

urlpatterns += [
    # favicon
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),

    # REST framework
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/v1/datas/$', views_api_v1.Datas.as_view()),
    url(r'^api/v1/datas/(?P<pk>[0-9]+)/$',  views_api_v1.DataDetail.as_view()),

    url(r'^api/v1.1/datas/$', views_api_v1_1.Datas.as_view()),

]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
