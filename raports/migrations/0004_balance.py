# Generated by Django 3.2.16 on 2022-12-10 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raports', '0003_sen_equip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('par_a', models.FloatField()),
                ('par_b', models.FloatField()),
                ('par_c', models.FloatField()),
                ('par_d', models.FloatField()),
                ('par_e', models.FloatField()),
                ('par_f', models.FloatField()),
                ('par_g', models.FloatField()),
                ('par_h', models.FloatField()),
                ('par_i', models.FloatField()),
                ('par_j', models.FloatField()),
                ('par_k', models.FloatField()),
                ('par_l', models.FloatField()),
                ('par_m', models.FloatField()),
                ('par_n', models.FloatField()),
                ('par_o', models.FloatField()),
                ('par_p', models.FloatField()),
                ('par_q', models.FloatField()),
                ('par_r', models.FloatField()),
                ('par_s', models.FloatField()),
                ('par_t', models.FloatField()),
                ('par_u', models.FloatField()),
                ('par_v', models.FloatField()),
                ('par_w', models.FloatField()),
                ('par_x', models.FloatField()),
                ('par_aa', models.FloatField()),
                ('par_bb', models.FloatField()),
                ('par_cc', models.FloatField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'balance',
                'ordering': ['update_time'],
                'managed': False,
            },
        ),
    ]
