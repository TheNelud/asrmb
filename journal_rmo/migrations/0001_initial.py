# Generated by Django 3.2.16 on 2022-10-31 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Const',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('value', models.FloatField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'const',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Data_gas_stabilization',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('v', models.FloatField()),
                ('m', models.FloatField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'data_gas_stabilization',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P5_app',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('molar_components', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('total_molar_mass', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('calculated_mass', models.FloatField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p5_app',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P6_app',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('molar_components', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('total_molar_mass', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('calculated_mass', models.FloatField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p6_app',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perehod_stabilizacii',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('perehod_per', models.FloatField()),
                ('perehod_t', models.FloatField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'Perehod_stabilizacii',
                'ordering': ['id'],
                'managed': False,
            },
        ),
    ]
