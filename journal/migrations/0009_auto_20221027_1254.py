# Generated by Django 3.2.16 on 2022-10-27 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0008_alltablecal_denprotokol_p10calc_p2sumtable_p4sumtable_p6sumtable'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AllTableCal',
        ),
        migrations.DeleteModel(
            name='DenProtokol',
        ),
        migrations.DeleteModel(
            name='P10Calc',
        ),
        migrations.DeleteModel(
            name='P10ProtokolKGN',
        ),
        migrations.DeleteModel(
            name='P1ComponentCompositionOfUnstableCondensate',
        ),
        migrations.DeleteModel(
            name='P2ComponentCompositionOfGas',
        ),
        migrations.DeleteModel(
            name='P2SumTable',
        ),
        migrations.DeleteModel(
            name='P3DeterminationOfTheComponentOfGas',
        ),
        migrations.DeleteModel(
            name='P4GasCompositionToTheProtocol',
        ),
        migrations.DeleteModel(
            name='P4SumTable',
        ),
        migrations.DeleteModel(
            name='P5DeterminationOfTheComponentComposition',
        ),
        migrations.DeleteModel(
            name='P6CompositionOfGasOutput',
        ),
        migrations.DeleteModel(
            name='P6SumTable',
        ),
        migrations.DeleteModel(
            name='P7CompositionOfGas10c',
        ),
        migrations.DeleteModel(
            name='P8CompositionOfTheCondensate',
        ),
        migrations.DeleteModel(
            name='P9ComponentOfTheSeparationGas',
        ),
    ]
