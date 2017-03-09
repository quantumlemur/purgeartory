from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = [
    url(r'loggedin$', views.loggedin, name='loggedin')
   # url(r'$', views.home, name='home'),
   # url(r'whoami$', views.home, name='whoami'),
]