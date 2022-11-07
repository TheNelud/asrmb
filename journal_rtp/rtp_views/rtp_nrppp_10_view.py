from django.shortcuts import render, redirect, get_object_or_404
from journal_rtp.models import *
from journal_rtp.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def nrppp_10_list(request):
    nrppp_10 = CondrecyclingTen.objects.all()

    return render(request, 'journal_rtp/forms/nrppp_10/content.html', {'nrppp_10': nrppp_10})
 
 
def save_nrppp_10_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p1 = CondrecyclingTen.objects.all()
            data['html_product_list'] = render_to_string('journal_rtp/forms/nrppp_10/partial_list.html', {
                'nrppp_10': data_p1
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def nrppp_10_create(request):
    if request.method == 'POST':
        form = CondrecyclingTenForm(request.POST)
    else:
        form = CondrecyclingTenForm()
    return save_nrppp_10_form(request, form, 'journal_rtp/forms/nrppp_10/partial_create.html')
 
 
def nrppp_10_update(request, pk):
    nrppp_10 = get_object_or_404(CondrecyclingTen, pk=pk)
    if request.method == 'POST':
        form = CondrecyclingTenForm(request.POST, instance=nrppp_10)
    else:
        form = CondrecyclingTenForm(instance=nrppp_10)
    return save_nrppp_10_form(request, form, 'journal_rtp/forms/nrppp_10/partial_update.html')
 
 
def nrppp_10_delete(request, pk):
    nrppp_10 = get_object_or_404(CondrecyclingTen, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        nrppp_10.delete()
        data['form_is_valid'] = True
        nrppp_10s = CondrecyclingTen.objects.all()
        data['html_product_list'] = render_to_string('journal_rtp/forms/nrppp_10/partial_list.html', {
            'nrppp_10': nrppp_10s
        })
    else:
        context = {'nrppp_10': nrppp_10}
        data['html_form'] = render_to_string('journal_rtp/forms/nrppp_10/partial_delete.html', context, request=request)
    return JsonResponse(data)


def GraphsViewBar_p1(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_nrppp_10 = CondrecyclingTen.objects.all()
    x = [item.name for item in data_nrppp_10]
    h = [item.chromatograph_mass for item in data_nrppp_10]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_nrppp_10.get(pk=1))
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