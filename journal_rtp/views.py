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


def create_rtp_3(request):
    form = TeclossesTreeForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = TeclossesTreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/rtp_3/table_form.html', context)


def update_rtp_3(request, pk):
    rtp_3 = TeclossesTree.objects.get(id=pk)
    form = TeclossesTreeForm(instance=rtp_3)
    if request.method == 'POST':
        form = TeclossesTreeForm(request.POST, instance=rtp_3)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/rtp_3/table_form.html', context)


def delete_rtp_3(request, pk):
    rtp_3 = TeclossesTree.objects.get(id=pk)
    if request.method == 'POST':
        rtp_3.delete()
        return redirect('/')
    context = {'item': rtp_3}
    return render(request, 'journal_rtp/forms/rtp_3/delete.html', context)


# _____________________________________________________________________________________

def create_rppp_1(request):
    form = RecyclingcalcOneForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = RecyclingcalcOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_1/table_form.html', context)


def update_rppp_1(request, pk):
    rppp = RecyclingcalcOne.objects.get(id=pk)
    form = RecyclingcalcOneForm(instance=rppp)
    if request.method == 'POST':
        form = RecyclingcalcOneForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_1/table_form.html', context)


def delete_rppp_1(request, pk):
    rppp = RecyclingcalcOne.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/rppp_1/delete.html', context)


def create_rppp_2(request):
    form = RecyclingcalcTwoForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = RecyclingcalcTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_2/table_form.html', context)


def update_rppp_2(request, pk):
    rppp = RecyclingcalcTwo.objects.get(id=pk)
    form = RecyclingcalcTwoForm(instance=rppp)
    if request.method == 'POST':
        form = RecyclingcalcTwoForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_2/table_form.html', context)


def delete_rppp_2(request, pk):
    rppp = RecyclingcalcTwo.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/rppp_2/delete.html', context)


def create_rppp_3(request):
    form = RecyclingcalcThreeForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = RecyclingcalcThreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_3/table_form.html', context)


def update_rppp_3(request, pk):
    rppp = RecyclingcalcThree.objects.get(id=pk)
    form = RecyclingcalcThreeForm(instance=rppp)
    if request.method == 'POST':
        form = RecyclingcalcThreeForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_3/table_form.html', context)


def delete_rppp_3(request, pk):
    rppp = RecyclingcalcThree.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/rppp_3/delete.html', context)


def create_rppp_4(request):
    form = RecyclingcalcFourForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = RecyclingcalcFourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_4/table_form.html', context)


def update_rppp_4(request, pk):
    rppp = RecyclingcalcFour.objects.get(id=pk)
    form = RecyclingcalcFourForm(instance=rppp)
    if request.method == 'POST':
        form = RecyclingcalcFourForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_4/table_form.html', context)


def delete_rppp_4(request, pk):
    rppp = RecyclingcalcFour.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/rppp_51/delete.html', context)


def create_rppp_51(request):
    form = RecyclingcalcFive1Form()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = RecyclingcalcFive1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_51/table_form.html', context)


