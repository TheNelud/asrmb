from django.shortcuts import render
from .models import *


def index(request):
    data_coef = Coef.objects.all()
    data_losses = Losses.objects.all()
    data_mol_mass = MolMass.objects.all()

    data_p1 = P1ComponentCompositionOfUnstableCondensate.objects.all()
    data_p2 = P2ComponentCompositionOfGas.objects.all()
    data_p3 = P3DeterminationOfTheComponentOfGas.objects.all()
    data_p4 = P4GasCompositionToTheProtocol.objects.all()
    data_p5 = P5DeterminationOfTheComponentComposition.objects.all()
    data_p6 = P6CompositionOfGasOutput.objects.all()
    data_p7 = P7CompositionOfGas10c.objects.all()
    data_p8 = P8CompositionOfTheCondensate.objects.all()
    data_p9 = P9ComponentOfTheSeparationGas.objects.all()
    data_p10 = P10ProtokolKGN.objects.all()

    context = {
        'coef': data_coef,
        'losses': data_losses,
        'mol_mass': data_mol_mass,

        'oks_p1': data_p1,
        'oks_p2': data_p2,
        'oks_p3': data_p3,
        'oks_p4': data_p4,
        'oks_p5': data_p5,
        'oks_p6': data_p6,
        'oks_p7': data_p7,
        'oks_p8': data_p8,
        'oks_p9': data_p9,
        'oks_p10': data_p10,
    }
    return render(request, "journal/journal.html", context)
