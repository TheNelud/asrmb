from django import forms
from .models import *
from django.forms import ModelForm, TextInput


class DateForm(forms.Form):
    date_sar = forms.DateTimeField( input_formats=['%Y.%m.%d'],
        
                                    widget=forms.DateTimeInput(attrs=
                                {
                                    'type':'date',
                                    'id':'id_date'
                                })) 

    # class Meta:
    #     model = Ser_per_day
        # fields = ['date_update']


"""МЭГ добавление значений для расчетов"""
class BalanceForm(ModelForm):
    # date_update = forms.DateTimeField(label='Дата')
    par_d = forms.FloatField(label="Приход товарного МЭГ (100% мас.) на склад фКГДУ (поз.6) ")      
    par_e = forms.FloatField(label="Приход товарного МЭГ 100% со склада ПБ на склад УКПГ (поз.20)")      
    par_f = forms.FloatField(label="Вовлечение товарного МЭГ со склада УКПГ (поз.20)")      
    par_g_nmag = forms.FloatField(label="Концентрация нМЭГ")
    par_g_rmag_30i_1 = forms.FloatField(label="Концентрация рМЭГ 30И-1")
    par_g_rmag_60e_1 = forms.FloatField(label="Концентрация рМЭГ 60E-1")
    par_h = forms.FloatField(label="Плотность рМЭГ")
    par_v = forms.FloatField(label="Потери МЭГ на РЭН")      
    par_w = forms.FloatField(label="КГС после УСК") 
    
    class Meta:
        model = Balance
        fields = ["par_d","par_e","par_f","par_g_nmag",
                    "par_g_rmag_30i_1","par_g_rmag_60e_1",
                  "par_h","par_v","par_w"]
    
    
