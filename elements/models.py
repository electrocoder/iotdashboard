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
    channel       = models.ForeignKey(Channel)
    type          = models.CharField(_('tip'), max_length=200, choices=FORM_ELEMENTS)
    name          = models.CharField(_('isim'), max_length=70)
    name_id       = models.CharField(_('isim id'), max_length=70, null=True, blank=True)
    pub_date      = models.DateTimeField(_('yayın tarihi'), auto_now=True)
    description   = models.TextField(_('açıklama'), blank=True)
    enable        = models.BooleanField(_('aktif et'), default=True)

    def __unicode__(self):
        """
        """
        return unicode(self.name)


    def save(self, *args, **kwargs):
        """
        """
        super(Element, self).save(*args, **kwargs)
        if not self.name_id:
            name_id = self.name.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.name_id = (djslugify(name_id)).replace('-', '_')
            self.save()
