from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def str(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField()
    info_temp = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')