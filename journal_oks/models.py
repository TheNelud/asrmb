from django.db import models

# Create your models here.

# For SHCEMA  public ------------------------------------------------------------------------------------------------->
class P1ComponentCompositionOfUnstableCondensate(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    time = models.DateField(null=True)

    # def __str__(self):
    #     return self.name

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
    def __str__(self):
        return self.name
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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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