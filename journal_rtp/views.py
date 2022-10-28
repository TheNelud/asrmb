from django.shortcuts import render, redirect
from .models import *
from .forms import *


def rtp(request):
    # Расчет технологических потерь при Добыче*
    data_rtp1 = TeclossesOne.objects.all()
    data_rtp2 = TeclossesTwo.objects.all()
    data_rtp3 = TeclossesTree.objects.all()

    # 'Расчет потерь при Переработке**
    data_rppp1 = RecyclingcalcOne.objects.all()
    data_rppp2 = RecyclingcalcTwo.objects.all()
    data_rppp3 = RecyclingcalcThree.objects.all()
    data_rppp4 = RecyclingcalcFour.objects.all()
    data_rppp5_1 = RecyclingcalcFive1.objects.all()
    data_rppp5_2 = RecyclingcalcFive2.objects.all()
    data_rppp6 = RecyclingcalcSix.objects.all()

    data_nrtp1 = CondensateprodOne.objects.all()
    data_nrtp2 = CondensateprodTwo.objects.all()
    data_nrtp3_1 = CondensateprodThree1.objects.all()
    data_nrtp3_2 = CondensateprodThree2.objects.all()

    context = {
        'rtp1': data_rtp1,
        'rtp2': data_rtp2,
        'rtp3': data_rtp3,

        'rppp1': data_rppp1,
        'rppp2': data_rppp2,
        'rppp3': data_rppp3,
        'rppp4': data_rppp4,
        'rppp5_1': data_rppp5_1,
        'rppp5_2': data_rppp5_2,
        'rppp6': data_rppp6,

        'nrtp1': data_nrtp1,
        'nrtp2': data_nrtp2,
        'nrtp3_1': data_nrtp3_1,
        'nrtp3_2': data_nrtp3_2,
    }

    return render(request, 'journal_rtp/rtp.html', context)

def create_rtp_1(request):
    form = TeclossesOneForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = TeclossesOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/rtp_1/table_form.html', context)


def update_rtp_1(request, pk):
    rtp_1 = TeclossesOne.objects.get(id=pk)
    form = TeclossesOneForm(instance=rtp_1)
    if request.method == 'POST':
        form = TeclossesOneForm(request.POST, instance=rtp_1)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/rtp_1/table_form.html', context)


def delete_rtp_1(request, pk):
    rtp_1 = TeclossesOne.objects.get(id=pk)
    if request.method == 'POST':
        rtp_1.delete()
        return redirect('/')
    context = {'item': rtp_1}
    return render(request, 'journal_rtp/forms/rtp_1/delete.html', context)


def create_rtp_2(request):
    form = TeclossesTwoForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = TeclossesTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/rtp_2/table_form.html', context)


def update_rtp_2(request, pk):
    rtp_2 = TeclossesTwo.objects.get(id=pk)
    form = TeclossesTwoForm(instance=rtp_2)
    if request.method == 'POST':
        form = TeclossesTwoForm(request.POST, instance=rtp_2)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/rtp_2/table_form.html', context)


def delete_rtp_2(request, pk):
    rtp_2 = TeclossesTwo.objects.get(id=pk)
    if request.method == 'POST':
        rtp_2.delete()
        return redirect('/')
    context = {'item': rtp_2}
    return render(request, 'journal_rtp/forms/rtp_2/delete.html', context)
