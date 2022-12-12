from django.db import models
import simplekml
from math import radians, cos, sin, pi
from .utils import kmlFile
# Create your models here.

class Cell(models.Model):
    id_code = models.CharField('Cell ID Code',max_length=50)
    latitude = models.DecimalField('LAT',max_digits=22,decimal_places=16)
    longitude = models.DecimalField('LONG',max_digits=22,decimal_places=16)
    azimuth = models.IntegerField('Azimuth', null=True)
    radius = models.IntegerField('Radius [meters]', null=True)
    aperture = models.FloatField('Angle of aperture', null=True, default=60)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_code

    def data_to_kml(self):
        kml = kmlFile(self.id_code, self.latitude, self.longitude, self.radius, self.azimuth, self.aperture)
        return kml