from django.urls import path
from . import views
from django.conf.urls import url

from raports.views import *

# from raports.raports_views.sr_kgmk_views import *


urlpatterns = [
    # path('', views.mar, name='raports'),

    url(r'^mar/$', views.mar, name='mar'),
    url(r'^mag/$', views.mag, name='mag'),
    url(r'^sar/$', views.sar, name='sar'),
    url(r'^sr_kgmk/$', views.sr_kgmk, name='sr_kgmk'),


    url(r'^mag/mag_create/$', mag_create, name='mag_create'),
    ]