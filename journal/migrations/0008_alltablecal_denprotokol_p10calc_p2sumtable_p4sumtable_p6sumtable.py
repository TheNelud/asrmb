# Generated by Django 3.2.16 on 2022-10-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_coefptm_p2calc_p3calc_p4calc_p5calc_p6calc_p7calc_recyclingcalcfive1_recyclingcalcfive2_recyclingcal'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllTableCal',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('sum_first', models.FloatField()),
                ('sum_second', models.FloatField()),
                ('xg_prod', models.FloatField()),
                ('xk_prod', models.FloatField()),
                ('c5_sum', models.FloatField()),
                ('calc_density', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'all_table_cal',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DenProtokol',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('num', models.FloatField()),
                ('comment', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'den_protocol',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P10Calc',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.FloatField()),
                ('calculation', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p10_calc',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P2SumTable',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('c6plus', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p2_sum_table',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P4SumTable',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('c6plus', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p4_sum_table',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P6SumTable',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('c6plus', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p6_sum_table',
                'ordering': ['id'],
                'managed': False,
            },
        ),
    ]
