import datetime
from pprint import pprint

from django.shortcuts import render
from datetime import datetime

from django.utils import timezone
from django.utils.timezone import now

from .models import Weather
import arrow
import requests

dataU = 1542967200
start = datetime.fromtimestamp(dataU, tz=timezone.utc)

# Get last hour of today
end = datetime.now(tz=timezone.utc)

response = requests.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat': 58.7984,
        'lng': 17.8081,
        'params': ','.join(['airTemperature', 'pressure', 'humidity', 'precipitation', 'visibility', 'waterTemperature',
                            'waveDirection', 'waveHeight', 'windWaveDirection', 'windDirection', 'windSpeed',
                            'wavePeriod']),
        'start': start,  # Convert to UTC timestamp
        'end': end,  # Convert to UTC timestamp
        'source': 'sg'
    },
    headers={
        'Authorization': '1c48e818-bc87-11eb-8d12-0242ac130002-1c48e8ea-bc87-11eb-8d12-0242ac130002'
    }
)

# Do something with response data.
json_data = response.json()
pprint(json_data)


def get_Weather():
    for x in json_data["hours"]:
        airTemperature = x["airTemperature"]['sg']
        pressure = x["pressure"]['sg']
        humidity = x["humidity"]['sg']
        precipitation = x["precipitation"]['sg']
        visibility = x["visibility"]['sg']
        waterTemperature = x["waterTemperature"]['sg']
        waveDirection = x["waveDirection"]['sg']
        waveHeight = x["waveHeight"]['sg']
        windWaveDirection = x["windWaveDirection"]['sg']
        windDirection = x["windDirection"]['sg']
        windSpeed = x["windSpeed"]['sg']
        wavePeriod = x["wavePeriod"]['sg']
        weather = Weather(airTemperature, pressure, humidity, precipitation, visibility, waterTemperature,
                          waveDirection, waveHeight, windWaveDirection, windDirection, windSpeed,
                          wavePeriod)

        weather.save()
    return Weather.objects.all()
