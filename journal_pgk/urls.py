from django.urls import path
from . import views

urlpatterns = [

    path('', views.pgk, name='pgk'),

    path('insert', views.insert, name='insert'),

    path('create_pgk', views.create_pgk, name='create_pgk'),
    path('update_pgk/<str:pk>', views.update_pgk, name='update_pgk'),
    path('delete_pgk/<str:pk>', views.delete_pgk, name='delete_pgk'),

]