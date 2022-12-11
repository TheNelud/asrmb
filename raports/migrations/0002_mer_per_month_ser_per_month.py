# Generated by Django 3.2.16 on 2022-12-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mer_per_month',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('mer_1', models.FloatField()),
                ('mer_2', models.FloatField()),
                ('mer_3', models.FloatField()),
                ('mer_4', models.FloatField()),
                ('mer_5', models.FloatField()),
                ('mer_6', models.FloatField()),
                ('mer_7', models.FloatField()),
                ('mer_8', models.FloatField()),
                ('mer_9', models.FloatField()),
                ('mer_10', models.FloatField()),
                ('mer_11', models.FloatField()),
                ('mer_12', models.FloatField()),
                ('mer_13', models.FloatField()),
                ('mer_14', models.FloatField()),
                ('mer_15', models.FloatField()),
                ('mer_16', models.FloatField()),
                ('mer_17', models.FloatField()),
                ('mer_18', models.FloatField()),
                ('mer_19', models.FloatField()),
                ('mer_20', models.FloatField()),
                ('mer_21', models.FloatField()),
                ('mer_22', models.FloatField()),
                ('mer_23', models.FloatField()),
                ('mer_24', models.FloatField()),
                ('mer_25', models.FloatField()),
                ('mer_26', models.FloatField()),
                ('mer_27', models.FloatField()),
                ('mer_28', models.FloatField()),
                ('mer_29', models.FloatField()),
                ('mer_30', models.FloatField()),
                ('mer_31', models.FloatField()),
                ('mer_32', models.FloatField()),
                ('mer_33', models.FloatField()),
                ('mer_34', models.FloatField()),
                ('mer_35', models.FloatField()),
                ('mer_36', models.FloatField()),
                ('mer_37', models.FloatField()),
                ('date_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'mer_per_month',
                'ordering': ['date_update'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ser_per_month',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('ser_101', models.FloatField()),
                ('ser_102', models.FloatField()),
                ('ser_103', models.FloatField()),
                ('ser_104', models.FloatField()),
                ('ser_105', models.FloatField()),
                ('ser_106', models.FloatField()),
                ('ser_107', models.FloatField()),
                ('ser_108', models.FloatField()),
                ('ser_109', models.FloatField()),
                ('ser_110', models.FloatField()),
                ('ser_111', models.FloatField()),
                ('ser_112', models.FloatField()),
                ('ser_113', models.FloatField()),
                ('ser_114', models.FloatField()),
                ('ser_115', models.FloatField()),
                ('ser_116', models.FloatField()),
                ('ser_117', models.FloatField()),
                ('ser_118', models.FloatField()),
                ('ser_119', models.FloatField()),
                ('ser_120', models.FloatField()),
                ('date_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'ser_per_month',
                'ordering': ['date_update'],
                'managed': False,
            },
        ),
    ]
