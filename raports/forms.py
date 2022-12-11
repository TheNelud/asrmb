from django import forms
from .models import *
from django.forms import ModelForm


class DateForm(forms.Form):
    date_update = forms.DateTimeField(widget=forms.TextInput(attrs=
                                {
                                    'class':'form-control'
                                })) 

    class Meta:
        model = Ser_per_day
        fields = ['date_update']


"""МЭГ добавление значений для расчетов"""
class BalanceForm(ModelForm):
    update_time = forms.DateTimeField(label='Дата')
    par_d = forms.FloatField(label="Приход товарного МЭГ (100% мас.) на склад фКГДУ (поз.6) ")      
    par_e = forms.FloatField(label="Приход товарного МЭГ 100% со склада ПБ на склад УКПГ (поз.20)")      
    par_f = forms.FloatField(label="Вовлечение товарного МЭГ со склада УКПГ (поз.20)")      
    par_g = forms.FloatField(label="Концентрация МЭ")
    par_h = forms.FloatField(label="Плотность рМЭГ")
    par_v = forms.FloatField(label="Потери МЭГ на РЭН")      
    par_w = forms.FloatField(label="КГС после УСК") 
    
    class Meta:
        mobel = Balance
        fields = ["par_d","par_e","par_f","par_g",
                  "par_h","par_v","par_w"]
