from django.shortcuts import render, redirect, get_object_or_404
from journal_oks.models import *
from journal_oks.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io

def oks_p7_list(request):
    oks_p7 = P7CompositionOfGas10c.objects.all()
    return render(request, 'journal_oks/forms/oks_p7/content.html', {'oks_p7': oks_p7})
 
 
def save_oks_p7_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p7 = P7CompositionOfGas10c.objects.all()
            data['html_product_list'] = render_to_string('journal_oks/forms/oks_p7/partial_list.html', {
                'oks_p7': data_p7
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def oks_p7_create(request):
    if request.method == 'POST':
        form = P7CompositionOfGas10cForm(request.POST)
    else:
        form = P7CompositionOfGas10cForm()
    return save_oks_p7_form(request, form, 'journal_oks/forms/oks_p7/partial_create.html')
 
 
def oks_p7_update(request, pk):
    oks_p7 = get_object_or_404(P7CompositionOfGas10c, pk=pk)
    if request.method == 'POST':
        form = P7CompositionOfGas10cForm(request.POST, instance=oks_p7)
    else:
        form = P7CompositionOfGas10cForm(instance=oks_p7)
    return save_oks_p7_form(request, form, 'journal_oks/forms/oks_p7/partial_update.html')
 
 
def oks_p7_delete(request, pk):
    oks_p7 = get_object_or_404(P7CompositionOfGas10c, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        oks_p7.delete()
        data['form_is_valid'] = True
        oks_p7s = P7CompositionOfGas10c.objects.all()
        data['html_product_list'] = render_to_string('journal_oks/forms/oks_p7/partial_list.html', {
            'oks_p7': oks_p7s
        })
    else:
        context = {'oks_p7': oks_p7}
        data['html_form'] = render_to_string('journal_oks/forms/oks_p7/partial_delete.html', context, request=request)
    return JsonResponse(data)


def GraphsViewBar(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_oks_p7 = P7CompositionOfGas10c.objects.all()
    x = [item.name for item in data_oks_p7]
    h = [item.chromatograph_mass for item in data_oks_p7]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_oks_p7.get(pk=1))
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