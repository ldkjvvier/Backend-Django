from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    reorder = models.IntegerField()

class Proyecto(models.Model):
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    prioridad = models.IntegerField()