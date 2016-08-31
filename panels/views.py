# -*- coding: utf-8 -*-
"""
Panels page

https://iothook.com/
"""

from django.shortcuts import render

def index(request):
    """
    :param request:
    :return:
    """
    return render(request, "back/index.html", locals())