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

    data_nrppp1 = CondrecyclingOne.objects.all()
    data_nrppp2 = CondrecyclingTwo.objects.all()
    data_nrppp3 = CondrecyclingThree.objects.all()
    data_nrppp4 = CondrecyclingFour.objects.all()
    data_nrppp5 = CondrecyclingFive.objects.all()
    data_nrppp6 = CondrecyclingSix.objects.all()
    data_nrppp7 = CondrecyclingSeven.objects.all()
    data_nrppp8 = CondrecyclingEight.objects.all()
    data_nrppp9 = CondrecyclingNine.objects.all()
    data_nrppp10 = CondrecyclingTen.objects.all()

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

        'nrppp1': data_nrppp1,
        'nrppp2': data_nrppp2,
        'nrppp3': data_nrppp3,
        'nrppp4': data_nrppp4,
        'nrppp5': data_nrppp5,
        'nrppp6': data_nrppp6,
        'nrppp7': data_nrppp7,
        'nrppp8': data_nrppp8,
        'nrppp9': data_nrppp9,
        'nrppp10': data_nrppp10,

    }

    return render(request, 'journal_rtp/rtp.html', context)



