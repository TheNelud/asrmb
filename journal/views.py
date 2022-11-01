from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, "journal/main.html")










# def koff(request):
#     data_coef = Coef.objects.all()
#     data_losses = Losses.objects.all()
#     data_mol_mass = MolMass.objects.all()
#     context = {
#         'coef': data_coef,
#         'losses': data_losses,
#         'mol_mass': data_mol_mass,
#     }
#     return render(request, 'journal/koff.html', context)





def pgk(request):
    return render(request, 'journal/pgk.html')