def update_rppp_51(request, pk):
    rppp = RecyclingcalcFive1.objects.get(id=pk)
    form = RecyclingcalcFive1Form(instance=rppp)
    if request.method == 'POST':
        form = RecyclingcalcFive1Form(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_51/table_form.html', context)


def delete_rppp_51(request, pk):
    rppp = RecyclingcalcFive1.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/rppp_51/delete.html', context)


def create_rppp_52(request):
    form = RecyclingcalcFive2Form()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = RecyclingcalcFive2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_52/table_form.html', context)


def update_rppp_52(request, pk):
    rppp = RecyclingcalcFive2.objects.get(id=pk)
    form = RecyclingcalcFive2Form(instance=rppp)
    if request.method == 'POST':
        form = RecyclingcalcFive2Form(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_52/table_form.html', context)


def delete_rppp_52(request, pk):
    rppp = RecyclingcalcFive2.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/rppp_52/delete.html', context)


def create_rppp_6(request):
    form = RecyclingcalcSixForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = RecyclingcalcSixForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_52/table_form.html', context)


def update_rppp_6(request, pk):
    rppp = RecyclingcalcSix.objects.get(id=pk)
    form = RecyclingcalcSixForm(instance=rppp)
    if request.method == 'POST':
        form = RecyclingcalcSixForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/rppp_6/table_form.html', context)


def delete_rppp_6(request, pk):
    rppp = RecyclingcalcSix.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/rppp_6/delete.html', context)


# ---------------------------------------------------------------------------------------------

def create_nrtp_1(request):
    form = CondensateprodOneForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = CondensateprodOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrtp_1/table_form.html', context)


def update_nrtp_1(request, pk):
    rppp = CondensateprodOne.objects.get(id=pk)
    form = CondensateprodOneForm(instance=rppp)
    if request.method == 'POST':
        form = CondensateprodOneForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrtp_1/table_form.html', context)


def delete_nrtp_1(request, pk):
    rppp = CondensateprodOne.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrtp_1/delete.html', context)


def create_nrtp_2(request):
    form = CondensateprodTwoForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = CondensateprodTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrtp_2/table_form.html', context)


def update_nrtp_2(request, pk):
    rppp = CondensateprodTwo.objects.get(id=pk)
    form = CondensateprodTwoForm(instance=rppp)
    if request.method == 'POST':
        form = CondensateprodTwoForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrtp_2/table_form.html', context)


def delete_nrtp_2(request, pk):
    rppp = CondensateprodTwo.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrtp_2/delete.html', context)


def create_nrtp_31(request):
    form = CondensateprodThree1Form()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = CondensateprodThree1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrtp_31/table_form.html', context)


def update_nrtp_31(request, pk):
    rppp = CondensateprodThree1.objects.get(id=pk)
    form = CondensateprodThree1Form(instance=rppp)
    if request.method == 'POST':
        form = CondensateprodThree1Form(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrtp_31/table_form.html', context)


def delete_nrtp_31(request, pk):
    rppp = CondensateprodThree1.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrtp_31/delete.html', context)


def create_nrtp_32(request):
    form = CondensateprodThree2Form()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = CondensateprodThree2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrtp_32/table_form.html', context)


def update_nrtp_32(request, pk):
    rppp = CondensateprodThree2.objects.get(id=pk)
    form = CondensateprodThree2Form(instance=rppp)
    if request.method == 'POST':
        form = CondensateprodThree2Form(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrtp_32/table_form.html', context)


def delete_nrtp_32(request, pk):
    rppp = CondensateprodThree2.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrtp_32/delete.html', context)



#------------------------------------------------------------------------------------
def create_nrppp_1(request):
    form = CondrecyclingOneForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = CondrecyclingOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_1/table_form.html', context)


def update_nrppp_1(request, pk):
    rppp = CondrecyclingOne.objects.get(id=pk)
    form = CondrecyclingOneForm(instance=rppp)
    if request.method == 'POST':
        form = CondrecyclingOneForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_1/table_form.html', context)


def delete_nrppp_1(request, pk):
    rppp = CondrecyclingOne.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrppp_1/delete.html', context)

def create_nrppp_2(request):
    form = CondrecyclingTwoForm()
    if request.method == 'POST':
        # print('Печать сообщения: ', request.POST)
        form = CondrecyclingTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_2/table_form.html', context)


def update_nrppp_2(request, pk):
    rppp = CondrecyclingTwo.objects.get(id=pk)
    form = CondrecyclingTwoForm(instance=rppp)
    if request.method == 'POST':
        form = CondrecyclingTwoForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_2/table_form.html', context)


def delete_nrppp_2(request, pk):
    rppp = CondrecyclingTwo.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrppp_2/delete.html', context)


def create_nrppp_3(request):
    form = CondrecyclingThreeForm()
    if request.method == 'POST':
        form = CondrecyclingThreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_3/table_form.html', context)


def update_nrppp_3(request, pk):
    rppp = CondrecyclingThree.objects.get(id=pk)
    form = CondrecyclingThreeForm(instance=rppp)
    if request.method == 'POST':
        form = CondrecyclingThreeForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_3/table_form.html', context)


def delete_nrppp_3(request, pk):
    rppp = CondrecyclingThree.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrppp_3/delete.html', context)

def create_nrppp_4(request):
    form = CondrecyclingFourForm()
    if request.method == 'POST':
        form = CondrecyclingFourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_4/table_form.html', context)


def update_nrppp_4(request, pk):
    rppp = CondrecyclingFour.objects.get(id=pk)
    form = CondrecyclingFourForm(instance=rppp)
    if request.method == 'POST':
        form = CondrecyclingFourForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_4/table_form.html', context)


def delete_nrppp_4(request, pk):
    rppp = CondrecyclingFour.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrppp_4/delete.html', context)


def create_nrppp_5(request):
    form = CondrecyclingFiveForm()
    if request.method == 'POST':
        form = CondrecyclingFiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_5/table_form.html', context)


def update_nrppp_5(request, pk):
    rppp = CondrecyclingFive.objects.get(id=pk)
    form = CondrecyclingFiveForm(instance=rppp)
    if request.method == 'POST':
        form = CondrecyclingFiveForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_5/table_form.html', context)


def delete_nrppp_5(request, pk):
    rppp = CondrecyclingFive.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrppp_5/delete.html', context)


def create_nrppp_6(request):
    form = CondrecyclingSixForm()
    if request.method == 'POST':
        form = CondrecyclingSixForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_6/table_form.html', context)


def update_nrppp_6(request, pk):
    rppp = CondrecyclingSix.objects.get(id=pk)
    form = CondrecyclingSixForm(instance=rppp)
    if request.method == 'POST':
        form = CondrecyclingSixForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_6/table_form.html', context)


def delete_nrppp_6(request, pk):
    rppp = CondrecyclingSixForm.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrppp_6/delete.html', context)

def create_nrppp_7(request):
    form = CondrecyclingSevenForm()
    if request.method == 'POST':
        form = CondrecyclingSevenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_7/table_form.html', context)


def update_nrppp_7(request, pk):
    rppp = CondrecyclingSeven.objects.get(id=pk)
    form = CondrecyclingSevenForm(instance=rppp)
    if request.method == 'POST':
        form = CondrecyclingSevenForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_7/table_form.html', context)


def delete_nrppp_7(request, pk):
    rppp = CondrecyclingSeven.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrppp_7/delete.html', context)

def create_nrppp_8(request):
    form = CondrecyclingEightForm()
    if request.method == 'POST':
        form = CondrecyclingEightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_8/table_form.html', context)


def update_nrppp_8(request, pk):
    rppp = CondrecyclingEight.objects.get(id=pk)
    form = CondrecyclingEightForm(instance=rppp)
    if request.method == 'POST':
        form = CondrecyclingEightForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_8/table_form.html', context)


def delete_nrppp_8(request, pk):
    rppp = CondrecyclingEight.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrppp_8/delete.html', context)

def create_nrppp_9(request):
    form = CondrecyclingNineForm()
    if request.method == 'POST':
        form = CondrecyclingNineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_9/table_form.html', context)


def update_nrppp_9(request, pk):
    rppp = CondrecyclingNine.objects.get(id=pk)
    form = CondrecyclingNineForm(instance=rppp)
    if request.method == 'POST':
        form = CondrecyclingNineForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_9/table_form.html', context)


def delete_nrppp_9(request, pk):
    rppp = CondrecyclingNine.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrppp_9/delete.html', context)


def create_nrppp_10(request):
    form = CondrecyclingTenForm()
    if request.method == 'POST':
        form = CondrecyclingTenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_10/table_form.html', context)


def update_nrppp_10(request, pk):
    rppp = CondrecyclingTen.objects.get(id=pk)
    form = CondrecyclingTenForm(instance=rppp)
    if request.method == 'POST':
        form = CondrecyclingTenForm(request.POST, instance=rppp)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'journal_rtp/forms/nrppp_10/table_form.html', context)


def delete_nrppp_10(request, pk):
    rppp = CondrecyclingTen.objects.get(id=pk)
    if request.method == 'POST':
        rppp.delete()
        return redirect('/')
    context = {'item': rppp}
    return render(request, 'journal_rtp/forms/nrppp_10/delete.html', context)
