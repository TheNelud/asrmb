from django.forms import ModelForm
from .models import *

class CoefPTMForm(ModelForm):
    class Meta:
        model = CoefPTM
        fields = '__all__'

class P2CalcForm(ModelForm):
    class Meta:
        model = P2Calc
        fields = '__all__'

class P3CalcForm(ModelForm):
    class Meta:
        model = P3Calc
        fields = '__all__'

class P4CalcForm(ModelForm):
    class Meta:
        model = P4Calc
        fields = '__all__'

class P5CalcForm(ModelForm):
    class Meta:
        model = P5Calc
        fields = '__all__'

class P6CalcForm(ModelForm):
    class Meta:
        model = P6Calc
        fields = '__all__'

class P7CalcForm(ModelForm):
    class Meta:
        model = P7Calc
        fields = '__all__'

class TabCoefAllForm(ModelForm):
    class Meta:
        model = TabCoefAll
        fields = '__all__'

class TabSumAllForm(ModelForm):
    class Meta:
        model = TabSumAll
        fields = '__all__'

class TotalCalcForm(ModelForm):
    class Meta:
        model = TotalCalc
        fields = '__all__'