from django.urls import path
from . import views

urlpatterns = [

    path('', views.pgk, name='pgk'),

    

]