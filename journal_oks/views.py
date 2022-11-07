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


def create_oks_p3(request):
    form = P3DeterminationOfTheComponentOfGasForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P3DeterminationOfTheComponentOfGasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p3/table_form.html', context)


def update_oks_p3(request, pk):
    oks_p3 = P3DeterminationOfTheComponentOfGas.objects.get(id=pk)
    form = P3DeterminationOfTheComponentOfGasForm(instance=oks_p3)
    if request.method == 'POST':
        form = P3DeterminationOfTheComponentOfGasForm(request.POST, instance=oks_p3)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p3/table_form.html', context)


def delete_oks_p3(request, pk):
    oks_p3 = P3DeterminationOfTheComponentOfGas.objects.get(id=pk)
    if request.method == 'POST':
        oks_p3.delete()
        return redirect('/')
    context = {'item': oks_p3}
    return render(request, 'journal_oks/forms/oks_p3/delete.html', context)


def create_oks_p4(request):
    form = P4GasCompositionToTheProtocolForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P4GasCompositionToTheProtocolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p4/table_form.html', context)


def update_oks_p4(request, pk):
    oks_p4 = P4GasCompositionToTheProtocol.objects.get(id=pk)
    form = P4GasCompositionToTheProtocolForm(instance=oks_p4)
    if request.method == 'POST':
        form = P4GasCompositionToTheProtocolForm(request.POST, instance=oks_p4)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p4/table_form.html', context)


def delete_oks_p4(request, pk):
    oks_p4 = P4GasCompositionToTheProtocol.objects.get(id=pk)
    if request.method == 'POST':
        oks_p4.delete()
        return redirect('/')
    context = {'item': oks_p4}
    return render(request, 'journal_oks/forms/oks_p4/delete.html', context)


def create_oks_p5(request):
    form = P5DeterminationOfTheComponentCompositionForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P5DeterminationOfTheComponentCompositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p5/table_form.html', context)


def update_oks_p5(request, pk):
    oks_p5 = P5DeterminationOfTheComponentComposition.objects.get(id=pk)
    form = P5DeterminationOfTheComponentCompositionForm(instance=oks_p5)
    if request.method == 'POST':
        form = P5DeterminationOfTheComponentCompositionForm(request.POST, instance=oks_p5)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p5/table_form.html', context)


def delete_oks_p5(request, pk):
    oks_p5 = P5DeterminationOfTheComponentComposition.objects.get(id=pk)
    if request.method == 'POST':
        oks_p5.delete()
        return redirect('/')
    context = {'item': oks_p5}
    return render(request, 'journal_oks/forms/oks_p5/delete.html', context)


def create_oks_p6(request):
    form = P6CompositionOfGasOutputForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P6CompositionOfGasOutputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p6/table_form.html', context)


def update_oks_p6(request, pk):
    oks_p6 = P6CompositionOfGasOutput.objects.get(id=pk)
    form = P6CompositionOfGasOutputForm(instance=oks_p6)
    if request.method == 'POST':
        form = P6CompositionOfGasOutputForm(request.POST, instance=oks_p6)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p6/table_form.html', context)


def delete_oks_p6(request, pk):
    oks_p6 = P6CompositionOfGasOutput.objects.get(id=pk)
    if request.method == 'POST':
        oks_p6.delete()
        return redirect('/')
    context = {'item': oks_p6}
    return render(request, 'journal_oks/forms/oks_p6/delete.html', context)


def create_oks_p7(request):
    form = P7CompositionOfGas10cForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P7CompositionOfGas10cForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p7/table_form.html', context)


def update_oks_p7(request, pk):
    oks_p7 = P7CompositionOfGas10c.objects.get(id=pk)
    form = P7CompositionOfGas10cForm(instance=oks_p7)
    if request.method == 'POST':
        form = P7CompositionOfGas10cForm(request.POST, instance=oks_p7)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p7/table_form.html', context)


def delete_oks_p7(request, pk):
    oks_p7 = P7CompositionOfGas10c.objects.get(id=pk)
    if request.method == 'POST':
        oks_p7.delete()
        return redirect('/')
    context = {'item': oks_p7}
    return render(request, 'journal_oks/forms/oks_p7/delete.html', context)


def create_oks_p8(request):
    form = P8CompositionOfTheCondensateForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P8CompositionOfTheCondensateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p8/table_form.html', context)


def update_oks_p8(request, pk):
    oks_p8 = P8CompositionOfTheCondensate.objects.get(id=pk)
    form = P1ComponentCompositionOfUnstableCondensateForm(instance=oks_p8)
    if request.method == 'POST':
        form = P1ComponentCompositionOfUnstableCondensateForm(request.POST, instance=oks_p8)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p8/table_form.html', context)


def delete_oks_p8(request, pk):
    oks_p8 = P8CompositionOfTheCondensate.objects.get(id=pk)
    if request.method == 'POST':
        oks_p8.delete()
        return redirect('/')
    context = {'item': oks_p8}
    return render(request, 'journal_oks/forms/oks_p8/delete.html', context)


def create_oks_p9(request):
    form = P9ComponentOfTheSeparationGasForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P9ComponentOfTheSeparationGasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p9/table_form.html', context)


def update_oks_p9(request, pk):
    oks_p9 = P9ComponentOfTheSeparationGas.objects.get(id=pk)
    form = P9ComponentOfTheSeparationGasForm(instance=oks_p9)
    if request.method == 'POST':
        form = P9ComponentOfTheSeparationGasForm(request.POST, instance=oks_p9)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p9/table_form.html', context)


def delete_oks_p9(request, pk):
    oks_p9 = P9ComponentOfTheSeparationGas.objects.get(id=pk)
    if request.method == 'POST':
        oks_p9.delete()
        return redirect('/')
    context = {'item': oks_p9}
    return render(request, 'journal_oks/forms/oks_p9/delete.html', context)


def create_oks_p10(request):
    form = P10ProtokolKGNForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = P10ProtokolKGNForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p10/table_form.html', context)


def update_oks_p10(request, pk):
    oks_p10 = P10ProtokolKGN.objects.get(id=pk)
    form = P10ProtokolKGNForm(instance=oks_p10)
    if request.method == 'POST':
        form = P10ProtokolKGNForm(request.POST, instance=oks_p10)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_oks/forms/oks_p10/table_form.html', context)


def delete_oks_p10(request, pk):
    oks_p10 = P10ProtokolKGN.objects.get(id=pk)
    if request.method == 'POST':
        oks_p10.delete()
        return redirect('/')
    context = {'item': oks_p10}
    return render(request, 'journal_oks/forms/oks_p10/delete.html', context)
