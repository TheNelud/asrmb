from django.shortcuts import render, redirect, get_object_or_404
from journal_rtp.models import *
from journal_rtp.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def nrtp_2_list(request):
    nrtp_2 = CondensateprodTwo.objects.all()

    return render(request, 'journal_rtp/forms/nrtp_2/content.html', {'nrtp_2': nrtp_2})
 
 
def save_nrtp_2_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data_p1 = CondensateprodTwo.objects.all()
            data['html_product_list'] = render_to_string('journal_rtp/forms/nrtp_2/partial_list.html', {
                'nrtp_2': data_p1
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def nrtp_2_create(request):
    if request.method == 'POST':
        form = CondensateprodTwoForm(request.POST)
    else:
        form = CondensateprodTwoForm()
    return save_nrtp_2_form(request, form, 'journal_rtp/forms/nrtp_2/partial_create.html')
 
 
def nrtp_2_update(request, pk):
    nrtp_2 = get_object_or_404(CondensateprodTwo, pk=pk)
    if request.method == 'POST':
        form = CondensateprodTwoForm(request.POST, instance=nrtp_2)
    else:
        form = CondensateprodTwoForm(instance=nrtp_2)
    return save_nrtp_2_form(request, form, 'journal_rtp/forms/nrtp_2/partial_update.html')
 
 
def nrtp_2_delete(request, pk):
    nrtp_2 = get_object_or_404(CondensateprodTwo, pk=pk)
    
    data = dict()
    if request.method == 'POST':
        nrtp_2.delete()
        data['form_is_valid'] = True
        nrtp_2s = CondensateprodTwo.objects.all()
        data['html_product_list'] = render_to_string('journal_rtp/forms/nrtp_2/partial_list.html', {
            'nrtp_2': nrtp_2s
        })
    else:
        context = {'nrtp_2': nrtp_2}
        data['html_form'] = render_to_string('journal_rtp/forms/nrtp_2/partial_delete.html', context, request=request)
    return JsonResponse(data)


def GraphsViewBar_p1(request):
    f = plt.figure()
    # x = np.arange(10)
    # h = [0, 1, 2, 3, 5, 6, 4, 2, 1, 0]
    data_nrtp_2 = CondensateprodTwo.objects.all()
    x = [item.name for item in data_nrtp_2]
    h = [item.chromatograph_mass for item in data_nrtp_2]
    data= dict(zip(x,h))
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    # print(data_nrtp_2.get(pk=1))
    data_names = list(data.values())[0:5] + [sum(list(data.values())[5:])]
    names = list(data.keys())[0:5] + ['????????????']
    plt.title('???????????? ????????????????????')
    # plt.xlim(0, 10)
    # plt.ylim(0, 8)
    # plt.xlabel('????????????????????')
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