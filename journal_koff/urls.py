from django.urls import path
from . import views


urlpatterns = [
    path('koff/', views.koff, name='koff'),
    ]