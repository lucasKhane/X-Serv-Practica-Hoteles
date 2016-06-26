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
    firstFoto = models.CharField(max_length=200, default="")
    numcomentarios = models.IntegerField(default=0)

class Comentario (models.Model):
    user = models.CharField(max_length=200, default="")
    date = models.DateField(auto_now=True)
    contenido = models.CharField(max_length=300, default="")
    idhotel = models.CharField(max_length=200, default="")

class CSS (models.Model):
    grosormarcos = models.CharField(max_length=200, default="")
    colormarcos = models.CharField(max_length=200, default="")
    colordefondo = models.CharField(max_length=200, default="")
    tamanioletra = models.CharField(max_length=200, default="")

class PersonalPage (models.Model):
    user = models.CharField(max_length=200, default="")
    tittlePage = models.CharField(max_length=200)
    css = models.ForeignKey(CSS, default="")

class PersonalHotel (models.Model):
    user=models.CharField(max_length=300,default="")
    hotel=models.ForeignKey(Hotel)
    date = models.DateField(auto_now=True)
