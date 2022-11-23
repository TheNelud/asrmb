from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    # path('', views.mar, name='raports'),

    url(r'^mar/$', views.mar, name='mar'),
    url(r'^mag/$', views.mag, name='mag'),
    url(r'^sar/$', views.sar, name='sar'),
    ]