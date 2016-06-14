"""Practicafinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from Hoteles import views

urlpatterns = [
    url(r'^$', 'Hoteles.views.principal'),
    url(r'^index.html$', 'Hoteles.views.principal'),
    url(r'^alojamientos$', 'Hoteles.views.alojamientos'),
    url(r'^alojamientos/(\d+)', 'Hoteles.views.elalojamiento'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about$', 'Hoteles.views.about'),

    #url(r'^(.*)$', 'Hoteles.views.usuario'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^accounts/loggedin/$', 'Hoteles.views.loggedin', name='loggedin'),
    url(r'^accounts/register/$', 'Hoteles.views.register', name='register'),
    url(r'^accounts/register/complete/$', 'Hoteles.views.registration_complete', name='registration_complete'),
    url(r'^XMLlinks$', 'Hoteles.views.XMLlinks', name='XMLlinks'),
    url(r'^(.*)$', 'Hoteles.views.user_profile', name='profile'),
    #url(r'^(.*)/xml$', 'Hoteles.views.user_XML', name='user_XML'),
]
