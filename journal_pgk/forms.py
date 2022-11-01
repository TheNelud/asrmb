from django.forms import ModelForm
from .models import *

class Calc_lossesForm(ModelForm):
    class Meta:
        model = Calc_losses
        fields = '__all__'

class Losses_gas_apparatusForm(ModelForm):
    class Meta:
        model = Losses_gas_apparatus
        fields = '__all__'