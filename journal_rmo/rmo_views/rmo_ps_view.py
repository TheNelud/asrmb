from django.shortcuts import render, redirect, get_object_or_404
from journal_rmo.models import *
from journal_rmo.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def rmo_ps_list(request):
    rmo_ps = Perehod_stabilizacii.objects.all()

    return render(request, 'journal_rmo/forms/rmo_ps/content.html', {'rmo_ps': rmo_ps})
 
 
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


def GraphsViewBar_p1(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_rmo_ps = Perehod_stabilizacii.objects.all()
    x = [item.name for item in data_rmo_ps]
    h = [item.chromatograph_mass for item in data_rmo_ps]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_rmo_ps.get(pk=1))
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