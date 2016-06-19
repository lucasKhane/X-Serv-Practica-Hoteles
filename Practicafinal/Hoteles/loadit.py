
from models import Hotel
import sys
import urllib
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class myContentHandler(ContentHandler):
    def __init__(self):
        print "In __init__ on myContentHandler"
        self.contador = 0
        self.record = None;

        #La etiqueta de los diferentes campos del XML que se iran recorriendo
        self.tag = ""

        #Los campos de nuestro modelo
        self.nombreHotel = ""
        self.email = ""
        self.telefono = ""
        self.descripcion = ""
        self.wedUrl = ""
        self.direccion = ""
        self.latitude = ""
        self.longitude = ""
        self.imageUrl = ""
        #categoria y estrellas
        self.tipo = ""

        #Para buscar dentro de item
        self.tiene_imagenes = False
        self.tiene_categoria = False
        self.tiene_estrellas = False

    def startElement (self, name, attrs):
        print "In startElement on myContentHandler"
        self.contador = self.contador + 1
        print "Numero Hotel: ", self.contador
        self.tag = name

        if name == 'basicData':
            self.record = Hotel(nombreHotel="",email="",telefono="", descripcion="",webUrl="",direccion="",latitude="",longitude="",imageUrl="",categoria="",estrellas="")

        if name == "item":
            if attrs['name'] == "Categoria":
                self.tiene_categoria == True;
            if attrs['name'] == "SubCategoria":
                self.tiene_estrellas = True;

        if name == "media":
            if attrs['type'] == "image":
                self.tiene_imagenes = True

    def endElement (self, name):
        print "In endElement on myContentHandler"

        if self.tag == 'title':
            self.record.nombreHotel = self.nombreHotel
            self.record.save()

        if self.tag == 'email':
            self.record.email = self.email
            self.record.save()

        if self.tag == 'phone':
            self.record.telefono = self.telefono
            self.record.save()

        if self.tag == 'body':
            self.record.descripcion = self.descripcion
            self.record.save()

        if self.tag == 'web':
            self.record.webUrl = self.webUrl
            self.record.save()

        if self.tag == 'address':
            self.record.direccion = self.direccion
            self.record.save()

        if self.tag == 'latitude':
            self.record.latitude = self.latitude
            self.record.save()

        if self.tag == 'longitude':
            self.record.longitude = self.longitude
            self.record.save()

        if self.tag == 'url' and self.tiene_imagenes:
            self.record.imageUrl = self.imageUrl
            self.record.save()

        if self.tag == 'item' and self.tiene_estrellas:
            self.record.estrellas = self.tipo
            self.record.save()
            self.tiene_estrellas = False

        if self.tag == 'item' and self.tiene_categoria:
            self.record.categoria = self.tipo
            self.record.save()
            self.tiene_categoria = False

        self.tag = ""

    def characters (self, chars):
        print "In characters on myContentHandler"

        if self.tag == 'title':
            self.nombreHotel = chars

        if self.tag == 'email':
            self.email = chars

        if self.tag == 'phone':
            self.telefono = chars

        if self.tag == 'body':
            self.descripcion = chars

        if self.tag == 'web':
            self.webUrl = chars

        if self.tag == 'address':
            self.direccion = chars

        if self.tag == 'latitude':
            self.latitude = chars

        if self.tag == 'longitude':
            self.longitude = chars

        if self.tag == 'url':
            self.imageUrl = chars

        #categoria y estrellas
        if self.tag == 'item':
            self.tipo = chars
