from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def koff_s(request):
    data_coef_ptm = CoefPTM.objects.all()
    data_p2calc = P2Calc.objects.all()
    data_p3calc = P3Calc.objects.all()
    data_p4calc = P4Calc.objects.all()
    data_p5calc = P5Calc.objects.all()
    data_p6calc = P6Calc.objects.all()
    data_p7calc = P7Calc.objects.all()
    data_tab_coef_all = TabCoefAll.objects.all()
    data_tab_sum_all = TabSumAll.objects.all()
    data_total_calc = TotalCalc.objects.all()

    context = {
        'data_coef_ptm': data_coef_ptm,
        'data_p2calc': data_p2calc,
        'data_p3calc': data_p3calc,
        'data_p4calc': data_p4calc,
        'data_p5calc': data_p5calc,
        'data_p6calc': data_p6calc,
        'data_p7calc': data_p7calc,
        'data_tab_coef_all': data_tab_coef_all,
        'data_tab_sum_all': data_tab_sum_all,
        'data_total_calc': data_total_calc,

    }

    return render(request, 'journal_koff_s/koff_s.html', context)


