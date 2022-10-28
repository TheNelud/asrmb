from django.urls import path
from . import views

urlpatterns = [
    path('rtp/', views.rtp, name='rtp'),

    path('create_rtp_1/', views.create_rtp_1, name='create_rtp_1'),
    path('update_rtp_1/<str:pk>', views.update_rtp_1, name='update_rtp_1'),
    path('delete_rtp_1/<str:pk>', views.delete_rtp_1, name='delete_rtp_1'),

    path('create_rtp_2/', views.create_rtp_2, name='create_rtp_2'),
    path('update_rtp_2/<str:pk>', views.update_rtp_2, name='update_rtp_2'),
    path('delete_rtp_2/<str:pk>', views.delete_rtp_2, name='delete_rtp_2'),
    ]