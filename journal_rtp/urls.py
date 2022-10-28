from django.urls import path
from . import views

urlpatterns = [
    path('rtp/', views.rtp, name='rtp'),
    ]