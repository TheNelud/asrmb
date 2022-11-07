from django.urls import path
from . import views
# from journal_oks.oks_views import oks_p1_view
from journal_oks.oks_views.oks_p1_view import *
from journal_oks.oks_views.oks_p2_view import *
from journal_oks.oks_views.oks_p3_view import *
from journal_oks.oks_views.oks_p4_view import *
from journal_oks.oks_views.oks_p5_view import *
from journal_oks.oks_views.oks_p6_view import *
from journal_oks.oks_views.oks_p7_view import *
from journal_oks.oks_views.oks_p8_view import *
from journal_oks.oks_views.oks_p9_view import *
from journal_oks.oks_views.oks_p10_view import *
from django.conf.urls import url

urlpatterns = [
    path('', views.oks, name='oks'),


    url(r'^oks_p1/$', oks_p1_list, name='oks_p1_list'),
    url(r'^oks_p1_create/$', oks_p1_create, name='oks_p1_create'),
    url(r'^oks_p1_products/(?P<pk>\d+)/update/$', oks_p1_update, name='oks_p1_update'),
    url(r'^oks_p1_products/(?P<pk>\d+)/delete/$', oks_p1_delete, name='oks_p1_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),


    url(r'^oks_p2/$', oks_p2_list, name='oks_p2_list'),
    url(r'^oks_p2_create/$', oks_p2_create, name='oks_p2_create'),
    url(r'^oks_p2_products/(?P<pk>\d+)/update/$', oks_p2_update, name='oks_p2_update'),
    url(r'^oks_p2_products/(?P<pk>\d+)/delete/$', oks_p2_delete, name='oks_p2_delete'),
    # url(r'^hist_2.png/$', GraphsViewBar_p2, name='plot_pic'),


    url(r'^oks_p3/$', oks_p3_list, name='oks_p3_list'),
    url(r'^oks_p3_create/$', oks_p3_create, name='oks_p3_create'),
    url(r'^oks_p3_products/(?P<pk>\d+)/update/$', oks_p3_update, name='oks_p3_update'),
    url(r'^oks_p3_products/(?P<pk>\d+)/delete/$', oks_p3_delete, name='oks_p3_delete'),
    # url(r'^hist_2.png/$', GraphsViewBar_p2, name='plot_pic'),

    url(r'^oks_p4/$', oks_p4_list, name='oks_p4_list'),
    url(r'^oks_p4_create/$', oks_p4_create, name='oks_p4_create'),
    url(r'^oks_p4_products/(?P<pk>\d+)/update/$', oks_p4_update, name='oks_p4_update'),
    url(r'^oks_p4_products/(?P<pk>\d+)/delete/$', oks_p4_delete, name='oks_p4_delete'),
    # url(r'^hist_2.png/$', GraphsViewBar_p2, name='plot_pic'),

    url(r'^oks_p5/$', oks_p5_list, name='oks_p5_list'),
    url(r'^oks_p5_create/$', oks_p5_create, name='oks_p5_create'),
    url(r'^oks_p5_products/(?P<pk>\d+)/update/$', oks_p5_update, name='oks_p5_update'),
    url(r'^oks_p5_products/(?P<pk>\d+)/delete/$', oks_p5_delete, name='oks_p5_delete'),
    # url(r'^hist_2.png/$', GraphsViewBar_p2, name='plot_pic'),

    url(r'^oks_p6/$', oks_p6_list, name='oks_p6_list'),
    url(r'^oks_p6_create/$', oks_p6_create, name='oks_p6_create'),
    url(r'^oks_p6_products/(?P<pk>\d+)/update/$', oks_p6_update, name='oks_p6_update'),
    url(r'^oks_p6_products/(?P<pk>\d+)/delete/$', oks_p6_delete, name='oks_p6_delete'),
    # url(r'^hist_2.png/$', GraphsViewBar_p2, name='plot_pic'),

    url(r'^oks_p7/$', oks_p7_list, name='oks_p7_list'),
    url(r'^oks_p7_create/$', oks_p7_create, name='oks_p7_create'),
    url(r'^oks_p7_products/(?P<pk>\d+)/update/$', oks_p7_update, name='oks_p7_update'),
    url(r'^oks_p7_products/(?P<pk>\d+)/delete/$', oks_p7_delete, name='oks_p7_delete'),
    # url(r'^hist_2.png/$', GraphsViewBar_p2, name='plot_pic'),

    url(r'^oks_p8/$', oks_p8_list, name='oks_p8_list'),
    url(r'^oks_p8_create/$', oks_p8_create, name='oks_p8_create'),
    url(r'^oks_p8_products/(?P<pk>\d+)/update/$', oks_p8_update, name='oks_p8_update'),
    url(r'^oks_p8_products/(?P<pk>\d+)/delete/$', oks_p8_delete, name='oks_p8_delete'),
    # url(r'^hist_2.png/$', GraphsViewBar_p2, name='plot_pic'),

    url(r'^oks_p9/$', oks_p9_list, name='oks_p9_list'),
    url(r'^oks_p9_create/$', oks_p9_create, name='oks_p9_create'),
    url(r'^oks_p9_products/(?P<pk>\d+)/update/$', oks_p9_update, name='oks_p9_update'),
    url(r'^oks_p9_products/(?P<pk>\d+)/delete/$', oks_p9_delete, name='oks_p9_delete'),
    # url(r'^hist_2.png/$', GraphsViewBar_p2, name='plot_pic'),

    url(r'^oks_p10/$', oks_p10_list, name='oks_p10_list'),
    url(r'^oks_p10_create/$', oks_p10_create, name='oks_p10_create'),
    url(r'^oks_p10_products/(?P<pk>\d+)/update/$', oks_p10_update, name='oks_p10_update'),
    url(r'^oks_p10_products/(?P<pk>\d+)/delete/$', oks_p10_delete, name='oks_p10_delete'),
    # url(r'^hist_2.png/$', GraphsViewBar_p2, name='plot_pic'),


    
]