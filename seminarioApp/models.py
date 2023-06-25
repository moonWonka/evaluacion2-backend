from django.db import models

# Create your models here.


class Seminarios(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha = models.DateField()
    organizacion = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=100)
