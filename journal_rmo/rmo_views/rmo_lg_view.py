from django.shortcuts import render, redirect, get_object_or_404
from journal_rmo.models import *
from journal_rmo.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def rmo_lg_list(request):
    rmo_lg = Losses_gas.objects.all()

    return render(request, 'journal_rmo/forms/rmo_lg/content.html', {'rmo_lg': rmo_lg})
 
 
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


def GraphsViewBar_p1(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_rmo_lg = Losses_gas.objects.all()
    x = [item.name for item in data_rmo_lg]
    h = [item.chromatograph_mass for item in data_rmo_lg]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_rmo_lg.get(pk=1))
    data_names = list(data.values())[0:5] + [sum(list(data.values())[5:])]
    names = list(data.keys())[0:5] + ['Другие']
    plt.title('Состав компонетов')
    # plt.xlim(0, 10)
    # plt.ylim(0, 8)
    # plt.xlabel('Компоненты')
    # plt.ylabel('%')
    # plt.bar(x, h, width=1.0, bottom=0, color='Green', alpha=0.65, label='Legend')
    plt.pie(data_names,labels=names,autopct='%.1f%%',pctdistance=1.6)
    # plt.legend()
    # plt.grid(True)
 
    canvas = FigureCanvasAgg(f)
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(f)
    return HttpResponse(buffer.getvalue(), content_type='image/png')