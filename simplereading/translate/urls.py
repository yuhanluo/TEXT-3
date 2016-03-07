from django.conf.urls import *
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
                url(r'^$', views.index, name='index'),
                url(r'^result/(?P<hard_text>[\w\W]*)/$', views.result, name='result'),
                
               ]
