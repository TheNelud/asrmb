from django.forms import ModelForm
from .models import *
from django import forms

class TeclossesOneForm(ModelForm):
    name = forms.CharField(label="Оборудование", max_length=255)
    v = forms.FloatField(label="V - геометрический объем аппарата")
    pn = forms.FloatField(label="Рн - абсолютное давление природного газа перед началом ремонтной работы")
    tn = forms.FloatField(label="Тн - температура природного газа перед началом работы")
    zn = forms.FloatField(label="Zн - коэффициенты сверхсжимаемости природного газа")
    press_pk = forms.FloatField(label="Рк - абсолютное давление природного газа после опорожнения")
    tk = forms.FloatField(label="Тк - температура природного газа после опорожнения")
    zk = forms.FloatField(label="Zк - коэффициенты сверхсжимаемости природного газа")
    # v_op = models.FloatField()
    # ng_prod = models.FloatField()
    ng_nl = forms.FloatField(label="nг.пл - соответственно число молей в газе")
    # xg_prod = models.FloatField()
    n = forms.FloatField(label="N - количество операций в расчетный период")
    # pn_op = forms.FloatField(label="соответственно число молей в газе")
    mol = forms.FloatField(label="Мольная доля С1-С4")
    class Meta:
        model = TeclossesOne
        # fields = '__all__'
        fields = ['name','v','pn','tn','zn','press_pk','tk','zk','ng_nl','n','mol']

class TeclossesTwoForm(ModelForm):
    name = forms.CharField(label="Оборудование", max_length=255)
    qgr_sh = forms.FloatField(label="Qг.р.ж. - расход природного газа при регенерации технических жидкостей")
    ng_prod = forms.FloatField(label="nг.пл - соответственно число молей в газе")
    ng_pl = forms.FloatField(label='nг.прод - соответственно число молей в газе')
    # xg_prod = forms.FloatField(label='Xг.прод - мольная доля добываемой продукции в газе')
    # pgr_sh = forms.FloatField(label="Пг.р.ж. - потери природного газа при регенерации технических жидкостей")
    class Meta:
        model = TeclossesTwo
        fields = ['name', 'qgr_sh', 'ng_prod', 'ng_pl']

class TeclossesTreeForm(ModelForm):
    name = forms.CharField(label="Вид анализа", max_length=255)
    v_pr = forms.FloatField(label="Vпр - геометрический объем пробоотборника для анализа i-го вида")
    p_pr = forms.FloatField(label="Рпр - давление в пробоотборнике для анализа i-го вида")
    t_pr = forms.FloatField(label="Tпр - температура в пробоотборнике для анализа i-го вида")
    z_pr = forms.FloatField(label="Zпр - коэффициент сжимаемости газа")
    b = forms.FloatField(label="b -кратность продувки, т.е. отношение объема (при условии отбора) газа,")
    ni = forms.FloatField(label="ni")
    xr_prod = forms.FloatField(label="Xг.прод - мольная доля добываемой продукции в газе")
    # pr_op = forms.FloatField(label="Пг.оп - потери природного газа при периодическом отборе проб для разовых")
    device = forms.CharField(label="Приборы",max_length=255)
    # v_p = forms.FloatField(label="Vр.- расход газа на i-й прибор")
    tau = forms.FloatField(label="τр - время работы i-го прибора в расчетный период")
    xrr_prod = forms.FloatField(label="Xг.прод - мольная доля добываемой продукции в газе")
    n = forms.FloatField(label="n - число видов анализов")
    # pr_pot = forms.FloatField(label="Пг.пот.i - потери природного газа при работе i-го прибора на потоке")
    # pr_pr = forms.FloatField(label="Пг.пр - соответственно число молей пластового газа и газа")
    class Meta:
        model = TeclossesTree
        fields = ['name','v_pr','p_pr','t_pr','z_pr','b','ni','xr_prod','device','tau','xrr_prod','n']
#________________________________________________________________________________
class RecyclingcalcOneForm(ModelForm):
    type = forms.CharField(label="Тип", max_length=255)
    aij = forms.FloatField(label="Аij - величина j-ого потока через одно уплотнение")
    bij = forms.FloatField(label="bij - количество уплотнений i-го типа на j-м потоке газа")
    tauij = forms.FloatField(label="τij - время работы уплотнений i-го типа на j-м потоке газа в расчетный период")
    a_ij = forms.FloatField(label="аij - расчетная доля уплотнений i-го типа на j-м потоке газа в расчетный период")
    mi = forms.FloatField(label="Mj - молярная масса газа в j-м потоке")
    # q_yp = forms.FloatField(label="")
    t_type = forms.CharField(label="Тип", max_length=255)
    t_aij = forms.FloatField(label="Аij - величина j-ого потока через одно уплотнение")
    t_bij = forms.FloatField(label="bij - количество уплотнений i-го типа на j-м потоке газа")
    t_tauij = forms.FloatField(label="τij - время работы уплотнений i-го типа на j-м потоке газа в расчетный период")
    t_a_ij = forms.FloatField(label="аij - расчетная доля уплотнений i-го типа на j-м потоке газа в расчетный период")
    t_mi = forms.FloatField(label="Mj - молярная масса газа в j-м потоке")
    t_q_yp = forms.FloatField(label="")
    class Meta:
        model = RecyclingcalcOne
        fields = ['type','aij','bij','tauij','a_ij', 'mi']

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

