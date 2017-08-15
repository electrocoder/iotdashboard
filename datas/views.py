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

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at

http://www.apache.org/licenses/
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import uuid

from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from rest_framework import routers, serializers, viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import permissions

from chartit import DataPool, Chart

from channels.forms import ChannelForm
from channels.models import Channel
from datas.models import Data
from datas.permissions import IsOwnerOrReadOnly
from datas.serializers import DataSerializer
from iotdashboard.debug import debug


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class DataQueryList(TemplateView):
    """
    All data list for template.
    """
    template_name = "back/data_list.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        datas = Data.objects.all().order_by('-pub_date')[:100]

        value_1 = False
        value_2 = False
        value_3 = False
        value_4 = False
        value_5 = False
        value_6 = False
        value_7 = False
        value_8 = False
        value_9 = False
        value_10 = False

        for i in datas:
            if i.value_1:
                value_1 = True
            if i.value_2:
                value_2 = True
            if i.value_3:
                value_3 = True
            if i.value_4:
                value_4 = True
            if i.value_5:
                value_5 = True
            if i.value_6:
                value_6 = True
            if i.value_7:
                value_7 = True
            if i.value_8:
                value_8 = True
            if i.value_9:
                value_9 = True
            if i.value_10:
                value_10 = True

        return render(request, self.template_name, {'datas': datas,
                                                    'value_1':value_1,
                                                    'value_2':value_2,
                                                    'value_3':value_3,
                                                    'value_4':value_4,
                                                    'value_5':value_5,
                                                    'value_6':value_6,
                                                    'value_7':value_7,
                                                    'value_8':value_8,
                                                    'value_9':value_9,
                                                    'value_10':value_10
                                                    })
