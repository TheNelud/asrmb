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

    path('create_rtp_3/', views.create_rtp_3, name='create_rtp_3'),
    path('update_rtp_3/<str:pk>', views.update_rtp_3, name='update_rtp_3'),
    path('delete_rtp_3/<str:pk>', views.delete_rtp_3, name='delete_rtp_3'),
#-----------------------------------------------------------------------------
    path('create_rppp_1/', views.create_rppp_1, name='create_rppp_1'),
    path('update_rppp_1/<str:pk>', views.update_rppp_1, name='update_rppp_1'),
    path('delete_rppp_1/<str:pk>', views.delete_rppp_1, name='delete_rppp_1'),

    path('create_rppp_2/', views.create_rppp_2, name='create_rppp_2'),
    path('update_rppp_2/<str:pk>', views.update_rppp_2, name='update_rppp_2'),
    path('delete_rppp_2/<str:pk>', views.delete_rppp_2, name='delete_rppp_2'),

    path('create_rppp_3/', views.create_rppp_3, name='create_rppp_3'),
    path('update_rppp_3/<str:pk>', views.update_rppp_3, name='update_rppp_3'),
    path('delete_rppp_3/<str:pk>', views.delete_rppp_3, name='delete_rppp_3'),

    path('create_rppp_4/', views.create_rppp_4, name='create_rppp_4'),
    path('update_rppp_4/<str:pk>', views.update_rppp_4, name='update_rppp_4'),
    path('delete_rppp_4/<str:pk>', views.delete_rppp_4, name='delete_rppp_4'),

    path('create_rppp_51/', views.create_rppp_51, name='create_rppp_51'),
    path('update_rppp_51/<str:pk>', views.update_rppp_51, name='update_rppp_51'),
    path('delete_rppp_51/<str:pk>', views.delete_rppp_51, name='delete_rppp_51'),

    path('create_rppp_52/', views.create_rppp_52, name='create_rppp_52'),
    path('update_rppp_52/<str:pk>', views.update_rppp_52, name='update_rppp_52'),
    path('delete_rppp_52/<str:pk>', views.delete_rppp_52, name='delete_rppp_52'),

    path('create_rppp_6/', views.create_rppp_6, name='create_rppp_6'),
    path('update_rppp_6/<str:pk>', views.update_rppp_6, name='update_rppp_6'),
    path('delete_rppp_6/<str:pk>', views.delete_rppp_6, name='delete_rppp_6'),
#------------------------------------------------------------------------------------------

    path('create_nrtp_1/', views.create_nrtp_1, name='create_nrtp_1'),
    path('update_nrtp_1/<str:pk>', views.update_nrtp_1, name='update_nrtp_1'),
    path('delete_nrtp_1/<str:pk>', views.delete_nrtp_1, name='delete_nrtp_1'),

    path('create_nrtp_2/', views.create_nrtp_2, name='create_nrtp_2'),
    path('update_nrtp_2/<str:pk>', views.update_nrtp_2, name='update_nrtp_2'),
    path('delete_nrtp_2/<str:pk>', views.delete_nrtp_2, name='delete_nrtp_2'),

    path('create_nrtp_31/', views.create_nrtp_31, name='create_nrtp_31'),
    path('update_nrtp_31/<str:pk>', views.update_nrtp_31, name='update_nrtp_31'),
    path('delete_nrtp_31/<str:pk>', views.delete_nrtp_31, name='delete_nrtp_31'),

    path('create_nrtp_32/', views.create_nrtp_32, name='create_nrtp_32'),
    path('update_nrtp_32/<str:pk>', views.update_nrtp_32, name='update_nrtp_32'),
    path('delete_nrtp_32/<str:pk>', views.delete_nrtp_32, name='delete_nrtp_32'),

#--------------------------------------------------------------------------------------------

    path('create_nrppp_1/', views.create_nrppp_1, name='create_nrppp_1'),
    path('update_nrppp_1/<str:pk>', views.update_nrppp_1, name='update_nrppp_1'),
    path('delete_nrppp_1/<str:pk>', views.delete_nrppp_1, name='delete_nrppp_1'),

    path('create_nrppp_2/', views.create_nrppp_2, name='create_nrppp_2'),
    path('update_nrppp_2/<str:pk>', views.update_nrppp_2, name='update_nrppp_2'),
    path('delete_nrppp_2/<str:pk>', views.delete_nrppp_2, name='delete_nrppp_2'),

    path('create_nrppp_3/', views.create_nrppp_3, name='create_nrppp_3'),
    path('update_nrppp_3/<str:pk>', views.update_nrppp_3, name='update_nrppp_3'),
    path('delete_nrppp_3/<str:pk>', views.delete_nrppp_3, name='delete_nrppp_3'),

    path('create_nrppp_4/', views.create_nrppp_4, name='create_nrppp_4'),
    path('update_nrppp_4/<str:pk>', views.update_nrppp_4, name='update_nrppp_4'),
    path('delete_nrppp_4/<str:pk>', views.delete_nrppp_4, name='delete_nrppp_4'),

    path('create_nrppp_5/', views.create_nrppp_5, name='create_nrppp_5'),
    path('update_nrppp_5/<str:pk>', views.update_nrppp_5, name='update_nrppp_5'),
    path('delete_nrppp_5/<str:pk>', views.delete_nrppp_5, name='delete_nrppp_5'),

    path('create_nrppp_6/', views.create_nrppp_6, name='create_nrppp_6'),
    path('update_nrppp_6/<str:pk>', views.update_nrppp_6, name='update_nrppp_6'),
    path('delete_nrppp_6/<str:pk>', views.delete_nrppp_6, name='delete_nrppp_6'),

    path('create_nrppp_7/', views.create_nrppp_7, name='create_nrppp_7'),
    path('update_nrppp_7/<str:pk>', views.update_nrppp_7, name='update_nrppp_7'),
    path('delete_nrppp_7/<str:pk>', views.delete_nrppp_7, name='delete_nrppp_7'),

    path('create_nrppp_8/', views.create_nrppp_8, name='create_nrppp_8'),
    path('update_nrppp_8/<str:pk>', views.update_nrppp_8, name='update_nrppp_8'),
    path('delete_nrppp_8/<str:pk>', views.delete_nrppp_8, name='delete_nrppp_8'),

    path('create_nrppp_9/', views.create_nrppp_9, name='create_nrppp_9'),
    path('update_nrppp_9/<str:pk>', views.update_nrppp_9, name='update_nrppp_9'),
    path('delete_nrppp_9/<str:pk>', views.delete_nrppp_9, name='delete_nrppp_9'),

    path('create_nrppp_10/', views.create_nrppp_10, name='create_nrppp_10'),
    path('update_nrppp_10/<str:pk>', views.update_nrppp_10, name='update_nrppp_10'),
    path('delete_nrppp_10/<str:pk>', views.delete_nrppp_10, name='delete_nrppp_10'),

]