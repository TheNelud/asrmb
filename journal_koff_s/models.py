from django.db import models

# Create your models here.

# for schema compress ---->

class CoefPTM(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    p = models.FloatField()
    t = models.FloatField()
    m = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return self.name

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
    time = models.DateTimeField()

    def __str__(self):
        return self.name

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
    time = models.DateTimeField()

    def __str__(self):
        return self.name

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
    time = models.DateTimeField()

    def __str__(self):
        return self.name

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
    time = models.DateTimeField()

    def __str__(self):
        return self.name

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
    time = models.DateTimeField()

    def __str__(self):
        return self.name

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
    time = models.DateTimeField()

    def __str__(self):
        return self.name

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
    time = models.DateTimeField()

    def __str__(self):
        return self.name

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
    time = models.DateTimeField()

    def __str__(self):
        return self.name

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
    time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'total_calc'

