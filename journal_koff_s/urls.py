from django.urls import path
from . import views

urlpatterns = [

    path('koff_s/', views.koff_s, name='koff_s'),

    path('create_koff_s_2pcalc/', views.create_koff_s_2pcalc, name='create_koff_s_2pcalc'),
    path('update_koff_s_2pcalc/<str:pk>', views.update_koff_s_2pcalc, name='update_koff_s_2pcalc'),
    path('delete_koff_s_2pcalc/<str:pk>', views.delete_koff_s_2pcalc, name='delete_koff_s_2pcalc'),

    path('create_koff_s_3pcalc/', views.create_koff_s_3pcalc, name='create_koff_s_3pcalc'),
    path('update_koff_s_3pcalc/<str:pk>', views.update_koff_s_3pcalc, name='update_koff_s_3pcalc'),
    path('delete_koff_s_3pcalc/<str:pk>', views.delete_koff_s_3pcalc, name='delete_koff_s_3pcalc'),

    path('create_koff_s_4pcalc/', views.create_koff_s_4pcalc, name='create_koff_s_4pcalc'),
    path('update_koff_s_4pcalc/<str:pk>', views.update_koff_s_4pcalc, name='update_koff_s_4pcalc'),
    path('delete_koff_s_4pcalc/<str:pk>', views.delete_koff_s_4pcalc, name='delete_koff_s_4pcalc'),

    path('create_koff_s_5pcalc/', views.create_koff_s_5pcalc, name='create_koff_s_5pcalc'),
    path('update_koff_s_5pcalc/<str:pk>', views.update_koff_s_5pcalc, name='update_koff_s_5pcalc'),
    path('delete_koff_s_5pcalc/<str:pk>', views.delete_koff_s_5pcalc, name='delete_koff_s_5pcalc'),

    path('create_koff_s_6pcalc/', views.create_koff_s_6pcalc, name='create_koff_s_6pcalc'),
    path('update_koff_s_6pcalc/<str:pk>', views.update_koff_s_6pcalc, name='update_koff_s_6pcalc'),
    path('delete_koff_s_6pcalc/<str:pk>', views.delete_koff_s_6pcalc, name='delete_koff_s_6pcalc'),

    path('create_koff_s_7pcalc/', views.create_koff_s_7pcalc, name='create_koff_s_7pcalc'),
    path('update_koff_s_7pcalc/<str:pk>', views.update_koff_s_7pcalc, name='update_koff_s_7pcalc'),
    path('delete_koff_s_7pcalc/<str:pk>', views.delete_koff_s_7pcalc, name='delete_koff_s_7pcalc'),


]