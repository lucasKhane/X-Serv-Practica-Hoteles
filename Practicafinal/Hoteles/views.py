from datetime import datetime
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

from models import Comentario
from models import CSS
from models import Hotel
from models import PersonalHotel
from models import PersonalPage

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
        try:
            listaHoteles = Hotel.objects.all()
        except Hotel.DoesNotExist:
            print "No hay hoteles en la base de datos"
            listaHoteles = {}
        if request.user.is_authenticated():
            username=request.user.username
            try:
                personalPages = PersonalPage.objects.all()
            except PersonalPage.DoesNotExist:
                print "No existe aun paginas personales. No debe haber usuarios registrados"
                personalPages = {}
            context = {'user': username, 'personalPages': personalPages, 'listaHoteles': listaHoteles[0:10]}
            return render_to_response('principal.html', context, context_instance = RequestContext(request))
        else:
            context = {'listaHoteles': listaHoteles[0:10]}
            return render_to_response('principal.html', context, context_instance = RequestContext(request))
    else:
        return HttpResponse(get_template('error404NotFound.html').render())

def about(request):
    if request.method == "GET":
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        context = {'user': username}
        return HttpResponse(get_template('about.html').render(context))
    else:
        return HttpResponse(get_template('error404NotFound.html').render())

def cleanword(word):
    auxStrFotos = str(word)
    auxStrFotos = auxStrFotos.replace("[","")
    auxStrFotos = auxStrFotos.replace("]","")
    auxStrFotos = auxStrFotos.replace("'","")
    auxStrFotos = auxStrFotos.strip()
    auxStrFotos = auxStrFotos.replace("u","",1)
    return auxStrFotos

def user_profile(request, usuario):
    if request.method == "GET":
        username = None
        try:
            personalHotel = PersonalHotel.objects.get(user=usuario)
        except PersonalHotel.DoesNotExist:
            print "Aun no hay hoteles seleccionados para este usuario"
            personalHotel = {}
        if request.user.is_authenticated():
            username = request.user.username
            #Siempre existira nuestra pagina personal si estamos logueados
            personalPage = PersonalPage.objects.get(user=username)
            context = {'user': username, 'personalPage': personalPage, 'personalHotel': personalHotel}
            return render_to_response('user_profile.html', context, context_instance = RequestContext(request))
        else:
            #Siempre existira nuestra pagina personal si estamos logueados
            personalPage = PersonalPage.objects.get(user=username)
            context = {'personalPage': personalPage, 'personalHotel': personalHotel}
            return render_to_response('user_profile.html', context, context_instance = RequestContext(request))
    elif request.method == 'POST':
        marcossize = request.POST.getlist("marcossize")
        marcoscolor = request.POST.getlist("marcoscolor")
        colorfondo = request.POST.getlist("colorfondo")
        tamanioletra = request.POST.getlist("tamanioletra")
        username = request.user.username
        personalPage = PersonalPage.objects.get(user=username)
        if marcossize != []:
            personalPage.css.grosormarcos = cleanword(marcossize);
        elif marcoscolor != []:
            personalPage.css.colormarcos = cleanword(marcoscolor);
        elif colorfondo != []:
            personalPage.css.colordefondo = cleanword(colorfondo);
        elif tamanioletra != []:
            personalPage.css.tamanioletra = cleanword(tamanioletra);
        else:
            print("ERROR: consulta a tu programador de confianza. En views.user_profile")
        personalPage.css.save()
        personalPage.save()
        try:
            personalHotel = PersonalHotel.objects.get(user=usuario)
        except PersonalHotel.DoesNotExist:
            personalHotel = {}
        context = {'user': username, 'personalPage': personalPage, 'personalHotel':personalHotel}
        return render_to_response('user_profile.html', context, context_instance = RequestContext(request))

def rechargelang(request):
    print ("Refresing...")
    #Crea un nuevo objeto parser y lo devuelve
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)
    fil = urllib2.urlopen('http://cursosweb.github.io/etc/alojamientos_es.xml')
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

        if request.user.is_authenticated():
            username=request.user.username
            try:
                personalPage = PersonalPage.objects.get(user=username)
                context = {'user': username, 'personalPage': personalPage, 'listaHoteles': listaFiltrado, 'numHoteles': numHoteles}
                return render_to_response('alojamientos.html', context, context_instance = RequestContext(request))
            except PersonalPage.DoesNotExist:
                print "Error. No existe pagina de usuario de usuario logueado"
                return HttpResponse(get_template('error404NotFound.html').render())
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
        if request.user.is_authenticated():
            username=request.user.username
            try:
                personalPages = PersonalPage.objects.all()
            except PersonalPage.DoesNotExist:
                print "No existe aun paginas personales. No debe haber usuarios registrados"
                personalPages = {}
            try:
                comentarios = Comentario.objects.get(idhotel=id)
            except Comentario.DoesNotExist:
                comentarios = {}
            context = {'user': username, 'personalPages': personalPages,'thatHotel': thatHotel[0], 'arrayNumFotos': arrayNumFotos,
                    'firstFoto': firstFoto, 'arrayFotos': arrayFotos, 'comentarios': comentarios}
            return render_to_response('elalojamiento.html', context, context_instance = RequestContext(request))
        context = {'user': username, 'personalPages': personalPages,'thatHotel': thatHotel[0], 'arrayNumFotos': arrayNumFotos,
                'firstFoto': firstFoto, 'arrayFotos': arrayFotos, 'comentarios': comentarios}
        return render_to_response('elalojamiento.html', context, context_instance = RequestContext(request))
    elif request.method == 'POST':
        if request.user.is_authenticated():
            #Enviar un comentario
            comentario = request.POST.get("addcomment")
            username = request.user.username
            thatHotel = Hotel.objects.get(id=id)
            date = datetime.now()
            nuevoComentario = Comentario(idhotel=id, user=username, contenido=comentario, date=date)
            nuevoComentario.save(request)
        return HttpResponseRedirect("elalojamiento/"+id)

def user_XML(request, usuario):
    return HttpResponse("user_XML")

def loggedin(request):
    #Creamos la pagina personal de usuario en la base de datos
    #No se puede crear en el register porque no puedes hacer el request.username hasta que no te logueas
    username=request.user.username
    try:
        aux = PersonalPage.objects.get(user=username)
    except PersonalPage.DoesNotExist:
        record1 = CSS(grosormarcos="2px", colormarcos="#777", colordefondo="#e6ffff", tamanioletra="")
        record1.save()
        record2 = PersonalPage(user=username, tittlePage="Pagina de "+username, css=record1)
        record2.save(request)
        return render_to_response('registration/loggedin.html',
                                  {'username': request.user.username})
    return render_to_response('registration/loggedin.html',
                              {'username': request.user.username})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=request.user.username
            print "Esta autenticado el usuario tras registrarse?: ", username
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
