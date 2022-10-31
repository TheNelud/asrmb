from django.forms import ModelForm
from .models import *

class P5_appForm(ModelForm):
    class Meta:
        model = P5_app
        fields = '__all__'

class P6_appForm(ModelForm):
    class Meta:
        model = P6_app
        fields = '__all__'

class Perehod_stabilizaciiForm(ModelForm):
    class Meta:
        model = Perehod_stabilizacii
        fields = '__all__'

class Data_gas_stabilizationForm(ModelForm):
    class Meta:
        model = Data_gas_stabilization
        fields = '__all__'

class ConstForm(ModelForm):
    class Meta:
        model = Const
        fields = '__all__'