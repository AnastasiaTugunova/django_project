from rest_framework.serializers import ModelSerializer
from .models import Sensor, Measurement


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'info_temp']


class SensorInfoSerializer(ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']