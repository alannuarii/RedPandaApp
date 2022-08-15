from django.db import models


# Model Unit
class Unit(models.Model):
    nama_unit = models.CharField('Nama Unit', max_length=30)

    def __str__(self):
        return self.nama_unit


# Model Mesin 
class Mesin(models.Model):
    nama_unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='Nama Unit')
    unit = models.CharField('Unit', max_length=3)
    nama_mesin = models.CharField('Nama Mesin', max_length=30)
    daya_mampu = models.IntegerField('Daya Mampu (kW)')
    is_sewa = models.BooleanField('Sewa')

    def __str__(self):
        return '{} Unit {} ({})'.format(self.nama_unit_id, self.unit, self.nama_mesin)


# Model Feeder 
class Feeder(models.Model):
    tanggal = models.DateField('Tanggal')
    jam = models.CharField('Jam', max_length=5)
    kota = models.IntegerField('Kota', default=0)
    tona = models.IntegerField('Tona', default=0)
    kolongan = models.IntegerField('Kolongan', default=0)
    lesabe = models.IntegerField('Lesabe', default=0)
    tamako = models.IntegerField('Tamako', default=0)
    mainlinepetta = models.IntegerField('Main Line Petta', default=0)
    pettakota = models.IntegerField('Petta Kota', default=0)
    mainlinetahuna = models.IntegerField('Main Line Tahuna', default=0)
    kendahe = models.IntegerField('Kendahe', default=0)
    bowongkulu = models.IntegerField('Bowongkulu', default=0)
    kotatamako = models.IntegerField('Kota Tamako', default=0)
    lapango = models.IntegerField('Lapango', default=0)
    tahuna = models.IntegerField('Tahuna', default=0)
    salurang = models.IntegerField('Salurang', default=0)
    pintareng = models.IntegerField('Pintareng', default=0)
    tahunaincome = models.IntegerField('Tahuna Income', default=0)

    def __str__(self):
        return '{}'.format(self.tanggal)