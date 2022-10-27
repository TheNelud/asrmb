from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, "journal/main.html")


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

    return render(request, 'journal/rtp.html', context)


def rmo(request):
    return render(request, 'journal/rmo.html')


def koff(request):
    data_coef = Coef.objects.all()
    data_losses = Losses.objects.all()
    data_mol_mass = MolMass.objects.all()
    context = {
        'coef': data_coef,
        'losses': data_losses,
        'mol_mass': data_mol_mass,
    }
    return render(request, 'journal/koff.html', context)


def koff_s(request):
    return render(request, 'journal/koff_s.html')


def pgk(request):
    return render(request, 'journal/pgk.html')
