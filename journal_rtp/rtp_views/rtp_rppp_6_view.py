from django.shortcuts import render, redirect, get_object_or_404
from journal_rtp.models import *
from journal_rtp.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def rppp_6_list(request):
    rppp_6 = RecyclingcalcSix.objects.all()

    return render(request, 'journal_rtp/forms/rppp_6/content.html', {'rppp_6': rppp_6})
 
 
def save_rppp_6_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p1 = RecyclingcalcSix.objects.all()
            data['html_product_list'] = render_to_string('journal_rtp/forms/rppp_6/partial_list.html', {
                'rppp_6': data_p1
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def rppp_6_create(request):
    if request.method == 'POST':
        form = RecyclingcalcSixForm(request.POST)
    else:
        form = RecyclingcalcSixForm()
    return save_rppp_6_form(request, form, 'journal_rtp/forms/rppp_6/partial_create.html')
 
 
def rppp_6_update(request, pk):
    rppp_6 = get_object_or_404(RecyclingcalcSix, pk=pk)
    if request.method == 'POST':
        form = RecyclingcalcSixForm(request.POST, instance=rppp_6)
    else:
        form = RecyclingcalcSixForm(instance=rppp_6)
    return save_rppp_6_form(request, form, 'journal_rtp/forms/rppp_6/partial_update.html')
 
 
def rppp_6_delete(request, pk):
    rppp_6 = get_object_or_404(RecyclingcalcSix, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        rppp_6.delete()
        data['form_is_valid'] = True
        rppp_6s = RecyclingcalcSix.objects.all()
        data['html_product_list'] = render_to_string('journal_rtp/forms/rppp_6/partial_list.html', {
            'rppp_6': rppp_6s
        })
    else:
        context = {'rppp_6': rppp_6}
        data['html_form'] = render_to_string('journal_rtp/forms/rppp_6/partial_delete.html', context, request=request)
    return JsonResponse(data)


def GraphsViewBar_p1(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_rppp_6 = RecyclingcalcSix.objects.all()
    x = [item.name for item in data_rppp_6]
    h = [item.chromatograph_mass for item in data_rppp_6]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_rppp_6.get(pk=1))
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