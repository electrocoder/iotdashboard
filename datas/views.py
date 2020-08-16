"""
Iotdashboard project
Django 3.1
Python 3.8

Author: Sahin MERSIN

Demo: http://iotdashboard.pythonanywhere.com
Source: https://github.com/electrocoder/iotdashboard

https://iothook.com/
http://mesebilisim.com

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from datas.models import Data

from datas.serializers import DataSerializer
from devices.models import Device
from iotdashboard.debug import debug


def ip_address(request):
    """
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def datalist(request):
    datas = Data.objects.all()
    return render(request, 'back/data_list.html', locals())


class DataList(APIView):
    """
    List all datas, or create a new data.
    """

    def get(self, request, format=None):
        # api_key= request.GET['api_key']
        # device = get_object_or_404(Device, api_key=api_key, enable=True)
        try:
            if request.GET['last']:
                datas = Data.objects.all()[:1]
        except:
            datas = Data.objects.all()

        serializer = DataSerializer(datas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            api_key = request.data['api_key']
            device = get_object_or_404(Device, api_key=api_key, enable=True)
            request.data['device'] = device.pk
            request.data['remote_address'] = ip_address(request)
            serializer = DataSerializer(data=request.data)
            debug(serializer)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            msg_err = {'err': 'API KEY not found!'}
            return Response(msg_err, status=status.HTTP_400_BAD_REQUEST)


class DataDetail(APIView):
    """
    Retrieve, update or delete a datas instance.
    """

    def get_object(self, pk):
        try:
            return Data.objects.get(pk=pk)
        except Data.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        datas = self.get_object(pk)
        serializer = DataSerializer(datas)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        datas = self.get_object(pk)
        serializer = DataSerializer(datas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        datas = self.get_object(pk)
        datas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def data_chart(request, id):
    device = Device.objects.get(pk=id)
    datas = Data.objects.filter(device=device)
    return render(request, 'back/data_chart.html', locals())


def data_chart_ajax(request, id):
    device = Device.objects.get(pk=id)
    datas = Data.objects.filter(device=device)[:10]

    labels = []
    data = []

    for entry in datas:
        labels.append(entry.pub_date)
        data.append(entry.field_1)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
