from django.shortcuts import render, redirect, get_object_or_404
from journal_koff_s.models import *
from journal_koff_s.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def p2calc_list(request):
    p2calc = P2Calc.objects.all()

    return render(request, 'journal_koff_s/forms/p2calc/content.html', {'p2calc': p2calc})
 
 
def save_p2calc_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p1 = P2Calc.objects.all()
            data['html_product_list'] = render_to_string('journal_koff_s/forms/p2calc/partial_list.html', {
                'p2calc': data_p1
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def p2calc_create(request):
    if request.method == 'POST':
        form = P2CalcForm(request.POST)
    else:
        form = P2CalcForm()
    return save_p2calc_form(request, form, 'journal_koff_s/forms/p2calc/partial_create.html')
 
 
def p2calc_update(request, pk):
    p2calc = get_object_or_404(P2Calc, pk=pk)
    if request.method == 'POST':
        form = P2CalcForm(request.POST, instance=p2calc)
    else:
        form = P2CalcForm(instance=p2calc)
    return save_p2calc_form(request, form, 'journal_koff_s/forms/p2calc/partial_update.html')
 
 
def p2calc_delete(request, pk):
    p2calc = get_object_or_404(P2Calc, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        p2calc.delete()
        data['form_is_valid'] = True
        p2calcs = P2Calc.objects.all()
        data['html_product_list'] = render_to_string('journal_koff_s/forms/p2calc/partial_list.html', {
            'p2calc': p2calcs
        })
    else:
        context = {'p2calc': p2calc}
        data['html_form'] = render_to_string('journal_koff_s/forms/p2calc/partial_delete.html', context, request=request)
    return JsonResponse(data)


def GraphsViewBar_p1(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_p2calc = P2Calc.objects.all()
    x = [item.name for item in data_p2calc]
    h = [item.chromatograph_mass for item in data_p2calc]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_p2calc.get(pk=1))
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