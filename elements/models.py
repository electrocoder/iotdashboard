#-*- coding: utf-8 -*-
"""
Element

https://iothook.com/
"""

from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify as djslugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from channels.models import Channel

FORM_ELEMENTS = (
    ("text", "text"),
    ("number", "number"),
)

class Element(models.Model):
    """
    Element
    """
    channel       = models.ForeignKey(Channel, verbose_name="Kanal adi")
    type          = models.CharField(max_length=200, choices=FORM_ELEMENTS, verbose_name="Element tipi")
    name          = models.CharField(max_length=70, verbose_name="Element adi")
    name_id       = models.CharField(max_length=70, null=True, blank=True)
    default_value = models.CharField(max_length=35, null=True, blank=True)
    size          = models.CharField(max_length=5, null=True, blank=True)
    max_length    = models.CharField(max_length=5, null=True, blank=True)
    pub_date      = models.DateTimeField(auto_now=True)
    description   = models.TextField(blank=True)
    enable        = models.BooleanField(default=True)

    def __unicode__(self):
        """
        """
        return unicode(self.name)
