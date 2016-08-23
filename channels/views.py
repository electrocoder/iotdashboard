#-*- coding: utf-8 -*-
"""
Channels page

https://iothook.com/
"""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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

def channel_edit(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(Channel, id=id)

    form = ChannelForm(request.POST or None, instance=val)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg_ok = u"element_edit"
            return HttpResponseRedirect(reverse('channel_list'))
        else:
            msg_err = u"Dikkat! Lütfen hataları düzeltiniz!"

    return render(request, "back/add.html", locals())

def channel_delete(request, id=None):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(Channel, id=id)
    val.delete()
    msg_ok = u"channel_delete"

    return HttpResponseRedirect(reverse('channel_list'), locals())

############################

def key_list(request):
    """
    :param request:
    :return:
    """
    list = Channel.objects.filter(enable=True)
    return render(request, "back/key_list.html", locals())

def generate_key(request, id=None):
    """
    :param request:
    :param id:
    :return:
    """
    val = get_object_or_404(Channel, id=id)
    val.api_key = (hashlib.sha1(str(val.pub_date)).hexdigest())[:5] + "-" + (hashlib.sha1(str(random.random())).hexdigest())[:5]
    val.save()
    list = Channel.objects.filter(enable=True)
    msg_ok = u"generate_key"

    return render(request, "back/key_list.html", locals())
