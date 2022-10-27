from django.db import models


# For Schema "coefficients" ------------------------------------------------------------------------------------------>
class Coef(models.Model):
    id = models.SmallAutoField(primary_key=True)
    temperature = models.CharField(max_length=255)
    less_20 = models.FloatField()
    t_20_52 = models.FloatField()
    t_53_84 = models.FloatField()
    t_85_112 = models.FloatField()
    t_113_138 = models.FloatField()
    t_139_162 = models.FloatField()
    t_163_185 = models.FloatField()
    t_186_206 = models.FloatField()
    t_207_226 = models.FloatField()
    t_227_244 = models.FloatField()
    t_245_262 = models.FloatField()
    t_263_278 = models.FloatField()
    t_279_294 = models.FloatField()
    t_295_310 = models.FloatField()
    t_311_324 = models.FloatField()
    t_325_350 = models.FloatField()
    more_than_350 = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = True
        db_table = 'coef'


class Losses(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name_of_device = models.CharField(max_length=255)
    gas_gasoline = models.FloatField()
    kerosene_diesel = models.FloatField()
    oil_masut = models.FloatField()

    class Meta:
        managed = False
        db_table = 'losses'


class MolMass(models.Model):
    id = models.SmallAutoField(primary_key=True)
    t_10_43 = models.FloatField()
    m_50_70 = models.FloatField()
    t_44_77 = models.FloatField()
    m_71_91 = models.FloatField()
    t_78_132 = models.FloatField()
    m_92_118 = models.FloatField()
    t_134_200 = models.FloatField()
    m_119_159 = models.FloatField()
    t_202_350 = models.FloatField()
    m_160_290 = models.FloatField()
    t_355_500 = models.FloatField()
    m_285_510 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mol_mass'


# For SHCEMA  public ------------------------------------------------------------------------------------------------->
class P1ComponentCompositionOfUnstableCondensate(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p1_component_composition_of_unstable_condensate'


class P2ComponentCompositionOfGas(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p2_component_composition_of_gas'


class P3DeterminationOfTheComponentOfGas(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p3_determination_of_the_component_of_gas'


class P4GasCompositionToTheProtocol(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    content_of_the_component = models.FloatField()
    proportion_of_the_component = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p4_gas_composition_to_the_protocol'


class P5DeterminationOfTheComponentComposition(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p5_determination_of_the_component_composition'


class P6CompositionOfGasOutput(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p6_composition_of_gas_output'


class P7CompositionOfGas10c(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p7_composition_of_gas_10c'


class P8CompositionOfTheCondensate(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cylinder_1506 = models.FloatField()
    cylinder_1641 = models.FloatField()
    average_value = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p8_composition_of_the_condensate'


class P9ComponentOfTheSeparationGas(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p9_component_of_the_separation_gas'


class P10ProtokolKGN(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    соmposition = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    chromatograph_mass = models.FloatField()
    proportion = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p10_protocol_kgn'


class AllTableCal(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sum_first = models.FloatField()
    sum_second = models.FloatField()
    xg_prod = models.FloatField()
    xk_prod = models.FloatField()
    c5_sum = models.FloatField()
    calc_density = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'all_table_cal'


class DenProtokol(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    num = models.FloatField()
    comment = models.CharField(max_length=255)
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'den_protocol'


class P2SumTable(models.Model):
    id = models.SmallAutoField(primary_key=True)
    c6plus = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p2_sum_table'


class P4SumTable(models.Model):
    id = models.SmallAutoField(primary_key=True)
    c6plus = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p4_sum_table'


class P6SumTable(models.Model):
    id = models.SmallAutoField(primary_key=True)
    c6plus = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p6_sum_table'


class P10Calc(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.FloatField()
    calculation = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p10_calc'


# For schema codensatecalc ------------------------------------------------------------------------------------------->
# 1. Технологические потери газового конденсата по итогам опорожнения технологического оборудования и трубопроводов перед проведением ремонтных работ, т. (п. 5.2)';
class CondensateprodOne(models.Model):
    id = models.SmallAutoField(primary_key=True)
    data = models.DateField()
    type = models.CharField(max_length=255)
    v_op = models.FloatField()
    mk_ic5 = models.FloatField()
    xkprod_ic5 = models.FloatField()
    mk_nc5 = models.FloatField()
    xkprod_nc5 = models.FloatField()
    mk_c6 = models.FloatField()
    xkprod_c6 = models.FloatField()
    vk_st_y = models.FloatField()
    pk_op = models.FloatField()
    application = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condensateprod_one'


# 3. Технологические потери газового конденсата при уносе с жидкостью, м3 (п. 5.4)
# Утилизация рефлюксной воды на КОС с УРМЭГ за отчетный период по счетчикам насоса 30Н-1'
class CondensateprodThree1(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    device = models.CharField(max_length=255)
    month = models.FloatField()
    day = models.FloatField()
    hour = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condensateprod_three1'


# 3. Технологические потери газового конденсата при уносе с жидкостью, м3 (п. 5.4)'

class CondensateprodThree2(models.Model):
    id = models.SmallAutoField(primary_key=True)
    type = models.CharField(max_length=255)
    q_sh = models.FloatField()
    gk = models.FloatField()
    tau = models.FloatField()
    p_opk = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condensateprod_three2'


# '2. Технологические потери газового конденсата при отборе проб, т (п. 5.3)'
class CondensateprodTwo(models.Model):
    id = models.SmallAutoField(primary_key=True)
    trial = models.CharField(max_length=255)
    v_pr = models.FloatField()
    p = models.FloatField()
    n = models.FloatField()
    b_pr = models.FloatField()
    xk_prod = models.FloatField()
    p_opk = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condensateprod_two'


# 8. Потери газового конденсата при ремонте трубопроводов, т (п.6.5.3)
class CondrecyclingEight(models.Model):
    id = models.SmallAutoField(primary_key=True)
    region = models.CharField(max_length=255)
    pt_p = models.FloatField()
    mp = models.FloatField()
    r = models.FloatField()
    tr_p = models.FloatField()
    pnj = models.FloatField()
    v_ychij = models.FloatField()
    pr_z_ij = models.FloatField()
    v_ych_ij = models.FloatField()
    pkj = models.FloatField()
    days = models.FloatField()
    pr_op_ij = models.FloatField()
    np_t_ij = models.FloatField()
    pyp = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condrecycling_eight'


# 5. Потери газового конденсата через неплотности соединений и уплотнений ЗРА, т (п.6.4.3)
class CondrecyclingFive(models.Model):
    id = models.SmallAutoField(primary_key=True)
    type = models.CharField(max_length=255)
    a_ij = models.FloatField()
    b_ij = models.FloatField()
    tau_ij = models.FloatField()
    aa_ij = models.FloatField()
    p_yp = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condrecycling_five'


# 4. Потери газового конденсата при отборе проб для аналитического контроля, т(п.6.3)
class CondrecyclingFour(models.Model):
    id = models.SmallAutoField(primary_key=True)
    test = models.CharField(max_length=255)
    v_pr = models.FloatField()
    p = models.FloatField()
    n = models.FloatField()
    b_pn = models.FloatField()
    p_opk = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condrecycling_four'


# 9. Потери газового конденсата при остановке объектов на планово-предупредительный ремонт, т (п.6.6.1)
class CondrecyclingNine(models.Model):
    id = models.SmallAutoField(primary_key=True)
    device = models.CharField(max_length=255)
    gm_o = models.FloatField()
    nt = models.FloatField()
    nk = models.FloatField()
    pr_a = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condrecycling_nine'


# Расчет потерь при Переработке**
# 1. Потери газового конденсата со сточными водами товарного парка, т (п.6.1.3.2)'
class CondrecyclingOne(models.Model):
    id = models.SmallAutoField(primary_key=True)
    test = models.CharField(max_length=255)
    gr_o = models.FloatField()
    nst_v = models.FloatField()
    tau = models.FloatField()
    vs_p = models.FloatField()
    ss_p = models.FloatField()
    ps_p = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condrecycling_one'


# 7. Потери газового конденсата через неплотности соединений теплообменной аппаратуры на расчетный период, т (п.6.4.7)
class CondrecyclingSeven(models.Model):
    id = models.SmallAutoField(primary_key=True)
    heat_con = models.CharField(max_length=255)
    p_ed = models.FloatField()
    nt_o = models.FloatField()
    tau_p = models.FloatField()
    p_t_o = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condrecycling_seven'


# 3. Потери газового конденсата от испарения при хранении в резервуарах от "больших дыханий", т (п.6.2.4)
class CondrecyclingThree(models.Model):
    id = models.SmallAutoField(primary_key=True)
    date_begin = models.DateField()
    date_end = models.DateField()
    batch_num = models.CharField(max_length=255)
    pg_p = models.FloatField()
    mp = models.FloatField()
    r = models.FloatField()
    tg_p = models.FloatField()
    ppj = models.FloatField()
    v_o = models.FloatField()
    v_pol = models.FloatField()
    n = models.FloatField()
    kf = models.FloatField()
    v = models.FloatField()
    py_s = models.FloatField()
    pa = models.FloatField()
    pb_d = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condrecycling_three'


# 2. Потери газового конденсата от испарения при хранении в резервуарах от "малых дыханий", т (п.6.2.3)
class CondrecyclingTwo(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    batch_num = models.CharField(max_length=255)
    hr = models.FloatField()
    ppj = models.FloatField()
    py_s = models.FloatField()
    d = models.FloatField()
    kn = models.FloatField()
    ko = models.FloatField()
    p = models.FloatField()
    tau = models.FloatField()
    tau_g = models.FloatField()
    pm_d = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condrecycling_two'


class CondrecyclingTwoDop(models.Model):
    id = models.SmallAutoField(primary_key=True)
    max_first = models.FloatField()
    level_first = models.FloatField()
    hr = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condrecycling_two_dop'


class CondrecyclingTwoDop2(models.Model):
    id = models.SmallAutoField(primary_key=True)
    max_first = models.FloatField()
    level_first = models.FloatField()
    hr = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'condrecycling_two_dop2'


# -------------------------------------------------------------------------------------------------------------------->
# For schema gascalc

# 5. Потери природного газа при опорожнении технологического оборудования перед проведением ремонтных работ на расчетный период Qоп, м3. (п.5.2.3)
# Участок от УИТ ГС до точки его смешения ГГПиГС, подлежит учету в составе технологических потерь ГС при переработке'
class RecyclingcalcFive1(models.Model):
    id = models.SmallAutoField(primary_key=True)
    date = models.DateField()
    device = models.CharField(max_length=255)
    v = models.FloatField()
    pn = models.FloatField()
    tn = models.FloatField()
    zn = models.FloatField()
    press_pk = models.FloatField()
    tk = models.FloatField()
    zk = models.FloatField()
    n = models.FloatField()
    pb_d = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'recyclingcalc_five1'


# '5. Потери природного газа при опорожнении технологического оборудования перед проведением ремонтных работ на расчетный период Qоп, м3. (п.5.2.3)
# Данный вид технологических потерь образовался на участке от УИХ КГН до УКУ ГКС и подлежит учету в составе технологических потерь КГН при переработке (п.9 настоящего расчета потерь КГН при переработке)*';

class RecyclingcalcFive2(models.Model):
    id = models.SmallAutoField(primary_key=True)
    date = models.DateField()
    device = models.CharField(max_length=255)
    v = models.FloatField()
    pn = models.FloatField()
    tn = models.FloatField()
    zn = models.FloatField()
    press_pk = models.FloatField()
    tk = models.FloatField()
    zk = models.FloatField()
    n = models.FloatField()
    pb_d = models.FloatField()
    p_act = models.FloatField()
    m = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'recyclingcalc_five2'


# '4. Потери природного газа при проведении индивидуальных испытаний оборудования Qисп, в случае сброса требующегося для испытания природного газа на факел или на свеч м3. (п.5.3.4)';

class RecyclingcalcFour(models.Model):
    id = models.SmallAutoField(primary_key=True)
    test = models.CharField(max_length=255)
    v_isp = models.FloatField()
    tau_isp = models.FloatField()
    q_isp = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'recyclingcalc_four'


# 'Расчет потерь при Переработке**
# 1. Потери природного газа через неплотности соединений и уплотнений ЗРА, м3. (п.5.1.3)';

class RecyclingcalcOne(models.Model):
    id = models.SmallAutoField(primary_key=True)
    type = models.CharField(max_length=255)
    aij = models.FloatField()
    bij = models.FloatField()
    tauij = models.FloatField()
    a_ij = models.FloatField()
    mi = models.FloatField()
    q_yp = models.FloatField()
    t_type = models.CharField(max_length=255)
    t_aij = models.FloatField()
    t_bij = models.FloatField()
    t_tauij = models.FloatField()
    t_a_ij = models.FloatField()
    t_mi = models.FloatField()
    t_q_yp = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'recyclingcalc_one'


class RecyclingcalcSix(models.Model):
    id = models.SmallAutoField(primary_key=True)
    device = models.CharField(max_length=255)
    v = models.FloatField()
    p = models.FloatField()
    t = models.FloatField()
    z = models.FloatField()
    b = models.FloatField()
    nv = models.FloatField()
    q_op = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'recyclingcalc_six'


# '3. Потери природного газа на технологическом объекте при отборе проб для аналитического контроля Qан, м3. (п.5.3.2)';

class RecyclingcalcThree(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    vp_o_i = models.FloatField()
    pp_o_i = models.FloatField()
    tp_o_i = models.FloatField()
    zp_o_i = models.FloatField()
    bi = models.FloatField()
    nan_i = models.FloatField()
    qo_p_i = models.FloatField()
    device = models.CharField(max_length=255)
    vp_p_i = models.FloatField()
    tau_p_i = models.FloatField()
    qpot_i = models.FloatField()
    qyp = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'recyclingcalc_three'


# Часы работы (нахождения под давлением) за месяц, час';

class RecyclingcalcTime(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    timing = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'recyclingcalc_time'


# 2. Потери природного газа через неплотности соединений теплообменной апаратуры на расчетный период, м3. (п.5.1.3)
class RecyclingcalcTwo(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    m_p = models.FloatField()
    p_p = models.FloatField()
    q_ed = models.FloatField()
    nt_o = models.FloatField()
    tau_p = models.FloatField()
    p_t_o = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'recyclingcalc_two'


# значения с распечатки показаний технологических расходомеров
# показания счетчиков 30Р-1
# для таблицы teclosses two'

class Teclosses2dop(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    data = models.DateField()
    num_one = models.FloatField()
    num_two = models.FloatField()
    difference = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'teclosses_2dop'


# '1. Технологические потери природного газа по итогам опорожнения технологического оборудования и трубопроводов перед проведением ремонтных работ, м3 (п.4.2.)';
class TeclossesOne(models.Model):
    id = models.SmallAutoField(primary_key=True)
    data = models.DateField()
    name = models.CharField(max_length=255)
    v = models.FloatField()
    pn = models.FloatField()
    tn = models.FloatField()
    zn = models.FloatField()
    press_pk = models.FloatField()
    tk = models.FloatField()
    zk = models.FloatField()
    v_op = models.FloatField()
    ng_prod = models.FloatField()
    ng_nl = models.FloatField()
    xg_prod = models.FloatField()
    n = models.FloatField()
    pn_op = models.FloatField()
    mol = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'teclosses_one'


# Расчет технологических потерь при Добыче*
# 3. Технологические потери природного газа при отборе проб, м3 (п. 4.5)';

class TeclossesTree(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    v_pr = models.FloatField()
    p_pr = models.FloatField()
    t_pr = models.FloatField()
    z_pr = models.FloatField()
    b = models.FloatField()
    ni = models.FloatField()
    xr_prod = models.FloatField()
    pr_op = models.FloatField()
    device = models.CharField(max_length=255)
    v_p = models.FloatField()
    tau = models.FloatField()
    xrr_prod = models.FloatField()
    n = models.FloatField()
    pr_pot = models.FloatField()
    pr_pr = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'teclosses_three'


# 'Приложения № 2,3,4,7
# Необходимо для расчета xrr_prod';
class TeclossesTreeDop(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nr_prod = models.FloatField()
    nr_pl = models.FloatField()
    xr_prod = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'teclosses_three_dop'


# 'Расчет технологических потерь при Добыче*
# 2. Технологические потери природного газа при регенерации технических жидкостей (МЭГа), м3 (п. 4.3.2)';

class TeclossesTwo(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    qgr_sh = models.FloatField()
    ng_prod = models.FloatField()
    ng_pl = models.FloatField()
    xg_prod = models.FloatField()
    pgr_sh = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'teclosses_two'


# -------------------------------------------------------------________________________________________________---------->
# for schema compress ---->

class CoefPTM(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    p = models.FloatField()
    t = models.FloatField()
    m = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'coef_p_t_m'


class P2Calc(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    d_e = models.FloatField()
    molar = models.FloatField()
    p = models.FloatField()
    t = models.FloatField()
    m = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p2_calc'


class P3Calc(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    d_e = models.FloatField()
    molar = models.FloatField()
    p = models.FloatField()
    t = models.FloatField()
    m = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p3_calc'


class P4Calc(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    d_e = models.FloatField()
    molar = models.FloatField()
    p = models.FloatField()
    t = models.FloatField()
    m = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p4_calc'


class P5Calc(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    d_e = models.FloatField()
    molar = models.FloatField()
    p = models.FloatField()
    t = models.FloatField()
    m = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p5_calc'


class P6Calc(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    d_e = models.FloatField()
    molar = models.FloatField()
    p = models.FloatField()
    t = models.FloatField()
    m = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p6_calc'


class P7Calc(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    d_e = models.FloatField()
    molar = models.FloatField()
    p = models.FloatField()
    t = models.FloatField()
    m = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p7_calc'


class TabCoefAll(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    pressure = models.FloatField()
    temperature = models.FloatField()
    p_pl = models.FloatField()
    t_pl = models.FloatField()
    p_kr = models.FloatField()
    t_kr = models.FloatField()
    p_pl_sm = models.FloatField()
    p_pr = models.FloatField()
    t_pr = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'tab_coef_all'


class TabSumAll(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sum_d_e = models.FloatField()
    sum_mol = models.FloatField()
    sum_p = models.FloatField()
    sum_t = models.FloatField()
    sum_m = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'tab_sum_all'


class TotalCalc(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    scalc_one = models.FloatField()
    calc_two = models.FloatField()
    calc_threе = models.FloatField()
    calc_four = models.FloatField()
    zn = models.FloatField()

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'total_calc'
