from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorInfoSerializer


class CreateSensorView(ListCreateAPIView):
    """Добавляет датчик и получает список всех датчиков"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateView(ListCreateAPIView):
    """Добавляем измерения и получаем список всех измерений"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorChangeView(RetrieveUpdateAPIView):
    """Получаем данные конкретного датчика"""
    queryset = Sensor.objects.all()
    serializer_class = SensorInfoSerializer