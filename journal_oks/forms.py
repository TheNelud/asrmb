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
    # total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль')
    # chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)')
    # calculated_mass = forms.FloatField(label='Масс, % (расчетная)')
    # time = forms.DateField(label='Дата')

    class Meta:
        model = P1ComponentCompositionOfUnstableCondensate
        # fields = '__all__'
        fields = ['name','molar_components', 'molar_mass_of_the_component']
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
        # fields = ['name','molar_components', 'molar_mass_of_the_component']

class P3DeterminationOfTheComponentOfGasForm(ModelForm):
    name = forms.CharField(label="Компонент",max_length=255)
    molar_components = forms.FloatField(label="Мольное содержание компонентов, %")
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента')
    # total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль')
    # chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)')
    # calculated_mass = forms.FloatField(label='Масс, % (расчетная)')
    # time = forms.DateTimeField(label='Дата')
    class Meta:
        model = P3DeterminationOfTheComponentOfGas
        # fields = '__all__'
        fields = ['name','molar_components', 'molar_mass_of_the_component']

class P4GasCompositionToTheProtocolForm(ModelForm):
    name = forms.CharField(max_length=255, label="Компонент")
    molar_components = forms.FloatField(label="Мольное содержание компонентов, %")
    molar_mass_of_the_component = forms.FloatField(label="Молярная масса компонента")
    # total_molar_mass = forms.FloatField(label="Молярная масса общая, гр/моль")
    # chromatograph_mass = forms.FloatField(label="Масс, % (хрома-тограф)")
    # calculated_mass = forms.FloatField(label="Масс, % (расчетная)")
    # content_of_the_component = forms.FloatField(label="Содержание компонента в  газе, кг/м3")
    # proportion_of_the_component = forms.FloatField(label="Доля компонента в 1м3 газа")
    # time = forms.DateTimeField(label="Дата")
    class Meta:
        model = P4GasCompositionToTheProtocol
        # fields = '__all__'
        fields = ['name','molar_components', 'molar_mass_of_the_component']

class P5DeterminationOfTheComponentCompositionForm(ModelForm):
    name = forms.CharField(max_length=255, label="Компонент")
    molar_components = forms.FloatField(label="мольное содержание компонентов, %")
    molar_mass_of_the_component = forms.FloatField(label="Молярная масса компо-нента")
    # total_molar_mass = forms.FloatField(label="Молярная масса , гр/моль")
    # chromatograph_mass = forms.FloatField(label="масс, % (хрома-тограф)")
    # calculated_mass = forms.FloatField(label="масс, % (расчетная)")
    # time = forms.DateTimeField(label="Дата")
    class Meta:
        model = P5DeterminationOfTheComponentComposition
        # fields = '__all__'
        fields = ['name','molar_components', 'molar_mass_of_the_component']
 
class P6CompositionOfGasOutputForm(ModelForm):
    name = forms.CharField(max_length=255, label="Компонент")
    molar_components = forms.FloatField(label="мольное содержание компонентов, %")
    molar_mass_of_the_component = forms.FloatField(label="Молярная масса компо-нента")
    # total_molar_mass = forms.FloatField(label="Молярная масса , гр/моль")
    # chromatograph_mass = forms.FloatField(label="масс, % (хрома-тограф)")
    # calculated_mass = forms.FloatField(label="масс, % (расчетная)")
    # time = forms.DateTimeField(label="Дата")
    class Meta:
        model = P6CompositionOfGasOutput
        # fields = '__all__'
        fields = ['name','molar_components', 'molar_mass_of_the_component']

class P7CompositionOfGas10cForm(ModelForm):
    name = forms.CharField(max_length=255, label="Компонент")
    molar_components = forms.FloatField(label="мольное содержание компонентов, %")
    molar_mass_of_the_component = forms.FloatField(label="Молярная масса компо-нента")
    # total_molar_mass = forms.FloatField(label="Молярная масса общая, гр/моль")
    # chromatograph_mass = forms.FloatField(label="масс, % (хрома-тограф)")
    # calculated_mass = forms.FloatField(label="масс, % (расчетная)")
    # time = forms.DateTimeField(label="Дата")
    class Meta:
        model = P7CompositionOfGas10c
        # fields = '__all__'
        fields = ['name','molar_components', 'molar_mass_of_the_component']

class P8CompositionOfTheCondensateForm(ModelForm):
    name = forms.CharField(max_length=255, label="Компонент")
    cylinder_1506 = forms.FloatField(label="Балон 1506")
    cylinder_1641 = forms.FloatField(label="Балон 1641")
    # average_value = forms.FloatField(label="Среднее")
    # time = forms.DateTimeField(label="Дата")
    class Meta:
        model = P8CompositionOfTheCondensate
        # fields = '__all__'
        fields = ['name','cylinder_1506', 'cylinder_1641']


class P9ComponentOfTheSeparationGasForm(ModelForm):
    name = forms.CharField(max_length=255, label="Компонент")
    molar_components = forms.FloatField(label="мольное содержание компонентов, %")
    molar_mass_of_the_component = forms.FloatField(label="Молярная масса компонента")
    # total_molar_mass = forms.FloatField(label="Молярная масса общая, гр/моль")
    # chromatograph_mass = forms.FloatField(label="масс, % (хрома-тограф)")
    # calculated_mass = forms.FloatField(label="масс, % (расчетная)")
    # time = forms.DateTimeField(label="Дата")
    class Meta:
        model = P9ComponentOfTheSeparationGas
        # fields = '__all__'
        fields = ['name','molar_components', 'molar_mass_of_the_component']

class P10ProtokolKGNForm(ModelForm):
    name = forms.CharField(max_length=255, label="Компонент")
    соmposition = forms.FloatField(label="Состав")
    # molar_mass_of_the_component = forms.FloatField(label="Молярная масса компо-нента")
    chromatograph_mass = forms.FloatField(label="масс, % (хрома-тограф)")
    # proportion = forms.FloatField(label="Разность")
    # time = forms.DateTimeField(label="Дата")
    class Meta:
        model = P10ProtokolKGN
        # fields = '__all__'
        fields = ['name','соmposition', 'chromatograph_mass']

#------------------------------------------------------------------------------------------------>