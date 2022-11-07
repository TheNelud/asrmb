from django.shortcuts import render, redirect, get_object_or_404
from journal_oks.models import *
from journal_oks.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io

def oks_p5_list(request):
    oks_p5 = P5DeterminationOfTheComponentComposition.objects.all()
    return render(request, 'journal_oks/forms/oks_p5/content.html', {'oks_p5': oks_p5})
 
 
def save_oks_p5_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p5 = P5DeterminationOfTheComponentComposition.objects.all()
            data['html_product_list'] = render_to_string('journal_oks/forms/oks_p5/partial_list.html', {
                'oks_p5': data_p5
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def oks_p5_create(request):
    if request.method == 'POST':
        form = P5DeterminationOfTheComponentCompositionForm(request.POST)
    else:
        form = P5DeterminationOfTheComponentCompositionForm()
    return save_oks_p5_form(request, form, 'journal_oks/forms/oks_p5/partial_create.html')
 
 
def oks_p5_update(request, pk):
    oks_p5 = get_object_or_404(P5DeterminationOfTheComponentComposition, pk=pk)
    if request.method == 'POST':
        form = P5DeterminationOfTheComponentCompositionForm(request.POST, instance=oks_p5)
    else:
        form = P5DeterminationOfTheComponentCompositionForm(instance=oks_p5)
    return save_oks_p5_form(request, form, 'journal_oks/forms/oks_p5/partial_update.html')
 
 
def oks_p5_delete(request, pk):
    oks_p5 = get_object_or_404(P5DeterminationOfTheComponentComposition, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        oks_p5.delete()
        data['form_is_valid'] = True
        oks_p5s = P5DeterminationOfTheComponentComposition.objects.all()
        data['html_product_list'] = render_to_string('journal_oks/forms/oks_p5/partial_list.html', {
            'oks_p5': oks_p5s
        })
    else:
        context = {'oks_p5': oks_p5}
        data['html_form'] = render_to_string('journal_oks/forms/oks_p5/partial_delete.html', context, request=request)
    return JsonResponse(data)


def GraphsViewBar(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_oks_p5 = P5DeterminationOfTheComponentComposition.objects.all()
    x = [item.name for item in data_oks_p5]
    h = [item.chromatograph_mass for item in data_oks_p5]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_oks_p5.get(pk=1))
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