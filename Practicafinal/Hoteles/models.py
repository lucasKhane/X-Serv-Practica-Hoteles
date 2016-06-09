from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hotel (models.Model):
    nombreHotel = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    imageSource = models.CharField(max_length=200)
    webSource = models.CharField(max_length=200)
    numComentarios = models.IntegerField()

class PersonalPage (models.Model):
    usuario = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
