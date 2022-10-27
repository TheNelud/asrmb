from django.urls import path
from . import views

urlpatterns = [
    path('oks/', views.oks, name='oks'),
    path('create_oks/', views.createOKS, name='create_oks'),
    path('update_oks/<str:pk>', views.updateOKS, name='update_oks'),
    path('delete_oks/<str:pk>', views.deleteOKS, name='delete_oks'),
]