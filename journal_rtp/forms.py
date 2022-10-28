from django.forms import ModelForm
from .models import *

class TeclossesOneForm(ModelForm):
    class Meta:
        model = TeclossesOne
        fields = '__all__'

class TeclossesTwoForm(ModelForm):
    class Meta:
        model = TeclossesTwo
        fields = '__all__'