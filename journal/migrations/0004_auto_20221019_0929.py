# Generated by Django 3.2.16 on 2022-10-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_p10protokolkgn_p1componentcopositionofunstablecondensate_p2componentcopositionofgas_p3determinationo'),
    ]

    operations = [
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
            ],
            options={
                'db_table': 'p2_component_composition_of_gas',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='P1ComponentCopositionOfUnstableCondensate',
        ),
        migrations.DeleteModel(
            name='P2ComponentCopositionOfGas',
        ),
    ]