from django.db import models

# Create your models here.
class Ser_per_day(models.Model):
    id = models.SmallAutoField(primary_key=True)
    ser_1 = models.FloatField()
    ser_2 = models.FloatField()
    ser_3 = models.FloatField()
    ser_4 = models.FloatField()
    ser_5 = models.FloatField()
    ser_6 = models.FloatField()
    ser_7 = models.FloatField()
    ser_8 = models.FloatField()
    ser_9 = models.FloatField()
    ser_10 = models.FloatField()
    ser_11 = models.FloatField()
    ser_12 = models.FloatField()
    ser_13 = models.FloatField()
    ser_14 = models.FloatField()
    ser_15 = models.FloatField()
    ser_16 = models.FloatField()
    ser_17 = models.FloatField()
    ser_18 = models.FloatField()
    ser_19 = models.FloatField()
    ser_20 = models.FloatField()
    date_update = models.DateField()


    class Meta:
        # ordering = ['-date_update']
        managed = False
        db_table = 'ser_per_day'

class Ser_per_month(models.Model):
    id = models.SmallAutoField(primary_key=True)
    ser_101 = models.FloatField()
    ser_102 = models.FloatField()
    ser_103 = models.FloatField()
    ser_104 = models.FloatField()
    ser_105 = models.FloatField()
    ser_106 = models.FloatField()
    ser_107 = models.FloatField()
    ser_108 = models.FloatField()
    ser_109 = models.FloatField()
    ser_110 = models.FloatField()
    ser_111 = models.FloatField()
    ser_112 = models.FloatField()
    ser_113 = models.FloatField()
    ser_114 = models.FloatField()
    ser_115 = models.FloatField()
    ser_116 = models.FloatField()
    ser_117 = models.FloatField()
    ser_118 = models.FloatField()
    ser_119 = models.FloatField()
    ser_120 = models.FloatField()
    date_update = models.DateTimeField()


    class Meta:
        ordering = ['date_update']
        managed = False
        db_table = 'ser_per_month'

        
class Mer_per_month(models.Model):
    id = models.SmallAutoField(primary_key=True)
    mer_1 = models.FloatField()
    mer_2 = models.FloatField()
    mer_3 = models.FloatField()
    mer_4 = models.FloatField()
    mer_5 = models.FloatField()
    mer_6 = models.FloatField()
    mer_7 = models.FloatField()
    mer_8 = models.FloatField()
    mer_9 = models.FloatField()
    mer_10 = models.FloatField()
    mer_11 = models.FloatField()
    mer_12 = models.FloatField()
    mer_13 = models.FloatField()
    mer_14 = models.FloatField()
    mer_15 = models.FloatField()
    mer_16 = models.FloatField()
    mer_17 = models.FloatField()
    mer_18 = models.FloatField()
    mer_19 = models.FloatField()
    mer_20 = models.FloatField()
    mer_21 = models.FloatField()
    mer_22 = models.FloatField()
    mer_23 = models.FloatField()
    mer_24 = models.FloatField()
    mer_25 = models.FloatField()
    mer_26 = models.FloatField()
    mer_27 = models.FloatField()
    mer_28 = models.FloatField()
    mer_29 = models.FloatField()
    mer_30 = models.FloatField()
    mer_31 = models.FloatField()
    mer_32 = models.FloatField()
    mer_33 = models.FloatField()
    mer_34 = models.FloatField()
    mer_35 = models.FloatField()
    mer_36 = models.FloatField()
    mer_37 = models.FloatField()
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
    r20 = models.FloatField() 
    r21 = models.FloatField() 
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
    par_g = models.FloatField()

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