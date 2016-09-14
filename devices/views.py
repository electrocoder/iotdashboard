# -*- coding: utf-8 -*-
"""
Devices page

https://iothook.com/
"""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import user_passes_test
from iotdashboard.settings import LOGIN_URL

from forms import *

def admin_group(user):
    """
    Django admin page, groups page, add admin
    """
    if user:
        return bool(user.groups.filter(user = user, name=u'admin')) | user.is_superuser
    return False

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
            msg_ok = _(u'Aygıt ekleme başarılı')
        else:
            msg_err = _(u'Dikkat! Lütfen hataları düzeltiniz!')

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
            msg_ok = _(u'Aygıt güncelleme başarılı')
            return HttpResponseRedirect(reverse('device_list'))
        else:
            msg_err = _(u'Dikkat! Lütfen hataları düzeltiniz!')

    return render(request, "back/add.html", locals())

@user_passes_test(admin_group, login_url=LOGIN_URL)
def device_delete(request, id=None):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(Device, id=id)
    val.delete()
    msg_ok = _(u'Aygıt silindi')

    return HttpResponseRedirect(reverse('device_list'), locals())
