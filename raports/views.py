from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from .calculate_balance import calculate_balance
import datetime
from datetime import timedelta


from django.views.generic.edit import UpdateView


import plotly.graph_objs as go

import numpy as np
import random
from plotly.offline import plot
import datetime

from .models import *
from .forms import *




def graphs_P_pcv():

    N =30
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
   
    layout = go.Layout(
        # title_text='States_Name',
        yaxis2=dict(overlaying='y'),
        width=900,
        height=300,
        margin=dict(l=0,r=0,b=0,t=0),
        legend=dict(orientation="h")
    )

    figure = go.Figure([go.Scatter(x = random_x,y = random_y0,name='P4 после PCV'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='P5 после PCV'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='P3 после PCV'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='P4-бис после PCV'),
        go.Scatter(x = random_x,y = random_y0 + 1, name='P3 после PCV')],
        layout=layout).to_html({'displaylogo': False})
    # figure.to_html(config= {'displaylogo': False})
    return figure


def graphs_T_c():
    N =30
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
   
    layout = go.Layout(
        
        yaxis2=dict(overlaying='y'),
        width=600,
        height=270,
        margin=dict(l=0,r=0,b=0,t=30),
        legend=dict(orientation="h")
    )

    figure = go.Figure([go.Scatter(x = random_x,y = random_y0,name='Температура точки росы'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Т норма УВ'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Температура УВ'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Содержание (СО2), %'),
        go.Scatter(x = random_x,y = random_y0 + 1, name='Т норма Н2О'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='СО2 норма')],
        layout=layout).to_html({'displaylogo': False})
    
    return figure

def graphs_V(): 
    
    data = {'50Р-1№1':random.randint(1,100),
            '50Р-1№2':random.randint(1,100)}

    courses = list(data.keys())
    print(courses[0])
    values = list(data.values())
    print(values)


    layout = go.Layout(
        title_text='Резервуарный парк',
        yaxis2=dict(overlaying='y'),
        width=200,
        height=300,
        margin=dict(l=0,r=0,b=0,t=30),
        legend=dict(orientation="h")
    )

    figure = go.Figure(go.Bar(x = courses, y = values , text= values),
        # go.Bar(data,x = courses[1], y = values[1], name = courses[1])],
        layout=layout).to_html(config= {'displaylogo': False})

    
    return figure

#__________________________________________#
def graphs_1():
    N =30
    random_x = np.linspace(0, 30, N)
    random_y0 = np.random.randn(N) + 5


    layout = go.Layout(
        title_text='БАЛАНСОВЫЕ И ПЛАНОВЫЕ ПОКАЗАТЕЛИ ДОБЫЧИ ГАЗА (тыс. м3/сут)',
        yaxis2=dict(overlaying='y'),
        # width=800,
        height=300,
        margin=dict(l=0,r=0,b=0,t=30),
        legend=dict(orientation="h")
    )

    figure = go.Figure([go.Scatter(x = random_x,y = random_y0,name='Добыча газа план'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Добыча газа факт'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Добыча газа P5'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='обыча газа Р6'),
        go.Scatter(x = random_x,y = random_y0 + 1, name='Добыча газа Р3'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Добыча газа Р4-бис')],
        layout=layout).to_html({'displaylogo': False})

     #('БАЛАНСОВЫЕ И ПЛАНОВЫЕ ПОКАЗАТЕЛИ ДОБЫЧИ ГАЗА (тыс. м3/сут)')
                                 
    return figure

def graphs_2():
    N =30
    random_x = np.linspace(0, 30, N)
    random_y0 = np.random.randn(N) + 5

    layout = go.Layout(
        title_text='ДОБЫЧА И ПЕРЕРАБОТКА КОНДЕНСАТА ГАЗОВОГО (тыс.тонн/сут)',
        yaxis2=dict(overlaying='y'),
        # width=800,
        height=300,
        margin=dict(l=0,r=0,b=0,t=30),
        legend=dict(orientation="h")
    )

    figure = go.Figure([go.Scatter(x = random_x,y = random_y0,name='Добыча КГН, тыс. тонн'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Производство КГС, тыс. тонн'),
        go.Scatter(x = random_x,y = random_y0 - 0.5, name='Добыча КГН план, тыс. тонн'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Производство КГС план, тыс. тонн')],
        layout=layout).to_html({'displaylogo': False})
    return figure

def graphs_3():
    N =30
    random_x = np.linspace(0, 30, N)
    random_y0 = np.random.randn(N) + 5
   
    layout = go.Layout(
        title_text='ПОСТАВКА КОНДЕНСАТА ГАЗОВОГО (тыс.тонн/сут)',
        yaxis2=dict(overlaying='y'),
        # width=800,
        height=300,
        margin=dict(l=0,r=0,b=0,t=30),
        legend=dict(orientation="h")
    )

    figure = go.Figure([go.Bar(x = random_x,y = random_y0,name='Добыча КГН, тыс. тонн'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Накопленная откачка в СЭИК'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='План откачки КГС в СЭИК'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='ППлан откачки КГС за месяц, тыс. тонн')],
        layout=layout).to_html({'displaylogo': False})
    return figure

def graphs_4():
    N =30
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
   
    layout = go.Layout(
        title_text='Потребление газа в г. Владивосток (тыс.м3/сут), давление на входе ГКС "Сахалин" (МПа)',
        yaxis2=dict(overlaying='y'),
        # width=800,
        height=300,
        margin=dict(l=0,r=0,b=0,t=30),
        legend=dict(orientation="h")
    )

    figure = go.Figure([go.Bar(x = random_x,y = random_y0,name='Потребление газа на г.Владивосток'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Р (МПа), на входе в ГКС Сахалин')],
        layout=layout).to_html({'displaylogo': False})
    return figure

def graphs_5():
    N =30
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
   
    layout = go.Layout(
        title_text='ПОСТУПЛЕНИЕ ЖИДКОСТИ НА УКПГ (тонн/сут)',
        yaxis2=dict(overlaying='y'),
        # width=800,
        height=300,
        margin=dict(l=0,r=0,b=0,t=30),
        legend=dict(orientation="h")
    )

    figure = go.Figure([go.Bar(x = random_x,y = random_y0,name='Рефлюксная вода с УРМ'),
        go.Bar(x = random_x,y = random_y0 + 0.2,name='Поступление КГН'),
        go.Bar(x = random_x,y = random_y0 - 0.3 ,name='Поступление нМЭГ')],
        layout=layout).to_html({'displaylogo': False})
    return figure

def graphs_6():
    N =30
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
   
    layout = go.Layout(
        title_text='СТН И ПОТЕРИ ГАЗА (тыс. м3/сут)',
        yaxis2=dict(overlaying='y'),
        # width=800,
        height=300,
        margin=dict(l=0,r=0,b=0,t=30),
        legend=dict(orientation="h")
    )

    figure = go.Figure([go.Scatter(x = random_x,y = random_y0 + 0.5, name='Собственные тех. нужды'),
        go.Scatter(x = random_x,y = random_y0 - 0.5, name='Потери')],
        layout=layout).to_html({'displaylogo': False})
    return figure

def graphs_7():
    N =30
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
   
    layout = go.Layout(
        title_text='МАТЕРИАЛЬНЫЙ БАЛАНС ХИМ. РЕАГЕНТОВ (РАСТВОР МЭГ) (тонн/сут)',
        yaxis2=dict(overlaying='y'),
        # width=800,
        height=300,
        margin=dict(l=0,r=0,b=0,t=30),
        legend=dict(orientation="h")
    )

    figure = go.Figure([go.Bar(x = random_x,y = random_y0,name='Концентрация нМЭГ'),
        go.Bar(x = random_x,y = random_y0 + 0.2,name='Концентрация рМЭГ'),
        go.Scatter(x = random_x,y = random_y0 + 0.5, name='Расход рМЭГ'),
        go.Scatter(x = random_x,y = random_y0 - 0.5, name='Регенерация МЭГ'),
        go.Scatter(x = random_x,y = random_y0 + 0.3, name='Приход нМЭГ на УРМ')],
        layout=layout).to_html({'displaylogo': False})
    return figure
#___________________________________________#
# Create your views here.

"""Для МЭР"""
def mar(request):
    max_date_now = datetime.datetime.now().strftime("%Y-%m-%d")
    items_month = Mer_per_month.objects.all().order_by('-date_update')[:1]
    return render(request, 'mar.html', context = {
                                                    "itemss_month":items_month,
                                                    'max_date_now':max_date_now     
                                                    })

def filter_date_mar(request):
    max_date_now = datetime.datetime.now().strftime("%Y-%m-%d")
    items_month =Mer_per_month.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    if items_month.values():
        just_day = items_month.values()[0]['date_update']
        delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
    else:
        delta_day = "-"

    print(items_month.values())
    return render(request, 'mar.html', context={
                                                'itemss_month' : items_month,
                                                'max_date_now':max_date_now,
                                                'delta_day':delta_day
                                                })

def mar_edit(request):
    items_month =Mer_per_month.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    if request.method == "POST":
        form_month = Mer_per_month_form(request.POST)
        print(form_month)
        if form_month.is_valid():
            form_month.save()
            print('SAVE')
            # return render(request, 'sar.html', context={'items_ser_day':items_ser_day})
    else:
        form_month = Mer_per_month_form()

    context = { 
                'form_month':form_month,
                'itemss_month':items_month
                }
    return render(request,'mar_edit.html', context)
 

"""Для МЭГ"""
def mag(request):
    max_date_now = datetime.datetime.now().strftime("%Y-%m-%d")
    items_tech = Sen_equip.objects.all().order_by('-date_update')[:1]
    items_balance = Balance.objects.all().order_by('-date_update')[:1]

    return render(request, 'mag.html', context = {
                                                    "itemss_tech":items_tech,
                                                    "itemss_balance":items_balance,
                                                    'max_date_now':max_date_now
                                                    })

def filter_date_mag(request):
    max_date_now = datetime.datetime.now().strftime("%Y-%m-%d")
    
    items_tech = Sen_equip.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1] 
    items_balance =Balance.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    if items_tech.values():
        just_day = items_tech.values()[0]['date_update']
        delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
    else:
        delta_day = "-"
    
    return render(request, 'mag.html', context={
                                               "itemss_tech":items_tech,
                                                "itemss_balance":items_balance,
                                                'max_date_now':max_date_now,
                                                'delta_day':delta_day
                                                })

def save_mag_balance(request, form,template_name):
    max_date_now = datetime.datetime.now().strftime("%Y-%m-%d")
    data = dict()
    if request.method == "POST":
        print(form)
        if form.is_valid:
            form.save()
            calculate_balance(request)
            data['form_is_valid'] = True
            items_balance = Balance.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-date_update')[:1]
            data['html_product_list'] = render_to_string('mag.html', context={
                "itemss_balance":items_balance,
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form,
                'max_date_now': max_date_now
                }
    data["html_form"] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)



def add_calculate_mag_balance(request):
    if request.method == 'POST':
        form = BalanceForm(request.POST)
    else:
        form = BalanceForm()

        print(form)
    return save_mag_balance(request, form, 'add_calculate_balance.html')


def mag_edit(request ):
    items_tech = Sen_equip.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-date_update')[:1] 
    items_balance =Balance.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-date_update')[:1]

    if request.method == "POST":
        form_tech = Sen_equip_form(request.POST)
        form_balance = BalanceForm(request.POST)
  
        
        if form_tech.is_valid() and form_balance.is_valid():
            form_tech.save()
            calculate_balance(request, form_balance)
            # form_balance.save()
            print('SAVE')
            # return render(request, 'sar.html', context={'items_ser_day':items_ser_day})
    else:
        form_tech = Sen_equip_form()
        form_balance = BalanceForm()
        print(form_balance, form_tech)
    context = { 'form_tech': form_tech,
                'form_balance':form_balance,
                'items_tech':items_tech,
                'items_balance':items_balance
                }
    return render(request,'mag_edit.html', context)
    

"""Для СЭР"""
def sar(request):

    max_date_now = datetime.datetime.now().strftime("%Y-%m-%d")
    items_day = Ser_per_day.objects.all().order_by('-date_update')[:1]
    items_month =Ser_per_month.objects.all().order_by('-date_update')[:1] 
    return render(request, 'sar.html', context={'items_day' : items_day,
                                                'items_month' : items_month,
                                                'max_date_now':max_date_now
                                                })

def filter_date_sar(request):
    max_date_now = datetime.datetime.now().strftime("%Y-%m-%d")
    items_day = Ser_per_day.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-date_update')[:1]
    items_month =Ser_per_month.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-date_update')[:1]
    print(items_day.values())
    print(items_month.values())
    if items_day.values():
        just_day = items_day.values()[0]['date_update']
        delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
    else:
        delta_day = "-"
     
    return render(request, 'sar.html', context={'items_ser_day' : items_day,
                                                'items_ser_month' : items_month,
                                                'max_date_now':max_date_now,
                                                'delta_day': delta_day
                                                }) 



def sar_edit(request):
    items_ser_day = Ser_per_day.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    items_ser_month =Ser_per_month.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    
    if request.method == "POST":
        form_day = Ser_per_day_form(request.POST)
        form_month = Ser_per_month_form(request.POST)
        print(form_day,'________', form_month)
        if form_day.is_valid() and form_month.is_valid():
            form_day.save()
            form_month.save()
            print('SAVE')
            # return render(request, 'sar.html', context={'items_ser_day':items_ser_day})
    else:
        form_day = Ser_per_day_form()
        form_month = Ser_per_month_form()
    context = { 'form_day': form_day,
                'form_month':form_month,
                'items_ser_day':items_ser_day,
                'items_ser_month':items_ser_month
                }
    return render(request,'sar_edit.html', context)








def sr_kgmk(request):

    graphsPpcv = graphs_P_pcv()
    graphsTc = graphs_T_c()
    graphsV = graphs_V()

    _graphs_1 = graphs_1()
    _graphs_2 = graphs_2()
    _graphs_3 = graphs_3()
    _graphs_4 = graphs_4()
    _graphs_5 = graphs_5()
    _graphs_6 = graphs_6()
    _graphs_7 = graphs_7()
    
    
    context = {
        'graphs_P_pcv':graphsPpcv,
        'graphs_T_c':graphsTc,
        'graphs_V':graphsV,

        'graphs_1':_graphs_1,
        'graphs_2':_graphs_2,
        'graphs_3':_graphs_3,
        'graphs_4':_graphs_4,
        'graphs_5':_graphs_5,
        'graphs_6':_graphs_6,
        'graphs_7':_graphs_7,
    }

    return render(request, 'sr_kgmk.html', context)





