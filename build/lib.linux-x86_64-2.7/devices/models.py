#-*- coding: utf-8 -*-
"""
Device manager

https://iothook.com/
"""

from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify as djslugify
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google

class Device(models.Model):
    """
    Device manager.
    Arduino, Rasberry pi ...
    """
    name                = models.CharField(max_length=30, help_text=u"Aygit adını giriniz")
    slug                = models.SlugField(max_length=50, help_text =u"Url adresi (Otomatik olarak alinir)")
    image               = models.ImageField(upload_to='images/%Y/%m/%d', default="images/image.png")
    pub_date            = models.DateTimeField(auto_now=True)
    description         = models.TextField(blank=True)
    enable              = models.BooleanField(default=True)

    def __unicode__(self):
        """
        """
        return unicode(self.name)

    def save(self, *args, **kwargs):
        """
        """
        super(Device, self).save(*args, **kwargs)
        if not self.slug:
            name = self.name.replace(u'\u0131', 'i') #turkce karakter 'ı' icin
            self.slug = djslugify(name + "-" + str(self.id))
            self.save()
