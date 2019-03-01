from django.core.management.base import BaseCommand
from requests.exceptions import RequestException
import requests
import json


from weather_data.models import WeatherDataModel
from weather_data import models


url1 = 'https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Tmax-{}.json'
url2 = 'https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Tmin-{}.json'
url3 = 'https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-{}.json'


class Command(BaseCommand):
    help = "Fetch data from S3 url and populates model."
    def handle(self, **options):
        locations = ('UK', 'Scotland', 'Wales', 'England')
        for loc in locations:
            try:
                response_tmax = requests.get(url=url1.format(loc), headers = {'Content-Type': 'application/json'})
                response_tmin = requests.get(url=url2.format(loc), headers = {'Content-Type': 'application/json'})
                response_rain = requests.get(url=url3.format(loc), headers = {'Content-Type': 'application/json'})
                response_tmax.raise_for_status()
                response_tmin.raise_for_status()
                response_rain.raise_for_status()
                self.stdout.write(f"Populating weather data of {loc} location........")
                inst, created = WeatherDataModel.objects.get_or_create(location=loc,
									tmax=response_tmax.json(),
									tmin=response_tmin.json(),
									rainfall=response_rain.json())
                if created:
                    self.stdout.write(self.style.SUCCESS('Data Popluated !!!'))
                else:
                    self.stdout.write(self.style.HTTP_NOT_MODIFIED("Already exists !!!"))
            except RequestException as e:
                self.stderr.write(e)
            except Exception as e:
                self.stderr.write(e)
