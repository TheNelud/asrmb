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
    par_d = forms.CharField(label="Приход товарного МЭГ (100% мас.) на склад фКГДУ (поз.6) ")      
    par_e = forms.CharField(label="Приход товарного МЭГ 100% со склада ПБ на склад УКПГ (поз.20)")      
    par_f = forms.CharField(label="Вовлечение товарного МЭГ со склада УКПГ (поз.20)")      
    par_g_nmag = forms.CharField(label="Концентрация нМЭГ")
    par_g_rmag_30i_1 = forms.CharField(label="Концентрация рМЭГ 30И-1")
    par_g_rmag_60e_1 = forms.CharField(label="Концентрация рМЭГ 60E-1")
    par_h = forms.CharField(label="Плотность рМЭГ")
    par_v = forms.CharField(label="Потери МЭГ на РЭН")      
    par_w = forms.CharField(label="КГС после УСК") 
    
    class Meta:
        model = Balance
        # fields = '__all__'
        fields = ["par_d","par_e","par_f","par_g_nmag",
                    "par_g_rmag_30i_1","par_g_rmag_60e_1",
                  "par_h","par_v","par_w"]
    
    """Для редактирование рапорта СЭР"""
class Ser_per_day_form(ModelForm):
    ser_1 = forms.CharField(max_length=255)
    ser_2 = forms.CharField(max_length=255)
    ser_3 = forms.CharField(max_length=255)
    ser_4 = forms.CharField(max_length=255)
    ser_5 = forms.CharField(max_length=255)
    ser_6 = forms.CharField(max_length=255)
    ser_7 = forms.CharField(max_length=255)
    ser_8 = forms.CharField(max_length=255)
    ser_9 = forms.CharField(max_length=255)
    ser_10 = forms.CharField(max_length=255)
    ser_11 = forms.CharField(max_length=255)
    ser_12 = forms.CharField(max_length=255)
    ser_13 = forms.CharField(max_length=255)
    ser_14 = forms.CharField(max_length=255)
    ser_15 = forms.CharField(max_length=255)
    ser_16 = forms.CharField(max_length=255)
    ser_17 = forms.CharField(max_length=255)
    ser_18 = forms.CharField(max_length=255)
    ser_19 = forms.CharField(max_length=255)
    ser_20 = forms.CharField(max_length=255) 
    date_update = forms.DateField()
   
    class Meta:
        model = Ser_per_day
        fields = '__all__'

class Ser_per_month_form(ModelForm):
    ser_101 = forms.CharField(max_length=255)
    ser_102 = forms.CharField(max_length=255)
    ser_103 = forms.CharField(max_length=255)
    ser_104 = forms.CharField(max_length=255)
    ser_105 = forms.CharField(max_length=255)
    ser_106 = forms.CharField(max_length=255)
    ser_107 = forms.CharField(max_length=255)
    ser_108 = forms.CharField(max_length=255)
    ser_109 = forms.CharField(max_length=255)
    ser_110 = forms.CharField(max_length=255)
    ser_111 = forms.CharField(max_length=255)
    ser_112 = forms.CharField(max_length=255)
    ser_113 = forms.CharField(max_length=255)
    ser_114 = forms.CharField(max_length=255)
    ser_115 = forms.CharField(max_length=255)
    ser_116 = forms.CharField(max_length=255)
    ser_117 = forms.CharField(max_length=255)
    ser_118 = forms.CharField(max_length=255)
    ser_119 = forms.CharField(max_length=255)
    ser_120 = forms.CharField(max_length=255) 
    date_update = forms.DateField()
    class Meta:
        model = Ser_per_month
        fields = '__all__'


class Mer_per_month_form(ModelForm):
    mer_1 = forms.CharField(max_length=255)
    mer_2 = forms.CharField(max_length=255)
    mer_3 = forms.CharField(max_length=255)
    mer_4 = forms.CharField(max_length=255)
    mer_5 = forms.CharField(max_length=255)
    mer_6 = forms.CharField(max_length=255)
    mer_7 = forms.CharField(max_length=255)
    mer_8 = forms.CharField(max_length=255)
    mer_9 = forms.CharField(max_length=255)
    mer_10 = forms.CharField(max_length=255)
    mer_11 = forms.CharField(max_length=255)
    mer_12 = forms.CharField(max_length=255)
    mer_13 = forms.CharField(max_length=255)
    mer_14 = forms.CharField(max_length=255)
    mer_15 = forms.CharField(max_length=255)
    mer_16 = forms.CharField(max_length=255)
    mer_17 = forms.CharField(max_length=255)
    mer_18 = forms.CharField(max_length=255)
    mer_19 = forms.CharField(max_length=255)
    mer_20 = forms.CharField(max_length=255)
    mer_21 = forms.CharField(max_length=255)
    mer_22 = forms.CharField(max_length=255)
    mer_23 = forms.CharField(max_length=255)
    mer_24 = forms.CharField(max_length=255)
    mer_25 = forms.CharField(max_length=255)
    mer_26 = forms.CharField(max_length=255)
    mer_27 = forms.CharField(max_length=255)
    mer_28 = forms.CharField(max_length=255)
    mer_29 = forms.CharField(max_length=255)
    mer_30 = forms.CharField(max_length=255)
    mer_31 = forms.CharField(max_length=255)
    mer_32 = forms.CharField(max_length=255)
    # mer_33 = forms.CharField(max_length=255)
    # mer_34 = forms.CharField(max_length=255)
    # mer_35 = forms.CharField(max_length=255)
    # mer_36 = forms.CharField(max_length=255)
    # mer_37 = forms.CharField(max_length=255)
    date_update = forms.DateTimeField()


    class Meta:
        model = Mer_per_month
        fields = '__all__'


class Sen_equip_form(ModelForm):

    r1 = forms.CharField()  
    r2 = forms.CharField()  
    r3 = forms.CharField()  
    r4 = forms.CharField()  
    r5 = forms.CharField()  
    r6 = forms.CharField()  
    r7 = forms.CharField()  
    r8 = forms.CharField()  
    r9 = forms.CharField()  
    r10 = forms.CharField() 
    r11 = forms.CharField() 
    r12 = forms.CharField() 
    dy13 = forms.CharField()
    rt13 = forms.CharField()
    dy14 = forms.CharField()
    rt14 = forms.CharField()
    dy15 = forms.CharField()
    rt15 = forms.CharField()
    dy16 = forms.CharField()
    rt16 = forms.CharField()
    r17 = forms.CharField() 
    r18 = forms.CharField()
    r19 = forms.CharField() 
    # r20 = forms.CharField() 
    # r21 = forms.CharField() 
    r22 = forms.CharField() 
    r23 = forms.CharField() 
    r24 = forms.CharField() 
    r25 = forms.CharField() 
    r26 = forms.CharField() 
    r27 = forms.CharField()
    date_update = forms.DateTimeField()
 

    class Meta:
        model = Sen_equip
        fields = '__all__'
 
