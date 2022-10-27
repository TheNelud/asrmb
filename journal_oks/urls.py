from django.urls import path
from . import views

urlpatterns = [
    path('oks/', views.oks, name='oks'),

    path('create_oks_p1/', views.create_oks_p1, name='create_oks_p1'),
    path('update_oks_p1/<str:pk>', views.update_oks_p1, name='update_oks_p1'),
    path('delete_oks_p1/<str:pk>', views.delete_oks_p1, name='delete_oks_p1'),

    path('create_oks_p2/', views.create_oks_p2, name='create_oks_p2'),
    path('update_oks_p2/<str:pk>', views.update_oks_p2, name='update_oks_p2'),
    path('delete_oks_p2/<str:pk>', views.delete_oks_p2, name='delete_oks_p2'),

    path('create_oks_p3/', views.create_oks_p3, name='create_oks_p3'),
    path('update_oks_p3/<str:pk>', views.update_oks_p3, name='update_oks_p3'),
    path('delete_oks_p3/<str:pk>', views.delete_oks_p3, name='delete_oks_p3'),

    path('create_oks_p4/', views.create_oks_p4, name='create_oks_p4'),
    path('update_oks_p4/<str:pk>', views.update_oks_p4, name='update_oks_p4'),
    path('delete_oks_p4/<str:pk>', views.delete_oks_p4, name='delete_oks_p4'),

    path('create_oks_p5/', views.create_oks_p5, name='create_oks_p5'),
    path('update_oks_p5/<str:pk>', views.update_oks_p5, name='update_oks_p5'),
    path('delete_oks_p5/<str:pk>', views.delete_oks_p5, name='delete_oks_p5'),

    path('create_oks_p6/', views.create_oks_p6, name='create_oks_p6'),
    path('update_oks_p6/<str:pk>', views.update_oks_p6, name='update_oks_p6'),
    path('delete_oks_p6/<str:pk>', views.delete_oks_p6, name='delete_oks_p6'),

    path('create_oks_p7/', views.create_oks_p7, name='create_oks_p7'),
    path('update_oks_p7/<str:pk>', views.update_oks_p7, name='update_oks_p7'),
    path('delete_oks_p7/<str:pk>', views.delete_oks_p7, name='delete_oks_p7'),

    path('create_oks_p8/', views.create_oks_p8, name='create_oks_p8'),
    path('update_oks_p8/<str:pk>', views.update_oks_p8, name='update_oks_p8'),
    path('delete_oks_p8/<str:pk>', views.delete_oks_p8, name='delete_oks_p8'),

    path('create_oks_p9/', views.create_oks_p9, name='create_oks_p9'),
    path('update_oks_p9/<str:pk>', views.update_oks_p9, name='update_oks_p9'),
    path('delete_oks_p9/<str:pk>', views.delete_oks_p9, name='delete_oks_p9'),

    path('create_oks_p10/', views.create_oks_p10, name='create_oks_p10'),
    path('update_oks_p10/<str:pk>', views.update_oks_p10, name='update_oks_p10'),
    path('delete_oks_p10/<str:pk>', views.delete_oks_p10, name='delete_oks_p10'),
]