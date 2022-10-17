from django.shortcuts import render
from .models import *


def index(request):
    data_coef = Coef.objects.all()
    data_losses = Losses.objects.all()
    data_mol_mass = MolMass.objects.all()

    context = {
        'coef': data_coef,
        'losses': data_losses,
        'mol_mass': data_mol_mass,
    }
    return render(request, "journal/journal.html", context)
