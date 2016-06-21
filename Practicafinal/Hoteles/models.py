from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hotel (models.Model):
    nombreHotel = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    telefono = models.CharField(max_length=200, default="")
    descripcion = models.CharField(max_length=200, default="")
    webUrl = models.CharField(max_length=200, default="")
    direccion = models.CharField(max_length=200, default="")
    latitude = models.CharField(max_length=200, default="")
    longitude = models.CharField(max_length=200, default="")
    imageNum = models.IntegerField(default=0)
    imageUrls = models.CharField(max_length=200, default="")
    categoria = models.CharField(max_length=200, default="")
    estrellas = models.CharField(max_length=200, default="")
    #numComentarios = models.IntegerField()

class PersonalPage (models.Model):
    usuario = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
