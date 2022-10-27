from django.forms import ModelForm
from .models import *

class P1ComponentCompositionOfUnstableCondensateForm(ModelForm):
    class Meta:
        model = P1ComponentCompositionOfUnstableCondensate
        fields = '__all__'
