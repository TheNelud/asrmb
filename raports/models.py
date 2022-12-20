from django.db import models

# Create your models here.
class Ser_per_day(models.Model):
    id = models.SmallAutoField(primary_key=True)
    ser_1 = models.CharField(max_length=255)
    ser_2 = models.CharField(max_length=255)
    ser_3 = models.CharField(max_length=255)
    ser_4 = models.CharField(max_length=255)
    ser_5 = models.CharField(max_length=255)
    ser_6 = models.CharField(max_length=255)
    ser_7 = models.CharField(max_length=255)
    ser_8 = models.CharField(max_length=255)
    ser_9 = models.CharField(max_length=255)
    ser_10 = models.CharField(max_length=255)
    ser_11 = models.CharField(max_length=255)
    ser_12 = models.CharField(max_length=255)
    ser_13 = models.CharField(max_length=255)
    ser_14 = models.CharField(max_length=255)
    ser_15 = models.CharField(max_length=255)
    ser_16 = models.CharField(max_length=255)
    ser_17 = models.CharField(max_length=255)
    ser_18 = models.CharField(max_length=255)
    ser_19 = models.CharField(max_length=255)
    ser_20 = models.CharField(max_length=255) 
    date_update = models.DateField()


    class Meta:
        # ordering = ['-date_update']
        managed = False
        db_table = 'ser_per_day'

class Ser_per_month(models.Model):
    id = models.SmallAutoField(primary_key=True)
    ser_101 = models.CharField(max_length=255)
    ser_102 = models.CharField(max_length=255)
    ser_103 = models.CharField(max_length=255)
    ser_104 = models.CharField(max_length=255)
    ser_105 = models.CharField(max_length=255)
    ser_106 = models.CharField(max_length=255)
    ser_107 = models.CharField(max_length=255)
    ser_108 = models.CharField(max_length=255)
    ser_109 = models.CharField(max_length=255)
    ser_110 = models.CharField(max_length=255)
    ser_111 = models.CharField(max_length=255)
    ser_112 = models.CharField(max_length=255)
    ser_113 = models.CharField(max_length=255)
    ser_114 = models.CharField(max_length=255)
    ser_115 = models.CharField(max_length=255)
    ser_116 = models.CharField(max_length=255)
    ser_117 = models.CharField(max_length=255)
    ser_118 = models.CharField(max_length=255)
    ser_119 = models.CharField(max_length=255)
    ser_120 = models.CharField(max_length=255)
    date_update = models.DateTimeField()


    class Meta:
        ordering = ['date_update']
        managed = False
        db_table = 'ser_per_month'

        
class Mer_per_month(models.Model):
    id = models.SmallAutoField(primary_key=True)
    mer_1 = models.CharField(max_length=255)
    mer_2 = models.CharField(max_length=255)
    mer_3 = models.CharField(max_length=255)
    mer_4 = models.CharField(max_length=255)
    mer_5 = models.CharField(max_length=255)
    mer_6 = models.CharField(max_length=255)
    mer_7 = models.CharField(max_length=255)
    mer_8 = models.CharField(max_length=255)
    mer_9 = models.CharField(max_length=255)
    mer_10 = models.CharField(max_length=255)
    mer_11 = models.CharField(max_length=255)
    mer_12 = models.CharField(max_length=255)
    mer_13 = models.CharField(max_length=255)
    mer_14 = models.CharField(max_length=255)
    mer_15 = models.CharField(max_length=255)
    mer_16 = models.CharField(max_length=255)
    mer_17 = models.CharField(max_length=255)
    mer_18 = models.CharField(max_length=255)
    mer_19 = models.CharField(max_length=255)
    mer_20 = models.CharField(max_length=255)
    mer_21 = models.CharField(max_length=255)
    mer_22 = models.CharField(max_length=255)
    mer_23 = models.CharField(max_length=255)
    mer_24 = models.CharField(max_length=255)
    mer_25 = models.CharField(max_length=255)
    mer_26 = models.CharField(max_length=255)
    mer_27 = models.CharField(max_length=255)
    mer_28 = models.CharField(max_length=255)
    mer_29 = models.CharField(max_length=255)
    mer_30 = models.CharField(max_length=255)
    mer_31 = models.CharField(max_length=255)
    mer_32 = models.CharField(max_length=255)
    # mer_33 = models.CharField(max_length=255)
    # mer_34 = models.CharField(max_length=255)
    # mer_35 = models.CharField(max_length=255)
    # mer_36 = models.CharField(max_length=255)
    # mer_37 = models.CharField(max_length=255)
    date_update = models.DateTimeField()


    class Meta:
        ordering = ['date_update']
        managed = False
        db_table = 'mer_per_month'


class Sen_equip(models.Model):
    id = models.SmallAutoField(primary_key=True) 
    r1 = models.FloatField()  
    r2 = models.FloatField()  
    r3 = models.FloatField()  
    r4 = models.FloatField()  
    r5 = models.FloatField()  
    r6 = models.FloatField()  
    r7 = models.FloatField()  
    r8 = models.FloatField()  
    r9 = models.FloatField()  
    r10 = models.FloatField() 
    r11 = models.FloatField() 
    r12 = models.FloatField() 
    dy13 = models.FloatField()
    rt13 = models.FloatField()
    dy14 = models.FloatField()
    rt14 = models.FloatField()
    dy15 = models.FloatField()
    rt15 = models.FloatField()
    dy16 = models.FloatField()
    rt16 = models.FloatField()
    r17 = models.FloatField() 
    r18 = models.FloatField()
    r19 = models.FloatField() 
    # r20 = models.FloatField() 
    # r21 = models.FloatField() 
    r22 = models.FloatField() 
    r23 = models.FloatField() 
    r24 = models.FloatField() 
    r25 = models.FloatField() 
    r26 = models.FloatField() 
    r27 = models.FloatField()
    date_update = models.DateTimeField()
 

    class Meta:
        ordering = ['date_update']
        managed = False
        db_table = 'sen_equip'

class Balance(models.Model):
    id = models.SmallAutoField(primary_key=True) 
    par_a = models.FloatField()   
    par_b = models.FloatField()      
    par_c = models.FloatField()      
    par_d = models.FloatField()      
    par_e = models.FloatField()      
    par_f = models.FloatField()      
    
    par_g_nmag = models.FloatField()
    par_g_rmag_30i_1 = models.FloatField()
    par_g_rmag_60e_1 = models.FloatField()

    par_h = models.FloatField()      
    par_i = models.FloatField()      
    par_j = models.FloatField()      
    par_k = models.FloatField()      
    par_l = models.FloatField()      
    par_m = models.FloatField()      
    par_n = models.FloatField()      
    par_o = models.FloatField()      
    par_p = models.FloatField()
          
    par_q = models.FloatField()      
    par_r = models.FloatField()      
    par_s = models.FloatField()      
    par_t = models.FloatField()      
    par_u = models.FloatField()      
    par_v = models.FloatField()      
    par_w = models.FloatField()      
    par_x = models.FloatField()      
    par_aa = models.FloatField()     
    par_bb = models.FloatField()     
    par_cc = models.FloatField()     
    date_update = models.DateTimeField()

    class Meta:
        ordering = ['date_update']
        managed = False
        db_table = 'balance'