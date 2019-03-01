from rest_framework import serializers


from weather_data.models import WeatherDataModel

class WeatherDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherDataModel
        fields = ('tmax', 'tmin', 'rainfall')
