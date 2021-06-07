from django.contrib import admin
from django.urls import include, path

from polls.views import WeatherListView
from polls.doubleT import Split

urlpatterns = [
    path('', WeatherListView.as_view()),
    path('', Split)

]
