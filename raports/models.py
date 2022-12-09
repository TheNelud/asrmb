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
    date_update = models.DateTimeField()

    class Meta:
        ordering = ['date_update']
        managed = False
        db_table = 'ser_per_day'
