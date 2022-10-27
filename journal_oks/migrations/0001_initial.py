# Generated by Django 3.2.16 on 2022-10-27 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='P10ProtokolKGN',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('соmposition', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('proportion', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p10_protocol_kgn',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P1ComponentCompositionOfUnstableCondensate',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('molar_components', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('total_molar_mass', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('calculated_mass', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p1_component_composition_of_unstable_condensate',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P2ComponentCompositionOfGas',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('molar_components', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('total_molar_mass', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('calculated_mass', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p2_component_composition_of_gas',
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
            name='P3DeterminationOfTheComponentOfGas',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('molar_components', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('total_molar_mass', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('calculated_mass', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p3_determination_of_the_component_of_gas',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P4GasCompositionToTheProtocol',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('molar_components', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('total_molar_mass', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('calculated_mass', models.FloatField()),
                ('content_of_the_component', models.FloatField()),
                ('proportion_of_the_component', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p4_gas_composition_to_the_protocol',
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
            name='P5DeterminationOfTheComponentComposition',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('molar_components', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('total_molar_mass', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('calculated_mass', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p5_determination_of_the_component_composition',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P6CompositionOfGasOutput',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('molar_components', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('total_molar_mass', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('calculated_mass', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p6_composition_of_gas_output',
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
        migrations.CreateModel(
            name='P7CompositionOfGas10c',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('molar_components', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('total_molar_mass', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('calculated_mass', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p7_composition_of_gas_10c',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P8CompositionOfTheCondensate',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cylinder_1506', models.FloatField()),
                ('cylinder_1641', models.FloatField()),
                ('average_value', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p8_composition_of_the_condensate',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='P9ComponentOfTheSeparationGas',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('molar_components', models.FloatField()),
                ('molar_mass_of_the_component', models.FloatField()),
                ('total_molar_mass', models.FloatField()),
                ('chromatograph_mass', models.FloatField()),
                ('calculated_mass', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'p9_component_of_the_separation_gas',
                'ordering': ['id'],
                'managed': False,
            },
        ),
    ]
