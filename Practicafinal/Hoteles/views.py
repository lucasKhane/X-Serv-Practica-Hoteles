from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from itertools import chain

from models import Hotel

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from loadit import myContentHandler

import urllib2

#template
#<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
#<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
#<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-multiselect/0.9.13/js/bootstrap-multiselect.min.js"></script>
#<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-multiselect/0.9.13/css/bootstrap-multiselect.css">

#<link rel="stylesheet" type="text/css" href="{% static 'bootstrap-3.3.6-dist/css/bootstrap.min.css' %}" />
#<script language="JavaScript" type="text/javascript" src="{% static 'bootstrap-3.3.6-dist/js/bootstrap.min.js' %}"></script>
#<link rel="stylesheet" type="text/css" href="{% static 'bootstrap-multiselect/bootstrap-multiselect.css' %}" />
#<script language="JavaScript" type="text/javascript" src="{% static 'bootstrap-multiselect/bootstrap-multiselect.js' %}"></script>


# Create your views here.
def principal(request):
    if request.method == "GET":
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        context = {'user': username}
        return HttpResponse(get_template('index.html').render(context))
    else:
        return HttpResponse(get_template('error404NotFound.html').render())

def reloadhotel(request):
    return HttpResponse("ReloadHotel")

def about(request):
    if request.method == "GET":
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        context = {'user': username}
        return HttpResponse(get_template('about.html').render(context))
    else:
        return HttpResponse(get_template('error404NotFound.html').render())

def user_profile(request, usuario):
    if request.method == "GET":
        username = None
        if request.user.is_authenticated():
            username = request.user.username
            context = {'user': username}
            return HttpResponse(get_template('user_profile.html').render(context))
        else:
            #CAMBIAR
            return HttpResponseRedirect("/")
    else:
        return HttpResponse(get_template('error404NotFound.html').render())

def rechargelang(request):
    print ("Refresing...")
    #Crea un nuevo objeto parser y lo devuelve
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)
    fil = urllib2.urlopen( 'http://cursosweb.github.io/etc/alojamientos_es.xml')
    theParser.parse(fil)
    return HttpResponseRedirect("alojamientos")

def alojamientos(request):
    if request.method == 'GET':
        listaHoteles = Hotel.objects.all()
        numHoteles = len(listaHoteles)
        context = {'listaHoteles': listaHoteles, 'numHoteles': numHoteles}
        return render_to_response('alojamientos.html', context, context_instance = RequestContext(request))

    elif request.method == 'POST':
        listaOpcionesFiltro = request.POST.getlist("multiple")
        listaHoteles = Hotel.objects.all()
        listaFiltrado = Hotel.objects.all().filter(estrellas="Initialize var")
        for i in range(len(listaOpcionesFiltro)):
            if  listaOpcionesFiltro[i].find("estrella")!= -1:
                listaFiltrado = listaFiltrado | listaHoteles.filter(estrellas=listaOpcionesFiltro[i])
            else:
                listaFiltrado = listaFiltrado | listaHoteles.filter(categoria=listaOpcionesFiltro[i])
        numHoteles = len(listaFiltrado)

        context = {'listaHoteles': listaFiltrado, 'numHoteles': numHoteles}
        return render_to_response('alojamientos.html', context, context_instance = RequestContext(request))

def elalojamiento(request, id):
    if request.method == 'GET':
        thatHotel = Hotel.objects.all().filter(id=id)
        arrayNumFotos = range(1,thatHotel[0].imageNum)
        auxStrFotos = str(thatHotel[0].imageUrls)
        auxStrFotos = auxStrFotos.replace("[","")
        auxStrFotos = auxStrFotos.replace("]","")
        auxStrFotos = auxStrFotos.replace("'","")
        auxStrFotos = auxStrFotos.strip()
        arrayFotos = auxStrFotos.split(",")
        
        for i in range(len(arrayFotos)):
            arrayFotos[i]= arrayFotos[i].replace("u","",1)
        firstFoto = arrayFotos.pop(0)

        context = {'thatHotel': thatHotel[0], 'arrayNumFotos': arrayNumFotos, 'firstFoto': firstFoto, 'arrayFotos': arrayFotos}
        return render_to_response('elalojamiento.html', context, context_instance = RequestContext(request))

    elif request.method == 'POST':
        listaOpcionesFiltro = request.POST.getlist("multiple")
        listaHoteles = Hotel.objects.all()
        listaFiltrado = Hotel.objects.all().filter(estrellas="Initialize var")
        for i in range(len(listaOpcionesFiltro)):
            if  listaOpcionesFiltro[i].find("estrella")!= -1:
                listaFiltrado = listaFiltrado | listaHoteles.filter(estrellas=listaOpcionesFiltro[i])
            else:
                listaFiltrado = listaFiltrado | listaHoteles.filter(categoria=listaOpcionesFiltro[i])
        numHoteles = len(listaFiltrado)

        context = {'listaHoteles': listaFiltrado, 'numHoteles': numHoteles}
        return render_to_response('alojamiento.html', context, context_instance = RequestContext(request))

def user_XML(request, usuario):
    return HttpResponse("user_XML")

def loggedin(request):
    return render_to_response('registration/loggedin.html',
                              {'username': request.user.username})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print "Esta autenticado el usuario tras registrarse?: ", request.user.username
            return HttpResponseRedirect('/accounts/register/complete')
    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
     return render_to_response('registration/registration_complete.html')

def XMLlinks(request):
    return render_to_response('XMLlinks.html')
