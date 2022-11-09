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






def rmo_ps_list(request):
    rmo_ps = Perehod_stabilizacii.objects.all()
    figure = graphs_ps_2()
    context = {'rmo_ps': rmo_ps,
                'figure': figure 
                }

    return render(request, 'journal_rmo/forms/rmo_ps/content.html', context=context  )


def graphs_ps_2():
    data_rmo_ps = Perehod_stabilizacii.objects.all()
    x_data = [item.update_time for item in data_rmo_ps]
    y_data = [item.perehod_t for item in data_rmo_ps]

    print(x_data)
    print(y_data)
   
    layout =go.Layout(
        title=f'Визуализация данных журнала ...',
        width=400,
        height=400,
        # legend_bgcolor= '#000000'
    )

    figure = go.Figure(px.line(x=x_data, y=y_data ),layout=layout).to_html()
   
    return figure
 
 
def save_rmo_ps_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p1 = Perehod_stabilizacii.objects.all()
            data['html_product_list'] = render_to_string('journal_rmo/forms/rmo_ps/partial_list.html', {
                'rmo_ps': data_p1
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def rmo_ps_create(request):
    if request.method == 'POST':
        form = Perehod_stabilizaciiForm(request.POST)
    else:
        form = Perehod_stabilizaciiForm()
    return save_rmo_ps_form(request, form, 'journal_rmo/forms/rmo_ps/partial_create.html')
 
 
def rmo_ps_update(request, pk):
    rmo_ps = get_object_or_404(Perehod_stabilizacii, pk=pk)
    if request.method == 'POST':
        form = Perehod_stabilizaciiForm(request.POST, instance=rmo_ps)
    else:
        form = Perehod_stabilizaciiForm(instance=rmo_ps)
    return save_rmo_ps_form(request, form, 'journal_rmo/forms/rmo_ps/partial_update.html')
 
 
def rmo_ps_delete(request, pk):
    rmo_ps = get_object_or_404(Perehod_stabilizacii, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        rmo_ps.delete()
        data['form_is_valid'] = True
        rmo_pss = Perehod_stabilizacii.objects.all()
        data['html_product_list'] = render_to_string('journal_rmo/forms/rmo_ps/partial_list.html', {
            'rmo_ps': rmo_pss
        })
    else:
        context = {'rmo_ps': rmo_ps}
        data['html_form'] = render_to_string('journal_rmo/forms/rmo_ps/partial_delete.html', context, request=request)
    return JsonResponse(data)





