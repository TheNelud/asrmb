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


# def create_rmo_p5(request):
#     form = P5_appForm()
#     if request.method == 'POST':
#         # print('Печать сообщения: ', request.POST)
#         form = P5_appForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#
#     context = {'form': form}
#     return render(request, 'journal_rmo/forms/koff_s_p2calc/table_form.html', context)


# def update_rmo_p5(request, pk):
#     rmo = P5_app.objects.get(id=pk)
#     form = P5_appForm(instance=rmo)
#     if request.method == 'POST':
#         form = P5_appForm(request.POST, instance=rmo)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form': form}
#     return render(request, 'journal_rmo/forms/koff_s_p2calc/table_form.html', context)
#
#
# def delete_rmo_p5(request, pk):
#     rmo = P5_app.objects.get(id=pk)
#     if request.method == 'POST':
#         rmo.delete()
#         return redirect('/')
#     context = {'item': rmo}
#     return render(request, 'journal_rmo/forms/koff_s_p2calc/delete.html', context)
#
#
# def create_rmo_p6(request):
#     form = P6_appForm()
#     if request.method == 'POST':
#         # print('Печать сообщения: ', request.POST)
#         form = P6_appForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#
#     context = {'form': form}
#     return render(request, 'journal_rmo/forms/rmo_p6/table_form.html', context)
#
#
# def update_rmo_p6(request, pk):
#     rmo = P6_app.objects.get(id=pk)
#     form = P6_appForm(instance=rmo)
#     if request.method == 'POST':
#         form = P6_appForm(request.POST, instance=rmo)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form': form}
#     return render(request, 'journal_rmo/forms/rmo_p6/table_form.html', context)
#
#
# def delete_rmo_p6(request, pk):
#     rmo = P6_app.objects.get(id=pk)
#     if request.method == 'POST':
#         rmo.delete()
#         return redirect('/')
#     context = {'item': rmo}
#     return render(request, 'journal_rmo/forms/rmo_p6/delete.html', context)




def create_rmo_lg(request):
    form = Losses_gasForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = Losses_gasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rmo/forms/rmo_lg/table_form.html', context)


def update_rmo_lg(request, pk):
    rmo = Losses_gas.objects.get(id=pk)
    form = Losses_gasForm(instance=rmo)
    if request.method == 'POST':
        form = Losses_gasForm(request.POST, instance=rmo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rmo/forms/rmo_lg/table_form.html', context)


def delete_rmo_lg(request, pk):
    rmo = Losses_gas.objects.get(id=pk)
    if request.method == 'POST':
        rmo.delete()
        return redirect('/')
    context = {'item': rmo}
    return render(request, 'journal_rmo/forms/rmo_lg/delete.html', context)

def create_rmo_md(request):
    form = Meters_data_20e_1Form()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = Meters_data_20e_1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rmo/forms/rmo_md/table_form.html', context)


def update_rmo_md(request, pk):
    rmo = Meters_data_20e_1.objects.get(id=pk)
    form = Meters_data_20e_1Form(instance=rmo)
    if request.method == 'POST':
        form = Meters_data_20e_1Form(request.POST, instance=rmo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rmo/forms/rmo_lg/table_form.html', context)


def delete_rmo_md(request, pk):
    rmo = Meters_data_20e_1.objects.get(id=pk)
    if request.method == 'POST':
        rmo.delete()
        return redirect('/')
    context = {'item': rmo}
    return render(request, 'journal_rmo/forms/rmo_md/delete.html', context)



def create_rmo_ps(request):
    form = Perehod_stabilizaciiForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = Perehod_stabilizaciiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rmo/forms/rmo_ps/table_form.html', context)


def update_rmo_ps(request, pk):
    rmo = Perehod_stabilizacii.objects.get(id=pk)
    form = Perehod_stabilizaciiForm(instance=rmo)
    if request.method == 'POST':
        form = Perehod_stabilizaciiForm(request.POST, instance=rmo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rmo/forms/rmo_ps/table_form.html', context)


def delete_rmo_ps(request, pk):
    rmo = Perehod_stabilizacii.objects.get(id=pk)
    if request.method == 'POST':
        rmo.delete()
        return redirect('/')
    context = {'item': rmo}
    return render(request, 'journal_rmo/forms/rmo_ps/delete.html', context)
