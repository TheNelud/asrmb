from django.shortcuts import render, redirect, get_object_or_404
from journal_rmo.models import *
from journal_rmo.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io


import plotly.graph_objs as go
import plotly.express as px


def graphs_ls():
    data_rmo_ps = Losses_gas.objects.all()
    x_data = [item.update_date for item in data_rmo_ps]
    y_data = [item.fakel for item in data_rmo_ps]

    print(x_data)
    print(y_data)
   
    
    figure = go.Figure(px.line(x=x_data, y=y_data, title="Потери газа")).to_html()
   
    return figure

def rmo_lg_list(request):
    rmo_lg = Losses_gas.objects.all()
    figure = graphs_ls()

    return render(request, 'journal_rmo/forms/rmo_lg/content.html', {'rmo_lg': rmo_lg, 'figure_lg':figure})
 
 
def save_rmo_lg_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p1 = Losses_gas.objects.all()
            data['html_product_list'] = render_to_string('journal_rmo/forms/rmo_lg/partial_list.html', {
                'rmo_lg': data_p1
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def rmo_lg_create(request):
    if request.method == 'POST':
        form = Losses_gasForm(request.POST)
    else:
        form = Losses_gasForm()
    return save_rmo_lg_form(request, form, 'journal_rmo/forms/rmo_lg/partial_create.html')
 
 
def rmo_lg_update(request, pk):
    rmo_lg = get_object_or_404(Losses_gas, pk=pk)
    if request.method == 'POST':
        form = Losses_gasForm(request.POST, instance=rmo_lg)
    else:
        form = Losses_gasForm(instance=rmo_lg)
    return save_rmo_lg_form(request, form, 'journal_rmo/forms/rmo_lg/partial_update.html')
 
 
def rmo_lg_delete(request, pk):
    rmo_lg = get_object_or_404(Losses_gas, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        rmo_lg.delete()
        data['form_is_valid'] = True
        rmo_lgs = Losses_gas.objects.all()
        data['html_product_list'] = render_to_string('journal_rmo/forms/rmo_lg/partial_list.html', {
            'rmo_lg': rmo_lgs
        })
    else:
        context = {'rmo_lg': rmo_lg}
        data['html_form'] = render_to_string('journal_rmo/forms/rmo_lg/partial_delete.html', context, request=request)
    return JsonResponse(data)
