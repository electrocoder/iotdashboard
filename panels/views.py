# -*- coding: utf-8 -*-
"""
Panels page

https://iothook.com/
"""

from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    """
    :param request:
    :return:
    """
    user = authenticate(username='iottestuser', password='iot12345**')
    login(request, user)
    return render(request, "back/index.html", locals())