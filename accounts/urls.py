from django.contrib.auth import views
from django.contrib.auth.views import LoginView
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.base, name = "base"),
    # url(' ', views.base, name='login'),
]


