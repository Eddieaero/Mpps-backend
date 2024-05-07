from django.contrib import admin
from django.urls import path
from mpps_api.views import RegisterView
from mpps_api.views import UploadView
from mpps_api.views import TransitPassView





urlpatterns = [
    # path('SensorData/', SensorDataView.as_view())
    # path('SensorData/', SensorDataView.as_view())
    # path('sensorData/', SensorDataView.as_view(), name='sensor-data'),
    # path('weatherData/', WeatherDataView.as_view(), name='weather-data'),
    # path('sensorData/<int:pk>/', SensorDataView.as_view(), name='sensor-data-detail'),
    # path('weatherData/<int:pk>/', WeatherDataView.as_view(), name='weather-data-detail')
    path('register/', RegisterView.as_view(), name='register'),
    path('uploadDocument/', UploadView.as_view(), name='upload'),
    path('transitPassApplication/', TransitPassView.as_view(), name='transit-pass'),


]