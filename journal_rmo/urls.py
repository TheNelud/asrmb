from django.urls import path
from . import views

from journal_rmo.rmo_views.rmo_lg_view import *
from journal_rmo.rmo_views.rmo_md_view import *
from journal_rmo.rmo_views.rmo_ps_view import *
from django.conf.urls import url

urlpatterns = [
    path('', views.rmo, name='rmo'),

    url(r'^rmo_lg/$', rmo_lg_list, name='rmo_lg_list'),
    url(r'^rmo_lg_create/$', rmo_lg_create, name='rmo_lg_create'),
    url(r'^rmo_lg_products/(?P<pk>\d+)/update/$', rmo_lg_update, name='rmo_lg_update'),
    url(r'^rmo_lg_products/(?P<pk>\d+)/delete/$', rmo_lg_delete, name='rmo_lg_delete'),
    # url(r'^hist_1_lg.png/$', GraphsViewBar_lg, name='plot_pic_lg'),

    url(r'^rmo_md/$', rmo_md_list, name='rmo_md_list'),
    url(r'^rmo_md_create/$', rmo_md_create, name='rmo_md_create'),
    url(r'^rmo_md_products/(?P<pk>\d+)/update/$', rmo_md_update, name='rmo_md_update'),
    url(r'^rmo_md_products/(?P<pk>\d+)/delete/$', rmo_md_delete, name='rmo_md_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^rmo_ps/$', rmo_ps_list, name='rmo_ps_list'),
    url(r'^rmo_ps_create/$', rmo_ps_create, name='rmo_ps_create'),
    url(r'^rmo_ps_products/(?P<pk>\d+)/update/$', rmo_ps_update, name='rmo_ps_update'),
    url(r'^rmo_ps_products/(?P<pk>\d+)/delete/$', rmo_ps_delete, name='rmo_ps_delete'),
    # url(r'^hist_1_ps.png/$', GraphsViewBar_ps, name='plot_pic_ps'),

]
