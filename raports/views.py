from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse

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
def mar(request):
    items_month = Mer_per_month.objects.all().order_by('date_update').last()
    return render(request, 'mar.html', context = {"items_month":items_month})


def mag(request):
    items_tech = Sen_equip.objects.all().order_by('update_time').last()
    items_balance = Balance.objects.order_by('-update_time')[:1]

    # items_balance = Balance.objects.all().order_by('update_time').last()
    return render(request, 'mag.html', context = {"items_tech":items_tech,
                                                    "items_balance":items_balance})


def mag_create(request):
 
    if request.method == 'POST':
        form = BalanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mag.html')
        
    form = BalanceForm()
    data ={
        'form' : form,
    }

    return render(request,'partial_create.html', data)

def sar(request):
    
    # items_day = Ser_per_day.objects.values().order_by('-date_update')
    # print(items_day)
    
    items_day = Ser_per_day.objects.order_by('-date_update')[:1]

    # i = 0
    # for i in range(len(items_day)):
    #     # print(items_day[i])
    #     print(items_day[i]["date_update"])
    #     for key, value in items_day[i].items():
    #         if items_day[i]["date_update"] < datetime.datetime.date(2022, 12, 9):
    #             print(key, value)
        # for item_list[i] in items_day:
        #     print(item_list)

    
    items_month =Ser_per_month.objects.all().order_by('-date_update')[:1]
    print(items_month.values())
    return render(request, 'sar.html', context={'items_day' : items_day,
                                                'items_month' : items_month,
                                               
                                                })

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





