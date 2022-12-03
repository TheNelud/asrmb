from django.shortcuts import render

import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np


from plotly.offline import plot



def graphs_P_pcv():

    N =30
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
   
    layout = go.Layout(
        # title_text='States_Name',
        yaxis2=dict(overlaying='y'),
        width=800,
        height=300,
        margin=dict(l=0,r=0,b=0,t=0)
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
        # title_text='States_Name',
        yaxis2=dict(overlaying='y'),
        width=800,
        height=300,
        margin=dict(l=0,r=0,b=0,t=0)
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
    
    data = {'50Р-1№1':np.linspace(1, 100, 1),
            '50Р-1№2':np.linspace(1, 100, 1)}
    courses = list(data.keys())
    print(courses)
    values = list(data.values())
    print(values)

    figure = go.Figure(px.bar(data,
                                width=500,
                                height=240,
                                )).to_html(config= {'displaylogo': False})

    
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
        margin=dict(l=0,r=0,b=0,t=30)
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
        margin=dict(l=0,r=0,b=0,t=30)
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
        margin=dict(l=0,r=0,b=0,t=30)
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
        margin=dict(l=0,r=0,b=0,t=30)
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
        margin=dict(l=0,r=0,b=0,t=30)
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
        margin=dict(l=0,r=0,b=0,t=30)
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
        margin=dict(l=0,r=0,b=0,t=30)
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
   
    return render(request, 'mar.html')


def mag(request):
       
    return render(request, 'mag.html')

def sar(request):
       
    return render(request, 'sar.html')

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





