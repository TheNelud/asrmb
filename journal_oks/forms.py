from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget
from django.contrib.admin import widgets
import datetime
# from django.forms.fields import DateTimeField


# for schema public -------------------------------------------------------------------------->
class P1ComponentCompositionOfUnstableCondensateForm(ModelForm):
    name = forms.CharField(label="Компонент",max_length=255)
    molar_components = forms.FloatField(label="Мольное содержание компонентов, %")
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента')
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль')
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)')
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)')
    time = forms.DateField(label='Дата')

    class Meta:
        model = P1ComponentCompositionOfUnstableCondensate
        fields = '__all__'
        widgets = {
            "time" :  AdminDateWidget()
        }

class P2ComponentCompositionOfGasForm(ModelForm):
    name = forms.CharField(label="Компонент",max_length=255)
    molar_components = forms.FloatField(label="Мольное содержание компонентов, %")
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента')
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль')
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)')
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)')
    time = forms.DateTimeField(label='Дата')
    class Meta:
        model = P2ComponentCompositionOfGas
        fields = '__all__'

class P3DeterminationOfTheComponentOfGasForm(ModelForm):
    name = forms.CharField(label="Компонент",max_length=255)
    molar_components = forms.FloatField(label="Мольное содержание компонентов, %")
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента')
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль')
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)')
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)')
    time = forms.DateTimeField(label='Дата')
    class Meta:
        model = P3DeterminationOfTheComponentOfGas
        fields = '__all__'

class P4GasCompositionToTheProtocolForm(ModelForm):
    class Meta:
        model = P4GasCompositionToTheProtocol
        fields = '__all__'

class P5DeterminationOfTheComponentCompositionForm(ModelForm):
    class Meta:
        model = P5DeterminationOfTheComponentComposition
        fields = '__all__'

class P6CompositionOfGasOutputForm(ModelForm):
    class Meta:
        model = P6CompositionOfGasOutput
        fields = '__all__'

class P7CompositionOfGas10cForm(ModelForm):
    class Meta:
        model = P7CompositionOfGas10c
        fields = '__all__'

class P8CompositionOfTheCondensateForm(ModelForm):
    class Meta:
        model = P8CompositionOfTheCondensate
        fields = '__all__'

class P9ComponentOfTheSeparationGasForm(ModelForm):
    class Meta:
        model = P9ComponentOfTheSeparationGas
        fields = '__all__'

class P10ProtokolKGNForm(ModelForm):
    class Meta:
        model = P10ProtokolKGN
        fields = '__all__'

#------------------------------------------------------------------------------------------------>