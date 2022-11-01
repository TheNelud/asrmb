from django.shortcuts import render, redirect
from . models import *
from . forms import *

# Create your views here.


def pgk(request):
    data_calc_losses = Calc_losses.objects.all()
    data_losses_gas_apparatus = Losses_gas_apparatus.objects.all()


    context = {
        'data_calc_losses': data_calc_losses,
        'data_losses_gas_apparatus': data_losses_gas_apparatus,
    }


    return render(request, 'journal_pgk/pgk.html', context)


def create_pgk(request):
    form = Losses_gas_apparatusForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = Losses_gas_apparatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_pgk/forms/pgk/table_form.html', context)


def update_pgk(request, pk):
    rmo = Losses_gas_apparatus.objects.get(id=pk)
    form = Losses_gas_apparatusForm(instance=rmo)
    if request.method == 'POST':
        form = Losses_gas_apparatusForm(request.POST, instance=rmo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_pgk/forms/pgk/table_form.html', context)


def delete_pgk(request, pk):
    rmo = Losses_gas_apparatus.objects.get(id=pk)
    if request.method == 'POST':
        rmo.delete()
        return redirect('/')
    context = {'item': rmo}
    return render(request, 'journal_pgk/forms/pgk/delete.html', context)
