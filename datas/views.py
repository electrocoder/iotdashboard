#-*- coding: utf-8 -*-
"""
Datas REST Framework

https://iothook.com/
"""

from serializers import DataSerializer

from django.http import Http404

from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

from rest_framework import routers, serializers, viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import permissions

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from models import Data
from channels.models import Channel
from permissions import IsOwnerOrReadOnly

class DataList(views.APIView):
    """
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
            datas = Data.objects.filter(channel=Channel.objects.get(api_key=api_key))
            serializer = DataSerializer(datas, many=True)
            return JSONResponse(serializer.data)
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
        data['channel'] = get_object_or_404(Channel, api_key=api_key).pk
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

    def get_object(self, pk):
        """
        :param pk:
        :return:
        """
        try:
            return Data.objects.get(pk=pk)
        except Data.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        :param request:
        :param pk:
        :param format:
        :return:
        """
        datas = self.get_object(pk)
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
    """
    template_name = "back/data_list.html"

    def get_context_data(self, **kwargs):
        context = super(DataQueryList, self).get_context_data(**kwargs)
        context['datas'] = Data.objects.all()[:50]
        return context

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

