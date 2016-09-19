# -*- coding: utf-8 -*-
"""
Datas REST Framework

https://iothook.com/
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django.http import Http404
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from rest_framework import routers, serializers, viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import permissions

from chartit import DataPool, Chart

from iotdashboard.settings import LOGIN_URL

from .models import Data
from elements.models import Element
from channels.models import Channel
from drawcharts.models import DrawChart

from datas.permissions import IsOwnerOrReadOnly
from datas.serializers import DataSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class DataList(views.APIView):
    """
    All data list
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, api_key, format=None):
        """
        http --json http://127.0.0.1:8000/api/v1/data/API-KEY/
        http -a username:password --json http://127.0.0.1:8000/api/v1/data/API-KEY/
        :param request:
        :param format:
        :return:
        """
        try:
            datas = Data.objects.filter(owner=request.user, channel=Channel.objects.get(api_key=api_key)).order_by('-pk')[:100]
            serializer = DataSerializer(datas, many=True)
            return Response(serializer.data)
        except:
            raise Http404

    def post(self, request, api_key, format=None):
        """
        http -a username:password --json POST http://127.0.0.1:8000/api/v1/data/API-KEY/ name_id="123" value="0"
        :param request:
        :param format:
        :return:
        """
        data = JSONParser().parse(request)
        data['owner'] = self.request.user.pk

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            data['remote_address'] = x_forwarded_for.split(',')[-1].strip()
        else:
            data['remote_address'] = request.META.get('REMOTE_ADDR') + "&" + request.META.get('HTTP_USER_AGENT') + "&" + request.META.get('SERVER_PROTOCOL')

        name=get_object_or_404(Element, name_id=data['name_id']).channel
        data['channel'] = get_object_or_404(Channel, api_key=api_key, name=name).pk

        serializer = DataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

class DataDetail(views.APIView):
    """
    Retrieve, update or delete a datas instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_object(self, request, pk, api_key):
        """
        :param pk:
        :return:
        """
        try:
            return Data.objects.get(pk=pk, owner=request.user, channel=Channel.objects.get(api_key=api_key))
        except Data.DoesNotExist:
            raise Http404

    def get(self, request, pk, api_key, format=None):
        """
        :param request:
        :param pk:
        :param format:
        :return:
        """
        datas = self.get_object(request, pk, api_key)
        serializer = DataSerializer(datas)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        :param request:
        :param pk:
        :param format:
        :return:
        """
        datas = self.get_object(pk)
        serializer = DataSerializer(datas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        :param request:
        :param pk:
        :param format:
        :return:
        """
        datas = self.get_object(pk)
        datas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DataQueryList(TemplateView):
    """
    All data list for template.
    """
    template_name = "back/data_list.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'datas': Data.objects.filter(owner=request.user).order_by('-pub_date')[:100]})

def chart_view(request, id):
    """
    :param request:
    :return:
    """
    datas = Data.objects.filter(owner=request.user, channel=id).order_by('-pub_date')[:100]

    for i in datas:
        # problem ?
        try:
            DrawChart(channel=i.channel, value_char=str(i.value), value_decimal=float(i.value), pub_date=i.pub_date).save()
        except:
            pass

    datas = DrawChart.objects.all()

    ds = DataPool(
           series=
            [
                {
                'options': {
               'source': datas
            },
              'terms': [
                'id',
                'pub_date',
                'value_decimal',
              ]
            }
             ]
    )

    cht = Chart(
            datasource = ds,
            series_options =
              [
                  {
                      'options':{
                        'type': 'scatter',
                        'stacking': False
                      },
                    'terms':{
                      'pub_date': [
                        'value_decimal',
                      ]
                      }
                  }
              ],

        chart_options={
            'title': {
                'text': _('Kanal: ') + str(datas[0].channel)
            },
            'xAxis': {
                'title': {
                    'text': 'Publish Date'}
            },
            'yAxis': {
                'title': {
                    'text': 'Value'}
            },
            'legend': {
                'enabled': False},
            'credits': {
                'enabled': False}
        },

    )

    val = DrawChart.objects.filter(channel=str(datas[0].channel)).delete()

    return render(request, "back/chart_view.html", locals())

def chart_view_realtime(request):
    """
    :param request:
    :return:
    """
    from django.utils.html import mark_safe

    array = ([
        ['Id', 'Value'],
        [5, 6],
        [33, 44],
        [66, 77],
        [88, 565],
    ])
    tmp = []
    tmp.append([125, 255])
    tmp.append([126, 255])
    tmp.append([127, 255])

    array = mark_safe(array)
    return render_to_response('back/chart_view_realtime.html', locals())
    # return render(request, 'back/chart_view_realtime.html')

def chart_view_realtime_now(request):
    import json
    import random

    gelen = ""
    if request.GET.has_key('client_response'):
        gelen =  request.GET['client_response'] #gelen
        # print "gelen-%s-" % gelen
        if not gelen == "":
            u = Data.objects.get(pk=54075)
            response_dict = {}
            gelen = random.random() * 100
            server_response = gelen  # gonderilen
            response_dict.update({'server_response': server_response})
            return HttpResponse(json.dumps(response_dict))
    else:
        print("hata")

    response_dict = {}
    gelen = random.random() * 100
    server_response = gelen  # gonderilen
    response_dict.update({'server_response': server_response})
    return HttpResponse(json.dumps(response_dict))

def export(request, model):
    """
    :param request:
    :return:
    """
    from django.apps import apps
    from django.core import serializers

    model = apps.get_model(app_label=model + 's', model_name=model)

    data = serializers.serialize(request.GET['format'], model.objects.all().order_by('-pub_date')[:100])

    return JSONResponse({'response_data':data})

