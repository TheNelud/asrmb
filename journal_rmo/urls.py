from django.urls import path
from . import views

urlpatterns = [
    path('rmo/', views.rmo, name='rmo'),

    path('create_rmo_p5/', views.create_rmo_p5, name='create_rmo_p5'),
    path('update_rmo_p5/<str:pk>', views.update_rmo_p5, name='update_rmo_p5'),
    path('delete_rmo_p5/<str:pk>', views.delete_rmo_p5, name='delete_rmo_p5'),

    path('create_rmo_p6/', views.create_rmo_p6, name='create_rmo_p6'),
    path('update_rmo_p6/<str:pk>', views.update_rmo_p6, name='update_rmo_p6'),
    path('delete_rmo_p6/<str:pk>', views.delete_rmo_p6, name='delete_rmo_p6'),

    path('create_rmo_ps/', views.create_rmo_ps, name='create_rmo_ps'),
    path('update_rmo_ps/<str:pk>', views.update_rmo_ps, name='update_rmo_ps'),
    path('delete_rmo_ps/<str:pk>', views.delete_rmo_ps, name='delete_rmo_ps'),

]
