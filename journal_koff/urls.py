from django.urls import path
from . import views


urlpatterns = [
    path('', views.koff, name='koff'),
    ]