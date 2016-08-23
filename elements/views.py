#-*- coding: utf-8 -*-
"""
Channels page

https://iothook.com/
"""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
            msg_ok = u"element_add"
            print msg_ok
        else:
            msg_err = u"Dikkat! Lütfen hataları düzeltiniz!"
            print msg_err

    form = ElementForm()
    return render(request, "back/add.html", locals())

def element_list(request):
    """
    :param request:
    :return:
    """
    list = Element.objects.all()
    return render(request, "back/element_list.html", locals())
