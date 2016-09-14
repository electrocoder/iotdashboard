# -*- coding: utf-8 -*-
"""
Channels page

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
from devices.views import admin_group

from forms import *

@csrf_exempt
def element_add(request):
    """
    :param request:
    :return:
    """
    msg_ok = ""
    msg_err = ""

    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            form.save()
            msg_ok = _(u'Element ekleme başarılı')
        else:
            msg_err = _(u'Dikkat! Lütfen hataları düzeltiniz!')

    form = ElementForm()
    return render(request, "back/add.html", locals())

def element_list(request):
    """
    :param request:
    :return:
    """
    list = Element.objects.all()
    return render(request, "back/element_list.html", locals())

def element_edit(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(Element, id=id)

    form = ElementForm(request.POST or None, instance=val)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg_ok = _(u'Element güncelleme başarılı')
            return HttpResponseRedirect(reverse('element_list'))
        else:
            msg_err = _(u'Dikkat! Lütfen hataları düzeltiniz!')

    return render(request, "back/add.html", locals())

@user_passes_test(admin_group, login_url=LOGIN_URL)
def element_delete(request, id=None):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(Element, id=id)
    val.delete()
    msg_ok = _(u'Element silindi')

    return HttpResponseRedirect(reverse('element_list'), locals())
