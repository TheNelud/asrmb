from django.shortcuts import render, redirect, get_object_or_404
from journal_rtp.models import *
from journal_rtp.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def rppp_1_list(request):
    rppp_1 = RecyclingcalcOne.objects.all()

    return render(request, 'journal_rtp/forms/rppp_1/content.html', {'rppp_1': rppp_1})
 
 
def save_rppp_1_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p1 = RecyclingcalcOne.objects.all()
            data['html_product_list'] = render_to_string('journal_rtp/forms/rppp_1/partial_list.html', {
                'rppp_1': data_p1
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def rppp_1_create(request):
    if request.method == 'POST':
        form = RecyclingcalcOneForm(request.POST)
    else:
        form = RecyclingcalcOneForm()
    return save_rppp_1_form(request, form, 'journal_rtp/forms/rppp_1/partial_create.html')
 
 
def rppp_1_update(request, pk):
    rppp_1 = get_object_or_404(RecyclingcalcOne, pk=pk)
    if request.method == 'POST':
        form = RecyclingcalcOneForm(request.POST, instance=rppp_1)
    else:
        form = RecyclingcalcOneForm(instance=rppp_1)
    return save_rppp_1_form(request, form, 'journal_rtp/forms/rppp_1/partial_update.html')
 
 
def rppp_1_delete(request, pk):
    rppp_1 = get_object_or_404(RecyclingcalcOne, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        rppp_1.delete()
        data['form_is_valid'] = True
        rppp_1s = RecyclingcalcOne.objects.all()
        data['html_product_list'] = render_to_string('journal_rtp/forms/rppp_1/partial_list.html', {
            'rppp_1': rppp_1s
        })
    else:
        context = {'rppp_1': rppp_1}
        data['html_form'] = render_to_string('journal_rtp/forms/rppp_1/partial_delete.html', context, request=request)
    return JsonResponse(data)


def GraphsViewBar_p1(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_rppp_1 = RecyclingcalcOne.objects.all()
    x = [item.name for item in data_rppp_1]
    h = [item.chromatograph_mass for item in data_rppp_1]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_rppp_1.get(pk=1))
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