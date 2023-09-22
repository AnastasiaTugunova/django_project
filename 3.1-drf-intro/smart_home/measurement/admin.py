from django.contrib import admin
from .models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    sensor_list = ['id', 'name', 'description']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    measurement_list = ['temperature', 'info_temp']