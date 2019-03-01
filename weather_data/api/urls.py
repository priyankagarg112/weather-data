from django.urls import path


from .views import WeatherListAPIView


urlpatterns = [
    path('api/', WeatherListAPIView.as_view(), name='get_data')
]
