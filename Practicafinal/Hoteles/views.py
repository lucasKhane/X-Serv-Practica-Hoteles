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

# Create your views here.
def principal(request):
    if request.method == "GET":
        return HttpResponse(get_template('index.html').render())
    else:
        return HttpResponse(get_template('error404NotFound.html').render())

def usuario(request):
    return HttpResponse("Index de la aplicacion")

def alojamientos(request):
    return HttpResponse("Index de la aplicacion")

def elalojamiento(request):
    return HttpResponse("Index de la aplicacion")

def usuario_XML(request):
    return HttpResponse("Index de la aplicacion")

def about(request):
    return HttpResponse("Index de la aplicacion")

def profile(request):
    return HttpResponse("Esta mierda va funcionando")

def loggedin(request):
    return render_to_response('registration/loggedin.html',
                              {'username': request.user.username})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')
    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
     return render_to_response('registration/registration_complete.html')
