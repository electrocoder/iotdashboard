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


# from datas.views import JSONResponse
from devices.forms import DeviceForm
from devices.models import Device
from iotdashboard.debug import debug
from iotdashboard.settings import LOGIN_URL


def index(request):
    """
    :param request:
    :return:
    """
    panel = True
    # auto login for test users
    # admin:Aa1234567890
    user = authenticate(username='admin', password='Aa1234567890')
    login(request, user)
    return render(request, "back/index.html", locals())


class DataQueryList(TemplateView):
    """
    All data list for template.
    """
    template_name = "back/data_list.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'datas': Device.objects.filter(owner=request.user).order_by('-pub_date')[:100]})


@login_required(login_url=LOGIN_URL)
@csrf_exempt
def device_add(request):
    """
    :param request:
    :return:
    """
    device_add = True
    msg_ok = ""
    msg_err = ""

    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.api_key = (uuid.uuid4().hex)[:20] + (uuid.uuid4().hex)[:20]

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                f.remote_address = x_forwarded_for.split(',')[-1].strip()
            else:
                f.remote_address = request.META.get('REMOTE_ADDR') + "&" + request.META.get(
                    'HTTP_USER_AGENT') + "&" + request.META.get('SERVER_PROTOCOL')

            f.save()
            msg_ok = _(u'Kanal ekleme başarılı')
        else:
            msg_err = _(u'Dikkat! Lütfen hataları düzeltiniz!')

    form = DeviceForm()

    return render(request, "back/add.html", locals())


@login_required(login_url=LOGIN_URL)
def device_list(request):
    """
    :param request:
    :return:
    """
    device_list = True
    list = Device.objects.all()
    return render(request, "back/device_list.html", locals())


@login_required(login_url=LOGIN_URL)
def device_edit(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(Device, id=id)

    form = DeviceForm(request.POST or None, request.FILES or None, instance=val)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg_ok = _(u'Kanal güncelleme başarılı')
            return HttpResponseRedirect(reverse('device_list'))
        else:
            msg_err = _(u'Dikkat! Lütfen hataları düzeltiniz!')

    return render(request, "back/add.html", locals())


@login_required(login_url=LOGIN_URL)
def device_delete(request, id=None):
    """
    :param request:
    :param id:
    :return:
    """
    device = get_object_or_404(Device, id=id).delete()

    msg_ok = _(u'Kanal silindi')

    return HttpResponseRedirect(reverse('device_list'), locals())


@login_required(login_url=LOGIN_URL)
def key_list(request):
    """
    :param request:
    :return:
    """
    key_list = True
    list = Device.objects.filter(enable=True)
    return render(request, "back/key_list.html", locals())


@login_required(login_url=LOGIN_URL)
def generate_key(request, id=None):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(Device, id=id)
    val.api_key = (uuid.uuid4().hex)[:20] + (uuid.uuid4().hex)[:20]
    val.save()
    list = Device.objects.filter(enable=True)
    msg_ok = _(u'Key üretildi')

    return HttpResponseRedirect(reverse('key_list'), locals())


def export(request, model):
    """
    :param request:
    :return:
    """
    from django.apps import apps
    from django.core import serializers

    model = apps.get_model(app_label=model + 's', model_name=model)

    data = serializers.serialize(request.GET['format'], model.objects.filter(owner=request.user).order_by('-pub_date')[:100])

    return JSONResponse({'response_data':data})