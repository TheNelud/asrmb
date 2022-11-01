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


def create_koff_s_2pcalc(request):
    form = P2CalcForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P2CalcForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p2calc/table_form.html', context)


def update_koff_s_2pcalc(request, pk):
    rtp_1 = P2Calc.objects.get(id=pk)
    form = P2CalcForm(instance=rtp_1)
    if request.method == 'POST':
        form = P2CalcForm(request.POST, instance=rtp_1)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p2calc/table_form.html', context)


def delete_koff_s_2pcalc(request, pk):
    rtp_1 = P2Calc.objects.get(id=pk)
    if request.method == 'POST':
        rtp_1.delete()
        return redirect('/')
    context = {'item': rtp_1}
    return render(request, 'journal_koff_s/forms/koff_s_p2calc/delete.html', context)


def create_koff_s_3pcalc(request):
    form = P3CalcForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P3CalcForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p3calc/table_form.html', context)


def update_koff_s_3pcalc(request, pk):
    rtp_1 = P3Calc.objects.get(id=pk)
    form = P3CalcForm(instance=rtp_1)
    if request.method == 'POST':
        form = P3CalcForm(request.POST, instance=rtp_1)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p3calc/table_form.html', context)


def delete_koff_s_3pcalc(request, pk):
    rtp_1 = P3Calc.objects.get(id=pk)
    if request.method == 'POST':
        rtp_1.delete()
        return redirect('/')
    context = {'item': rtp_1}
    return render(request, 'journal_koff_s/forms/koff_s_p3calc/delete.html', context)


def create_koff_s_4pcalc(request):
    form = P4CalcForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P4CalcForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p4calc/table_form.html', context)


def update_koff_s_4pcalc(request, pk):
    rtp_1 = P4Calc.objects.get(id=pk)
    form = P4CalcForm(instance=rtp_1)
    if request.method == 'POST':
        form = P4CalcForm(request.POST, instance=rtp_1)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p4calc/table_form.html', context)


def delete_koff_s_4pcalc(request, pk):
    rtp_1 = P4Calc.objects.get(id=pk)
    if request.method == 'POST':
        rtp_1.delete()
        return redirect('/')
    context = {'item': rtp_1}
    return render(request, 'journal_koff_s/forms/koff_s_p4calc/delete.html', context)


def create_koff_s_5pcalc(request):
    form = P5CalcForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P5CalcForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p5calc/table_form.html', context)


def update_koff_s_5pcalc(request, pk):
    rtp_1 = P5Calc.objects.get(id=pk)
    form = P5CalcForm(instance=rtp_1)
    if request.method == 'POST':
        form = P5CalcForm(request.POST, instance=rtp_1)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p5calc/table_form.html', context)


def delete_koff_s_5pcalc(request, pk):
    rtp_1 = P5Calc.objects.get(id=pk)
    if request.method == 'POST':
        rtp_1.delete()
        return redirect('/')
    context = {'item': rtp_1}
    return render(request, 'journal_koff_s/forms/koff_s_p5calc/delete.html', context)


def create_koff_s_6pcalc(request):
    form = P6CalcForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P6CalcForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p6calc/table_form.html', context)


def update_koff_s_6pcalc(request, pk):
    rtp_1 = P6Calc.objects.get(id=pk)
    form = P6CalcForm(instance=rtp_1)
    if request.method == 'POST':
        form = P6CalcForm(request.POST, instance=rtp_1)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p6calc/table_form.html', context)


def delete_koff_s_6pcalc(request, pk):
    rtp_1 = P6Calc.objects.get(id=pk)
    if request.method == 'POST':
        rtp_1.delete()
        return redirect('/')
    context = {'item': rtp_1}
    return render(request, 'journal_koff_s/forms/koff_s_p6calc/delete.html', context)

def create_koff_s_7pcalc(request):
    form = P7CalcForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P7CalcForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p7calc/table_form.html', context)


def update_koff_s_7pcalc(request, pk):
    rtp_1 = P7Calc.objects.get(id=pk)
    form = P7CalcForm(instance=rtp_1)
    if request.method == 'POST':
        form = P7CalcForm(request.POST, instance=rtp_1)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_koff_s/forms/koff_s_p7calc/table_form.html', context)


def delete_koff_s_7pcalc(request, pk):
    rtp_1 = P7Calc.objects.get(id=pk)
    if request.method == 'POST':
        rtp_1.delete()
        return redirect('/')
    context = {'item': rtp_1}
    return render(request, 'journal_koff_s/forms/koff_s_p7calc/delete.html', context)