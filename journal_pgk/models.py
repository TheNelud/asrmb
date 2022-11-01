from django.db import models


# Create your models here.

class Calc_losses(models.Model):
    id = models.SmallAutoField(primary_key=True)
    device = models.CharField(max_length=255)
    p_ap_avg = models.FloatField()
    k_d_avg = models.FloatField()
    pa_sh_sum = models.FloatField()
    time = models.DateTimeField()


    def __str__(self):
        return self.device

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'calc_losses'



class Losses_gas_apparatus(models.Model):
    id = models.SmallAutoField(primary_key=True)
    date = models.DateField()
    device = models.CharField(max_length=255)
    p_ap = models.FloatField()
    t_ap = models.FloatField()
    v_ap = models.FloatField()
    tay_ap = models.FloatField()
    k_d = models.FloatField()
    n_ap = models.FloatField()
    pa_sh = models.FloatField()
    time = models.DateTimeField()


    def __str__(self):
        return self.device

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'losses_gas_apparatus'