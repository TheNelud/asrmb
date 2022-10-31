from django.db import models


# Create your models here.

class P5_app(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p5_app'


class P6_app(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'p6_app'


class Perehod_stabilizacii(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    perehod_per = models.FloatField()
    perehod_t = models.FloatField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'perehod_stabilizacii'


class Data_gas_stabilization(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    v = models.FloatField()
    m = models.FloatField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'data_gas_stabilization'


class Const(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value= models.FloatField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'const'
