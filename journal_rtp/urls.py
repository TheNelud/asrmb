from django.conf.urls import url
from django.urls import path
from . import views

from journal_rtp.rtp_views.rtp_1_view import *
from journal_rtp.rtp_views.rtp_2_view import *
from journal_rtp.rtp_views.rtp_3_view import *

from journal_rtp.rtp_views.rtp_rppp_1_view import *
from journal_rtp.rtp_views.rtp_rppp_2_view import *
from journal_rtp.rtp_views.rtp_rppp_3_view import *
from journal_rtp.rtp_views.rtp_rppp_4_view import *
from journal_rtp.rtp_views.rtp_rppp_51_view import *
from journal_rtp.rtp_views.rtp_rppp_52_view import *
from journal_rtp.rtp_views.rtp_rppp_6_view import *

from journal_rtp.rtp_views.rtp_nrtp_1_view import *
from journal_rtp.rtp_views.rtp_nrtp_2_view import *
from journal_rtp.rtp_views.rtp_nrtp_31_view import *
from journal_rtp.rtp_views.rtp_nrtp_32_view import *

from journal_rtp.rtp_views.rtp_nrppp_1_view import *
from journal_rtp.rtp_views.rtp_nrppp_2_view import *
from journal_rtp.rtp_views.rtp_nrppp_3_view import *
from journal_rtp.rtp_views.rtp_nrppp_4_view import *
from journal_rtp.rtp_views.rtp_nrppp_5_view import *
from journal_rtp.rtp_views.rtp_nrppp_6_view import *
from journal_rtp.rtp_views.rtp_nrppp_7_view import *
from journal_rtp.rtp_views.rtp_nrppp_8_view import *
from journal_rtp.rtp_views.rtp_nrppp_9_view import *
from journal_rtp.rtp_views.rtp_nrppp_10_view import *


