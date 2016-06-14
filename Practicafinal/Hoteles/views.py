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
#import parsehotel

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

def alojamientos(request):
    return HttpResponse("alojamientos")

def elalojamiento(request):
    return HttpResponse("elalojamiento")

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
            return HttpResponseRedirect("accounts/login/")
    else:
        return HttpResponse(get_template('error404NotFound.html').render())

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
