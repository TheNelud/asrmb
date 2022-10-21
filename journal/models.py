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

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p10_protocol_kgn'


# For schema codensatecalc ------------------------------------------------------------------------------------------->
# 1. Технологические потери газового конденсата по итогам опорожнения технологического оборудования и трубопроводов перед проведением ремонтных работ, т. (п. 5.2)';
class CondensateprodOne(models.Model):
    id = models.SmallAutoField(primary_key=True)
    date = models.DateField()
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
