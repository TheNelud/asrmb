from django.forms import ModelForm
from .models import *

# class P5_appForm(ModelForm):
#     class Meta:
#         model = P5_app
#         fields = '__all__'
#
# class P6_appForm(ModelForm):
#     class Meta:
#         model = P6_app
#         fields = '__all__'


class Losses_gasForm(ModelForm):
    class Meta:
        model = Losses_gas
        fields = '__all__'

class Meters_data_20e_1Form(ModelForm):
    class Meta:
        model = Meters_data_20e_1
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