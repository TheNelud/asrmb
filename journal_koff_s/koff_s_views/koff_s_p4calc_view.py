from django.shortcuts import render, redirect, get_object_or_404
from journal_koff_s.models import *
from journal_koff_s.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def p4calc_list(request):
    p4calc = P4Calc.objects.all()

    return render(request, 'journal_koff_s/forms/p4calc/content.html', {'p4calc': p4calc})
 
 
def save_p4calc_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p1 = P4Calc.objects.all()
            data['html_product_list'] = render_to_string('journal_koff_s/forms/p4calc/partial_list.html', {
                'p4calc': data_p1
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def p4calc_create(request):
    if request.method == 'POST':
        form = P4CalcForm(request.POST)
    else:
        form = P4CalcForm()
    return save_p4calc_form(request, form, 'journal_koff_s/forms/p4calc/partial_create.html')
 
 
def p4calc_update(request, pk):
    p4calc = get_object_or_404(P4Calc, pk=pk)
    if request.method == 'POST':
        form = P4CalcForm(request.POST, instance=p4calc)
    else:
        form = P4CalcForm(instance=p4calc)
    return save_p4calc_form(request, form, 'journal_koff_s/forms/p4calc/partial_update.html')
 
 
def p4calc_delete(request, pk):
    p4calc = get_object_or_404(P4Calc, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        p4calc.delete()
        data['form_is_valid'] = True
        p4calcs = P4Calc.objects.all()
        data['html_product_list'] = render_to_string('journal_koff_s/forms/p4calc/partial_list.html', {
            'p4calc': p4calcs
        })
    else:
        context = {'p4calc': p4calc}
        data['html_form'] = render_to_string('journal_koff_s/forms/p4calc/partial_delete.html', context, request=request)
    return JsonResponse(data)


def GraphsViewBar_p1(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_p4calc = P4Calc.objects.all()
    x = [item.name for item in data_p4calc]
    h = [item.chromatograph_mass for item in data_p4calc]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_p4calc.get(pk=1))
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