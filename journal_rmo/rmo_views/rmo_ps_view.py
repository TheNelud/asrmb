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
import pandas as pd





def rmo_ps_list(request):
    rmo_ps = Perehod_stabilizacii.objects.all()
    figure = graphs_ps()
    context = {'rmo_ps': rmo_ps,
                'figure_ps_perehod_per': figure[0],
                'figure_ps_perehod_t': figure[1],
                }

    return render(request, 'journal_rmo/forms/rmo_ps/content.html', context=context  )


def graphs_ps():
    data = Perehod_stabilizacii.objects.all()
    
    df = pd.DataFrame({
                        'name':[item.name for item in data],
                        'perehod_per': [item.perehod_per for item in data],
                        'perehod_t' : [item.perehod_t for item in data],
                        'update_time' : [item.update_time for item in data]
                        })
    print(df)
    figure_perehod_per = go.Figure(px.pie(df ,values='perehod_per', 
                                            names='name', 
                                            title="Перешло из газа стабилизации в КГН, % массовые"
                                            ),
                                            layout=go.Layout(width=400)).to_html(config= {'displaylogo': False})
    figure_perehod_t = go.Figure(px.pie(df ,values='perehod_t',
                                            names='name', 
                                            title="Перешло из газа стабилизации в КГН"
                                            ),
                                            layout=go.Layout(width=400)).to_html(config= {'displaylogo': False})
    
    return [figure_perehod_per, figure_perehod_t]
 
 
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





