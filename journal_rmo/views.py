from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.


def rmo(request):
    # data_rmo_p5 = P5_app.objects.all()
    # data_rmo_p6 = P6_app.objects.all()

    data_rmo_lg = Losses_gas.objects.all()
    data_rmo_md = Meters_data_20e_1.objects.all()
    data_rmo_ps = Perehod_stabilizacii.objects.all()
    data_rmo_gs = Data_gas_stabilization.objects.all()
    data_rmo_const = Const.objects.all()

    context = {
        # 'rmo_p5': data_rmo_p5,
        # 'rmo_p6': data_rmo_p6,

        'data_rmo_lg': data_rmo_lg,
        'data_rmo_md': data_rmo_md,
        'rmo_ps': data_rmo_ps,
        'rmo_gs': data_rmo_gs,
        'rmo_const': data_rmo_const,
    }

    return render(request, 'journal_rmo/rmo.html', context)



