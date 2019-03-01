from django.test import TestCase
from django.core.management import call_command

from rest_framework.test import APITestCase
from rest_framework import status

from io import StringIO
import requests

class TestWeatherListAPIView(APITestCase):

    def test_weather_data(self):
        url = 'http://127.0.0.1:8000/api/'
        try:
            res = requests.get(url)
            self.assertEqual(res.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
            err_response= 'All parameters are not found in the url.'
            self.assertIn(err_response, res.json()['Error'])
            args = {'start_date':'27-02-1999',
		    'end_date':'01-02-2019',
		    'metric_type':'Rainfall',
		    'location':'UK'
		   }
            res = requests.get(url,params=args)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertIsInstance(res.json()['Result'], list)
        except Exception as e:
            print(e)

class TestCustomManagementCommand(TestCase):

    def test_custom_command(self):
        out = StringIO()
        call_command('store_data',stdout=out)
        self.assertIn('Populating', out.getvalue())

