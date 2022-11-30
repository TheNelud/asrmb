from django.shortcuts import render

import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np


def graphs_P_pcv():

    N =30
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
   
    figure = go.Figure(px.line(x=random_x,
                                 y=random_y0
                                 )).to_html(config= {'displaylogo': False})
    
    return figure


# Create your views here.
def mar(request):
   
    return render(request, 'mar.html')


def mag(request):
       
    return render(request, 'mag.html')

def sar(request):
       
    return render(request, 'sar.html')

def sr_kgmk(request):

    graphsPpcv = graphs_P_pcv()

    context = {
        'graphs_P_pcv':graphsPpcv,
    }

    return render(request, 'sr_kgmk.html', context)





