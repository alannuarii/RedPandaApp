# Generated by Django 4.0.7 on 2022-08-14 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feeder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(verbose_name='Tanggal')),
                ('jam', models.CharField(max_length=5, verbose_name='Jam')),
                ('kota', models.IntegerField(default=0, verbose_name='Kota')),
                ('tona', models.IntegerField(default=0, verbose_name='Tona')),
                ('kolongan', models.IntegerField(default=0, verbose_name='Kolongan')),
                ('lesabe', models.IntegerField(default=0, verbose_name='Lesabe')),
                ('tamako', models.IntegerField(default=0, verbose_name='Tamako')),
                ('mainlinepetta', models.IntegerField(default=0, verbose_name='Main Line Petta')),
                ('pettakota', models.IntegerField(default=0, verbose_name='Petta Kota')),
                ('mainlinetahuna', models.IntegerField(default=0, verbose_name='Main Line Tahuna')),
                ('kendahe', models.IntegerField(default=0, verbose_name='Kendahe')),
                ('bowongkulu', models.IntegerField(default=0, verbose_name='Bowongkulu')),
                ('kotatamako', models.IntegerField(default=0, verbose_name='Kota Tamako')),
                ('lapango', models.IntegerField(default=0, verbose_name='Lapango')),
                ('tahuna', models.IntegerField(default=0, verbose_name='Tahuna')),
                ('salurang', models.IntegerField(default=0, verbose_name='Salurang')),
                ('pintareng', models.IntegerField(default=0, verbose_name='Pintareng')),
                ('tahunaincome', models.IntegerField(default=0, verbose_name='Tahuna Income')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_unit', models.CharField(max_length=30, verbose_name='Nama Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Mesin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=3, verbose_name='Unit')),
                ('nama_mesin', models.CharField(max_length=30, verbose_name='Nama Mesin')),
                ('daya_mampu', models.IntegerField(verbose_name='Daya Mampu (kW)')),
                ('is_sewa', models.BooleanField(verbose_name='Sewa')),
                ('nama_unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redpanda.unit', verbose_name='Nama Unit')),
            ],
        ),
    ]
