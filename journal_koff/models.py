from django.db import models

# Create your models here.


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


