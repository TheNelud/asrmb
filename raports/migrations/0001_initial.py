# Generated by Django 3.2.16 on 2022-12-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ser_per_day',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('ser_1', models.FloatField()),
                ('ser_2', models.FloatField()),
                ('ser_3', models.FloatField()),
                ('ser_4', models.FloatField()),
                ('ser_5', models.FloatField()),
                ('ser_6', models.FloatField()),
                ('ser_7', models.FloatField()),
                ('ser_8', models.FloatField()),
                ('ser_9', models.FloatField()),
                ('ser_11', models.FloatField()),
                ('ser_12', models.FloatField()),
                ('ser_13', models.FloatField()),
                ('ser_14', models.FloatField()),
                ('ser_15', models.FloatField()),
                ('ser_16', models.FloatField()),
                ('ser_17', models.FloatField()),
                ('ser_18', models.FloatField()),
                ('ser_19', models.FloatField()),
                ('ser_20', models.FloatField()),
                ('date_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'ser_per_day',
                'ordering': ['date_update'],
                'managed': False,
            },
        ),
    ]
