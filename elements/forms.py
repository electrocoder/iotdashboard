#-*- coding: utf-8 -*-

from django.forms import ModelForm
from models import *

class ElementForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Element
        exclude = [
            'api_key',
        ]

    def __init__(self, *args, **kwargs):
        super(ElementForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            if i not in ['enable',]:
                self.fields[i].widget.attrs['class'] = 'form-control'
                self.fields[i].widget.attrs['name'] = i
