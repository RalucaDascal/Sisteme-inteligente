from .models import Weather
from rest_framework.serializers import (ModelSerializer,)

class WeatherSerializers(ModelSerializer):
    class Meta:
        model = Weather
        fields = ('airTemperature', 'pressure', 'humidity', 'precipitation', 'visibility', 'waterTemperature',
                  'waveDirection', 'waveHeight', 'windWaveDirection', 'windDirection', 'windSpeed', 'wavePeriod')
