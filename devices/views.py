#-*- coding: utf-8 -*-
"""
Devices page

https://iothook.com/
"""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from forms import *

@csrf_exempt
def device_add(request):
    """
    :param request:
    :return:
    """
    msg_ok = ""
    msg_err = ""

    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            msg_ok = u"device_add"
        else:
            msg_err = u"Dikkat! Lütfen hataları düzeltiniz!"

    form = DeviceForm()
    return render(request, "back/add.html", locals())

def device_list(request):
    """
    :param request:
    :return:
    """
    list = Device.objects.all()
    return render(request, "back/device_list.html", locals())
