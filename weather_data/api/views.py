from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from datetime import datetime
import json

from .serializers import WeatherDataSerializer
from weather_data.models import WeatherDataModel


class WeatherListAPIView(ListAPIView):
    renderer_classes = (JSONRenderer, )
    valid_locations = ('UK', 'England', 'Scotland', 'Wales')
    valid_metrics = ('Tmax', 'Tmin', 'Rainfall')

    def get_weather_data(self,metric,location,start_date,end_date):
        output = []
        qs = WeatherDataModel.objects.filter(location=location).first()
        if qs:
            weatherdata = WeatherDataSerializer(qs).data
            for item in weatherdata[metric]:
                dte = f"{str(item['month'])}-{str(item['year'])}"
                dte = datetime.strptime(dte, '%m-%Y')
                if dte >= start_date and dte <= end_date:
                    val = f"'{datetime.strftime(dte, '%Y-%m')}': {str(item['value'])}"
                    output.append(val)
            return output
        return f"{location} data does not exist."

    def get(self, request):
        passed_startdate = request.GET.get('start_date',False)
        passed_enddate = request.GET.get('end_date',False)
        passed_metric = request.GET.get('metric_type',False)
        passed_location = request.GET.get('location',False)

        if passed_startdate and passed_enddate and passed_metric and passed_location:
            if passed_metric not in self.valid_metrics:
                return Response({'Error':'Metric Type can not be other than Tmax, Tmin and Rainfall.'},
                                 status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            if passed_location not in self.valid_locations:
                return Response({'Error':'Location can not be other than UK, England, Scotland and Wales.'},          					status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            try:
                start_date = datetime.strptime(passed_startdate, '%d-%m-%Y')
                end_date = datetime.strptime(passed_enddate, '%d-%m-%Y')
            except ValueError as e:
                return Response({'Error':'Start and End date format should be DD-MM-YYYY'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            try:
                result = self.get_weather_data(passed_metric.lower(), passed_location, start_date, end_date)
                return Response({'Result':result}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'Error': e }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            return Response({'Error':'All parameters are not found in the url.Expected parameters <start_date>, <end_date>, <metric_type> and <location>.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
