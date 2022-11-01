from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),


    # path('oks/', views.oks, name='oks'),
    # path('create_oks/', views.createOKS, name='create_oks'),
    # path('update_oks/<str:pk>', views.updateOKS, name='update_oks'),
    # path('delete_oks/<str:pk>', views.deleteOKS, name='delete_oks'),


    # path('rtp/', views.rtp, name='rtp'),
    # path('rmo/', views.rmo, name='rmo'),
    # path('koff/', views.koff, name='koff'),
    path('koff_s/', views.koff_s, name='koff_s'),
    path('pgk/', views.pgk, name='pgk'),
]