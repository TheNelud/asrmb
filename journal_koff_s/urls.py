from django.urls import path
from . import views

from journal_koff_s.koff_s_views.koff_s_p2calc_view import *
from journal_koff_s.koff_s_views.koff_s_p3calc_view import *
from journal_koff_s.koff_s_views.koff_s_p4calc_view import *
from journal_koff_s.koff_s_views.koff_s_p5calc_view import *
from journal_koff_s.koff_s_views.koff_s_p6calc_view import *
from journal_koff_s.koff_s_views.koff_s_p7calc_view import *

from django.conf.urls import url

urlpatterns = [

    path('', views.koff_s, name='koff_s'),

    url(r'^p2calc/$', p2calc_list, name='p2calc_list'),
    url(r'^p2calc_create/$', p2calc_create, name='p2calc_create'),
    url(r'^p2calc_products/(?P<pk>\d+)/update/$', p2calc_update, name='p2calc_update'),
    url(r'^p2calc_products/(?P<pk>\d+)/delete/$', p2calc_delete, name='p2calc_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^p3calc/$', p3calc_list, name='p3calc_list'),
    url(r'^p3calc_create/$', p3calc_create, name='p3calc_create'),
    url(r'^p3calc_products/(?P<pk>\d+)/update/$', p3calc_update, name='p3calc_update'),
    url(r'^p3calc_products/(?P<pk>\d+)/delete/$', p3calc_delete, name='p3calc_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^p4calc/$', p4calc_list, name='p4calc_list'),
    url(r'^p4calc_create/$', p4calc_create, name='p4calc_create'),
    url(r'^p4calc_products/(?P<pk>\d+)/update/$', p4calc_update, name='p4calc_update'),
    url(r'^p4calc_products/(?P<pk>\d+)/delete/$', p4calc_delete, name='p4calc_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^p5calc/$', p5calc_list, name='p5calc_list'),
    url(r'^p5calc_create/$', p5calc_create, name='p5calc_create'),
    url(r'^p5calc_products/(?P<pk>\d+)/update/$', p5calc_update, name='p5calc_update'),
    url(r'^p5calc_products/(?P<pk>\d+)/delete/$', p5calc_delete, name='p5calc_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^p6calc/$', p6calc_list, name='p6calc_list'),
    url(r'^p6calc_create/$', p6calc_create, name='p6calc_create'),
    url(r'^p6calc_products/(?P<pk>\d+)/update/$', p6calc_update, name='p6calc_update'),
    url(r'^p6calc_products/(?P<pk>\d+)/delete/$', p6calc_delete, name='p6calc_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^p7calc/$', p7calc_list, name='p7calc_list'),
    url(r'^p7calc_create/$', p7calc_create, name='p7calc_create'),
    url(r'^p7calc_products/(?P<pk>\d+)/update/$', p7calc_update, name='p7calc_update'),
    url(r'^p7calc_products/(?P<pk>\d+)/delete/$', p7calc_delete, name='p7calc_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    


]