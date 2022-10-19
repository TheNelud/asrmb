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