urlpatterns = [
    path('', views.rtp, name='rtp'),

    url(r'^rtp_1/$', rtp_1_list, name='rtp_1_list'),
    url(r'^rtp_1_create/$', rtp_1_create, name='rtp_1_create'),
    url(r'^rtp_1_products/(?P<pk>\d+)/update/$', rtp_1_update, name='rtp_1_update'),
    url(r'^rtp_1_products/(?P<pk>\d+)/delete/$', rtp_1_delete, name='rtp_1_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^rtp_2/$', rtp_2_list, name='rtp_2_list'),
    url(r'^rtp_2_create/$', rtp_2_create, name='rtp_2_create'),
    url(r'^rtp_2_products/(?P<pk>\d+)/update/$', rtp_2_update, name='rtp_2_update'),
    url(r'^rtp_2_products/(?P<pk>\d+)/delete/$', rtp_2_delete, name='rtp_2_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^rtp_3/$', rtp_3_list, name='rtp_3_list'),
    url(r'^rtp_3_create/$', rtp_3_create, name='rtp_3_create'),
    url(r'^rtp_3_products/(?P<pk>\d+)/update/$', rtp_3_update, name='rtp_3_update'),
    url(r'^rtp_3_products/(?P<pk>\d+)/delete/$', rtp_3_delete, name='rtp_3_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^rppp_1/$', rppp_1_list, name='rppp_1_list'),
    url(r'^rppp_1_create/$', rppp_1_create, name='rppp_1_create'),
    url(r'^rppp_1_products/(?P<pk>\d+)/update/$', rppp_1_update, name='rppp_1_update'),
    url(r'^rppp_1_products/(?P<pk>\d+)/delete/$', rppp_1_delete, name='rppp_1_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^rppp_2/$', rppp_2_list, name='rppp_2_list'),
    url(r'^rppp_2_create/$', rppp_2_create, name='rppp_2_create'),
    url(r'^rppp_2_products/(?P<pk>\d+)/update/$', rppp_2_update, name='rppp_2_update'),
    url(r'^rppp_2_products/(?P<pk>\d+)/delete/$', rppp_2_delete, name='rppp_2_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^rppp_3/$', rppp_3_list, name='rppp_3_list'),
    url(r'^rppp_3_create/$', rppp_3_create, name='rppp_3_create'),
    url(r'^rppp_3_products/(?P<pk>\d+)/update/$', rppp_3_update, name='rppp_3_update'),
    url(r'^rppp_3_products/(?P<pk>\d+)/delete/$', rppp_3_delete, name='rppp_3_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^rppp_4/$', rppp_4_list, name='rppp_4_list'),
    url(r'^rppp_4_create/$', rppp_4_create, name='rppp_4_create'),
    url(r'^rppp_4_products/(?P<pk>\d+)/update/$', rppp_4_update, name='rppp_4_update'),
    url(r'^rppp_4_products/(?P<pk>\d+)/delete/$', rppp_4_delete, name='rppp_4_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^rppp_5/$', rppp5_1_list, name='rppp_5_list'),
    url(r'^rppp_5_create/$', rppp5_1_create, name='rppp5_1_create'),
    url(r'^rppp_5_products/(?P<pk>\d+)/update/$', rppp5_1_update, name='rppp5_1_update'),
    url(r'^rppp_5_products/(?P<pk>\d+)/delete/$', rppp5_1_delete, name='rppp5_1_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^rppp_5/$', rppp5_2_list, name='rppp_5_list'),
    url(r'^rppp_5_create/$', rppp5_2_create, name='rppp5_2_create'),
    url(r'^rppp_5_products/(?P<pk>\d+)/update/$', rppp5_2_update, name='rppp5_2_update'),
    url(r'^rppp_5_products/(?P<pk>\d+)/delete/$', rppp5_2_delete, name='rppp5_2_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^rppp_6/$', rppp_6_list, name='rppp_6_list'),
    url(r'^rppp_6_create/$', rppp_6_create, name='rppp_6_create'),
    url(r'^rppp_6_products/(?P<pk>\d+)/update/$', rppp_6_update, name='rppp_6_update'),
    url(r'^rppp_6_products/(?P<pk>\d+)/delete/$', rppp_6_delete, name='rppp_6_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrtp_1/$', nrtp_1_list, name='nrtp_1_list'),
    url(r'^nrtp_1_create/$', nrtp_1_create, name='nrtp_1_create'),
    url(r'^nrtp_1_products/(?P<pk>\d+)/update/$', nrtp_1_update, name='nrtp_1_update'),
    url(r'^nrtp_1_products/(?P<pk>\d+)/delete/$', nrtp_1_delete, name='nrtp_1_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrtp_2/$', nrtp_2_list, name='nrtp_2_list'),
    url(r'^nrtp_2_create/$', nrtp_2_create, name='nrtp_2_create'),
    url(r'^nrtp_2_products/(?P<pk>\d+)/update/$', nrtp_2_update, name='nrtp_2_update'),
    url(r'^nrtp_2_products/(?P<pk>\d+)/delete/$', nrtp_2_delete, name='nrtp_2_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrtp_3/$', nrtp3_1_list, name='nrtp_3_list'),
    url(r'^nrtp_3_create/$', nrtp3_1_create, name='nrtp3_1_create'),
    url(r'^nrtp_3_products/(?P<pk>\d+)/update/$', nrtp3_1_update, name='nrtp3_1_update'),
    url(r'^nrtp_3_products/(?P<pk>\d+)/delete/$', nrtp3_1_delete, name='nrtp3_1_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrtp_3/$', nrtp3_2_list, name='nrtp_3_list'),
    url(r'^nrtp_3_create/$', nrtp3_2_create, name='nrtp3_2_create'),
    url(r'^nrtp_3_products/(?P<pk>\d+)/update/$', nrtp3_2_update, name='nrtp3_2_update'),
    url(r'^nrtp_3_products/(?P<pk>\d+)/delete/$', nrtp3_2_delete, name='nrtp3_2_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrppp_1/$', nrppp_1_list, name='nrppp_1_list'),
    url(r'^nrppp_1_create/$', nrppp_1_create, name='nrppp_1_create'),
    url(r'^nrppp_1_products/(?P<pk>\d+)/update/$', nrppp_1_update, name='nrppp_1_update'),
    url(r'^nrppp_1_products/(?P<pk>\d+)/delete/$', nrppp_1_delete, name='nrppp_1_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrppp_2/$', nrppp_2_list, name='nrppp_2_list'),
    url(r'^nrppp_2_create/$', nrppp_2_create, name='nrppp_2_create'),
    url(r'^nrppp_2_products/(?P<pk>\d+)/update/$', nrppp_2_update, name='nrppp_2_update'),
    url(r'^nrppp_2_products/(?P<pk>\d+)/delete/$', nrppp_2_delete, name='nrppp_2_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrppp_3/$', nrppp_3_list, name='nrppp_3_list'),
    url(r'^nrppp_3_create/$', nrppp_3_create, name='nrppp_3_create'),
    url(r'^nrppp_3_products/(?P<pk>\d+)/update/$', nrppp_3_update, name='nrppp_3_update'),
    url(r'^nrppp_3_products/(?P<pk>\d+)/delete/$', nrppp_3_delete, name='nrppp_3_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrppp_4/$', nrppp_4_list, name='nrppp_4_list'),
    url(r'^nrppp_4_create/$', nrppp_4_create, name='nrppp_4_create'),
    url(r'^nrppp_4_products/(?P<pk>\d+)/update/$', nrppp_4_update, name='nrppp_4_update'),
    url(r'^nrppp_4_products/(?P<pk>\d+)/delete/$', nrppp_4_delete, name='nrppp_4_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrppp_5/$', nrppp_5_list, name='nrppp_5_list'),
    url(r'^nrppp_5_create/$', nrppp_5_create, name='nrppp_5_create'),
    url(r'^nrppp_5_products/(?P<pk>\d+)/update/$', nrppp_5_update, name='nrppp_5_update'),
    url(r'^nrppp_5_products/(?P<pk>\d+)/delete/$', nrppp_5_delete, name='nrppp_5_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrppp_6/$', nrppp_6_list, name='nrppp_6_list'),
    url(r'^nrppp_6_create/$', nrppp_6_create, name='nrppp_6_create'),
    url(r'^nrppp_6_products/(?P<pk>\d+)/update/$', nrppp_6_update, name='nrppp_6_update'),
    url(r'^nrppp_6_products/(?P<pk>\d+)/delete/$', nrppp_6_delete, name='nrppp_6_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrppp_7/$', nrppp_7_list, name='nrppp_7_list'),
    url(r'^nrppp_7_create/$', nrppp_7_create, name='nrppp_7_create'),
    url(r'^nrppp_7_products/(?P<pk>\d+)/update/$', nrppp_7_update, name='nrppp_7_update'),
    url(r'^nrppp_7_products/(?P<pk>\d+)/delete/$', nrppp_7_delete, name='nrppp_7_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrppp_8/$', nrppp_8_list, name='nrppp_8_list'),
    url(r'^nrppp_8_create/$', nrppp_8_create, name='nrppp_8_create'),
    url(r'^nrppp_8_products/(?P<pk>\d+)/update/$', nrppp_8_update, name='nrppp_8_update'),
    url(r'^nrppp_8_products/(?P<pk>\d+)/delete/$', nrppp_8_delete, name='nrppp_8_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrppp_9/$', nrppp_9_list, name='nrppp_9_list'),
    url(r'^nrppp_9_create/$', nrppp_9_create, name='nrppp_9_create'),
    url(r'^nrppp_9_products/(?P<pk>\d+)/update/$', nrppp_9_update, name='nrppp_9_update'),
    url(r'^nrppp_9_products/(?P<pk>\d+)/delete/$', nrppp_9_delete, name='nrppp_9_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),

    url(r'^nrppp_10/$', nrppp_10_list, name='nrppp_10_list'),
    url(r'^nrppp_10_create/$', nrppp_10_create, name='nrppp_10_create'),
    url(r'^nrppp_10_products/(?P<pk>\d+)/update/$', nrppp_10_update, name='nrppp_10_update'),
    url(r'^nrppp_10_products/(?P<pk>\d+)/delete/$', nrppp_10_delete, name='nrppp_10_delete'),
    # url(r'^hist_1.png/$', GraphsViewBar_p1, name='plot_pic'),
]