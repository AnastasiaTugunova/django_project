from django.urls import path
from .views import CreateSensorView, MeasurementCreateView, SensorChangeView

urlpatterns = [
    path('sensors/', CreateSensorView.as_view()),
    path('sensors/<pk>/', SensorChangeView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
