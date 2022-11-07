from django.shortcuts import render, redirect, get_object_or_404
from journal_rtp.models import *
from journal_rtp.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def nrppp_6_list(request):
    nrppp_6 = CondrecyclingSix.objects.all()

    return render(request, 'journal_rtp/forms/nrppp_6/content.html', {'nrppp_6': nrppp_6})
 
 
def save_nrppp_6_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p1 = CondrecyclingSix.objects.all()
            data['html_product_list'] = render_to_string('journal_rtp/forms/nrppp_6/partial_list.html', {
                'nrppp_6': data_p1
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def nrppp_6_create(request):
    if request.method == 'POST':
        form = CondrecyclingSixForm(request.POST)
    else:
        form = CondrecyclingSixForm()
    return save_nrppp_6_form(request, form, 'journal_rtp/forms/nrppp_6/partial_create.html')
 
 
def nrppp_6_update(request, pk):
    nrppp_6 = get_object_or_404(CondrecyclingSix, pk=pk)
    if request.method == 'POST':
        form = CondrecyclingSixForm(request.POST, instance=nrppp_6)
    else:
        form = CondrecyclingSixForm(instance=nrppp_6)
    return save_nrppp_6_form(request, form, 'journal_rtp/forms/nrppp_6/partial_update.html')
 
 
def nrppp_6_delete(request, pk):
    nrppp_6 = get_object_or_404(CondrecyclingSix, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        nrppp_6.delete()
        data['form_is_valid'] = True
        nrppp_6s = CondrecyclingSix.objects.all()
        data['html_product_list'] = render_to_string('journal_rtp/forms/nrppp_6/partial_list.html', {
            'nrppp_6': nrppp_6s
        })
    else:
        context = {'nrppp_6': nrppp_6}
        data['html_form'] = render_to_string('journal_rtp/forms/nrppp_6/partial_delete.html', context, request=request)
    return JsonResponse(data)


def GraphsViewBar_p1(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_nrppp_6 = CondrecyclingSix.objects.all()
    x = [item.name for item in data_nrppp_6]
    h = [item.chromatograph_mass for item in data_nrppp_6]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_nrppp_6.get(pk=1))
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