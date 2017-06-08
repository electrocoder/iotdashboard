# -*- coding: utf-8 -*-
"""
URLs for iotdashboard project.
Django 1.9.7.
Python 2.7.12

https://iothook.com/
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

    # REST framework login to the Browsable API
    url(r'^docs/api/', include('rest_framework_docs.urls')),

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
    url(r'^api/v1/datas/$', views_datas.Datas.as_view()),
    url(r'^api/v1/datas/(?P<pk>[0-9]+)/$',  views_datas.DataDetail.as_view()),
]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
