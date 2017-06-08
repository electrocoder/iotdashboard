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

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at

http://www.apache.org/licenses/
"""

from django import template
from iotdashboard.settings import WEBSITE_NAME
import time
import os


register = template.Library()


@register.simple_tag
def version():
    """
        GIT version
    """
    try:
        return time.strftime('%m%d%Y/%u', time.gmtime(os.path.getmtime('.git/')))
    except:
        return 0


@register.simple_tag
def website_name():
    """
        WEBSITE_NAME = "Iotdashboard"
    """
    return WEBSITE_NAME
