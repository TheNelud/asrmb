from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io

# Create your views here.


def oks(request):
    # data_p1 = P1ComponentCompositionOfUnstableCondensate.objects.all()
    # data_p2 = P2ComponentCompositionOfGas.objects.all()
    data_p3 = P3DeterminationOfTheComponentOfGas.objects.all()
    data_p4 = P4GasCompositionToTheProtocol.objects.all()
    data_p5 = P5DeterminationOfTheComponentComposition.objects.all()
    data_p6 = P6CompositionOfGasOutput.objects.all()
    data_p7 = P7CompositionOfGas10c.objects.all()
    data_p8 = P8CompositionOfTheCondensate.objects.all()
    data_p9 = P9ComponentOfTheSeparationGas.objects.all()
    data_p10 = P10ProtokolKGN.objects.all()
    data_all_table_cal = AllTableCal.objects.all()
    data_den_protocol = DenProtokol.objects.all()
    data_p2_sum_table = P2SumTable.objects.all()
    data_p4_sum_table = P4SumTable.objects.all()
    data_p6_sum_table = P6SumTable.objects.all()
    data_p10_calc = P10Calc.objects.all()
    context = {
        # 'oks_p1': data_p1,
        # 'oks_p2': data_p2,
        'oks_p3': data_p3,
        'oks_p4': data_p4,
        'oks_p5': data_p5,
        'oks_p6': data_p6,
        'oks_p7': data_p7,
        'oks_p8': data_p8,
        'oks_p9': data_p9,
        'oks_p10': data_p10,
        'oks_all_table_cal': data_all_table_cal,
        'data_den_protocol': data_den_protocol,
        'data_p2_sum_table': data_p2_sum_table,
        'data_p4_sum_table': data_p4_sum_table,
        'data_p6_sum_table': data_p6_sum_table,
        'data_p10_calc': data_p10_calc

    }
    return render(request, 'journal_oks/oks.html', context)


# 


