# -*- coding: utf-8 -*-
"""
DrawChart

https://iothook.com/
"""

from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify as djslugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import hashlib, random

from channels.models import Channel

class DrawChart(models.Model):
    """
    Requests for draw charts
    """
    channel       = models.CharField(max_length=50)
    value_char    = models.CharField(max_length=10, null=False, blank=False)
    value_decimal = models.DecimalField(max_digits=9, decimal_places=2)
    pub_date      = models.DateTimeField(auto_now=False)

    def __unicode__(self):
        return unicode(self.channel)

