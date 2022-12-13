from django.urls import path,register_converter
from . import views
from datetime import datetime
from django.conf.urls import url


from raports.views import *

# from raports.raports_views.sr_kgmk_views import *


class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')
# /<yyyy:date>/
urlpatterns = [
    # path('', views.mar, name='raports'),

    url(r'^mar/$', views.mar, name='mar'),
    url(r'^mag/$', views.mag, name='mag'),
    url(r'^sar/$', views.sar, name='sar'),
    url(r'^sar/<yyyy:date>/$', views.filter_date_sar, name="filter_date_sar"),


    url(r'^sr_kgmk/$', views.sr_kgmk, name='sr_kgmk'),


    url(r'^mag/mag_create/$', views.mag_create, name='mag_create'),
    ]