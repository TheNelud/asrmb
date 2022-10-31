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

class TeclossesTreeForm(ModelForm):
    class Meta:
        model = TeclossesTree
        fields = '__all__'
#________________________________________________________________________________
class RecyclingcalcOneForm(ModelForm):
    class Meta:
        model = RecyclingcalcOne
        fields = '__all__'

class RecyclingcalcTwoForm(ModelForm):
    class Meta:
        model = RecyclingcalcTwo
        fields = '__all__'

class RecyclingcalcThreeForm(ModelForm):
    class Meta:
        model = RecyclingcalcThree
        fields = '__all__'

class RecyclingcalcFourForm(ModelForm):
    class Meta:
        model = RecyclingcalcFour
        fields = '__all__'

class RecyclingcalcFive1Form(ModelForm):
    class Meta:
        model = RecyclingcalcFive1
        fields = '__all__'

class RecyclingcalcFive2Form(ModelForm):
    class Meta:
        model = RecyclingcalcFive2
        fields = '__all__'

class RecyclingcalcSixForm(ModelForm):
    class Meta:
        model = RecyclingcalcSix
        fields = '__all__'

#________________________________________________________________________________

class CondensateprodOneForm(ModelForm):
    class Meta:
        model = CondensateprodOne
        fields = '__all__'

class CondensateprodTwoForm(ModelForm):
    class Meta:
        model = CondensateprodTwo
        fields = '__all__'

class CondensateprodThree1Form(ModelForm):
    class Meta:
        model = CondensateprodThree1
        fields = '__all__'

class CondensateprodThree2Form(ModelForm):
    class Meta:
        model = CondensateprodThree2
        fields = '__all__'

#__________________________________________________________________________________

class CondrecyclingOneForm(ModelForm):
    class Meta:
        model = CondrecyclingOne
        fields = '__all__'

class CondrecyclingTwoForm(ModelForm):
    class Meta:
        model = CondrecyclingTwo
        fields = '__all__'

class CondrecyclingThreeForm(ModelForm):
    class Meta:
        model = CondrecyclingThree
        fields = '__all__'


class CondrecyclingFourForm(ModelForm):
    class Meta:
        model = CondrecyclingFour
        fields = '__all__'

class CondrecyclingFiveForm(ModelForm):
    class Meta:
        model = CondrecyclingFive
        fields = '__all__'

class CondrecyclingSixForm(ModelForm):
    class Meta:
        model = CondrecyclingSix
        fields = '__all__'

class CondrecyclingSevenForm(ModelForm):
    class Meta:
        model = CondrecyclingSeven
        fields = '__all__'

class CondrecyclingEightForm(ModelForm):
    class Meta:
        model = CondrecyclingEight
        fields = '__all__'


class CondrecyclingNineForm(ModelForm):
    class Meta:
        model = CondrecyclingNine
        fields = '__all__'

class CondrecyclingTenForm(ModelForm):
    class Meta:
        model = CondrecyclingTen
        fields = '__all__'

