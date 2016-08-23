#-*- coding: utf-8 -*-
"""
Channels page

https://iothook.com/
"""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from forms import *

@csrf_exempt
def channel_add(request):
    """
    :param request:
    :return:
    """
    msg_ok = ""
    msg_err = ""

    if request.method == 'POST':
        form = ChannelForm(request.POST)
        if form.is_valid():
            form.save()
            msg_ok = u"channel_add"
            print msg_ok
        else:
            msg_err = u"Dikkat! Lütfen hataları düzeltiniz!"
            print msg_err

    form = ChannelForm()
    return render(request, "back/add.html", locals())

def channel_list(request):
    """
    :param request:
    :return:
    """
    list = Channel.objects.all()
    return render(request, "back/channel_list.html", locals())
