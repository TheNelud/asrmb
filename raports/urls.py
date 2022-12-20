from . import views
from django.conf.urls import url
from raports.views import *
from django.urls import path




urlpatterns = [
    # path('', views.mar, name='raports'),

    url(r'^mar/$', views.mar, name='mar'),
    url(r'^mar/filter/$', views.filter_date_mar, name="filter_date_mar"),
    url(r'^mar/edit/$', views.mar_edit, name="mar_edit"),

    url(r'^mag/$', views.mag, name='mag'),
    url(r'^mag/filter/$', views.filter_date_mag, name="filter_date_mag"),
    url(r'^mag/calculate_balance/$', views.add_calculate_mag_balance, name='add_calculate_mag_balance'),
    url(r'^mag/edit/$', views.mag_edit, name="mag_edit"),

    
    url(r'^sar/$', views.sar, name='sar'),
    url(r'^sar/filter/$', views.filter_date_sar, name="filter_date_sar"),
    url(r'^sar/edit/$', views.sar_edit, name="sar_edit"),


    url(r'^sr_kgmk/$', views.sr_kgmk, name='sr_kgmk'),



   

    ]