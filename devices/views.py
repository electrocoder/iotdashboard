#-*- coding: utf-8 -*-
"""
Devices page

https://iothook.com/
"""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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

def device_edit(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(Device, id=id)

    form = DeviceForm(request.POST or None, instance=val)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg_ok = u"device_edit"
            return HttpResponseRedirect(reverse('device_list'))
        else:
            msg_err = u"Dikkat! Lütfen hataları düzeltiniz!"

    return render(request, "back/add.html", locals())

def device_delete(request, id=None):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(Device, id=id)
    val.delete()
    msg_ok = u"device_delete"

    return HttpResponseRedirect(reverse('device_list'), locals())
