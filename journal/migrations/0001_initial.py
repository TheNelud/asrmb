# Generated by Django 3.2.16 on 2022-10-31 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Losses',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name_of_device', models.CharField(max_length=255)),
                ('gas_gasoline', models.FloatField()),
                ('kerosene_diesel', models.FloatField()),
                ('oil_masut', models.FloatField()),
            ],
            options={
                'db_table': 'losses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MolMass',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('t_10_43', models.FloatField()),
                ('m_50_70', models.FloatField()),
                ('t_44_77', models.FloatField()),
                ('m_71_91', models.FloatField()),
                ('t_78_132', models.FloatField()),
                ('m_92_118', models.FloatField()),
                ('t_134_200', models.FloatField()),
                ('m_119_159', models.FloatField()),
                ('t_202_350', models.FloatField()),
                ('m_160_290', models.FloatField()),
                ('t_355_500', models.FloatField()),
                ('m_285_510', models.FloatField()),
            ],
            options={
                'db_table': 'mol_mass',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Coef',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('temperature', models.CharField(max_length=255)),
                ('less_20', models.FloatField()),
                ('t_20_52', models.FloatField()),
                ('t_53_84', models.FloatField()),
                ('t_85_112', models.FloatField()),
                ('t_113_138', models.FloatField()),
                ('t_139_162', models.FloatField()),
                ('t_163_185', models.FloatField()),
                ('t_186_206', models.FloatField()),
                ('t_207_226', models.FloatField()),
                ('t_227_244', models.FloatField()),
                ('t_245_262', models.FloatField()),
                ('t_263_278', models.FloatField()),
                ('t_279_294', models.FloatField()),
                ('t_295_310', models.FloatField()),
                ('t_311_324', models.FloatField()),
                ('t_325_350', models.FloatField()),
                ('more_than_350', models.FloatField()),
            ],
            options={
                'db_table': 'coef',
                'ordering': ['id'],
                'managed': True,
            },
        ),
    ]
