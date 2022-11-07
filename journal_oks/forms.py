from django.forms import ModelForm
from .models import *
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget
from django.contrib.admin import widgets
# from django.forms.fields import DateTimeField


# for schema public -------------------------------------------------------------------------->
class P1ComponentCompositionOfUnstableCondensateForm(ModelForm):
    # time = DateTimeField(widget=AdminDateWidget)
    class Meta:
        model = P1ComponentCompositionOfUnstableCondensate
        fields = '__all__'
        widgets = {
            "time" :  AdminDateWidget()
        }

class P2ComponentCompositionOfGasForm(ModelForm):
    class Meta:
        model = P2ComponentCompositionOfGas
        fields = '__all__'

class P3DeterminationOfTheComponentOfGasForm(ModelForm):
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