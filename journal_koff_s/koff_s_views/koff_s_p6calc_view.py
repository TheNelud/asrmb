from django.shortcuts import render, redirect, get_object_or_404
from journal_koff_s.models import *
from journal_koff_s.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def p6calc_list(request):
    p6calc = P6Calc.objects.all()

    return render(request, 'journal_koff_s/forms/p6calc/content.html', {'p6calc': p6calc})
 
 
def save_p6calc_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p1 = P6Calc.objects.all()
            data['html_product_list'] = render_to_string('journal_koff_s/forms/p6calc/partial_list.html', {
                'p6calc': data_p1
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def p6calc_create(request):
    if request.method == 'POST':
        form = P6CalcForm(request.POST)
    else:
        form = P6CalcForm()
    return save_p6calc_form(request, form, 'journal_koff_s/forms/p6calc/partial_create.html')
 
 
def p6calc_update(request, pk):
    p6calc = get_object_or_404(P6Calc, pk=pk)
    if request.method == 'POST':
        form = P6CalcForm(request.POST, instance=p6calc)
    else:
        form = P6CalcForm(instance=p6calc)
    return save_p6calc_form(request, form, 'journal_koff_s/forms/p6calc/partial_update.html')
 
 
def p6calc_delete(request, pk):
    p6calc = get_object_or_404(P6Calc, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        p6calc.delete()
        data['form_is_valid'] = True
        p6calcs = P6Calc.objects.all()
        data['html_product_list'] = render_to_string('journal_koff_s/forms/p6calc/partial_list.html', {
            'p6calc': p6calcs
        })
    else:
        context = {'p6calc': p6calc}
        data['html_form'] = render_to_string('journal_koff_s/forms/p6calc/partial_delete.html', context, request=request)
    return JsonResponse(data)


def GraphsViewBar_p1(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_p6calc = P6Calc.objects.all()
    x = [item.name for item in data_p6calc]
    h = [item.chromatograph_mass for item in data_p6calc]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_p6calc.get(pk=1))
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