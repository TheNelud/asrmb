from django.shortcuts import render, redirect
from . models import *
from . forms import *
from  .filters import *

# Create your views here.


def pgk(request):
    data_calc_losses = Calc_losses.objects.all()
    data_losses_gas_apparatus = Losses_gas_apparatus.objects.all()


    filterDate = Losses_gas_apparatusFilter()


    context = {
        'data_calc_losses': data_calc_losses,
        'data_losses_gas_apparatus': data_losses_gas_apparatus,

        'filterDate': filterDate,
    }


    return render(request, 'journal_pgk/pgk.html', context)






