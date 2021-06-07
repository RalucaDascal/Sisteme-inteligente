from pprint import pprint
from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from polls.models import Weather
from .serializers import WeatherSerializers
from .date import get_Weather


class WeatherListView(ListAPIView):
    #  queryset = Weather.objects.all()
    queryset = get_Weather()
    serializer_class = WeatherSerializers


def readWeather():
    w = Weather.objects.all()
    return w
