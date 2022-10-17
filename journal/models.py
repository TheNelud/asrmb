from django.db import models



# For Schema "coefficients" ------->
class Coef(models.Model):
    id = models.SmallAutoField(primary_key=True)
    temperature = models.CharField(max_length=255)
    less_20 = models.FloatField()
    _20_52 = models.FloatField()
    _53_84 = models.FloatField()
    _85_112 = models.FloatField()
    _113_138 = models.FloatField()
    _139_162 = models.FloatField()
    _163_185 = models.FloatField()
    _186_206 = models.FloatField()
    _207_226 = models.FloatField()
    _227_244 = models.FloatField()
    _245_262 = models.FloatField()
    _263_278 = models.FloatField()
    _279_294 = models.FloatField()
    _295_310 = models.FloatField()
    _311_324 = models.FloatField()
    _325_350 = models.FloatField()
    more_than_350 = models.FloatField()

    class Meta:
        managed = False
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
