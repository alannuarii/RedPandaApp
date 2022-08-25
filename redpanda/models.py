from django.db import models
from datetime import datetime, timedelta


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


# Model Pemeliharaan
class Har(models.Model):
    list_har = (
        ('Standby', 'Standby'),
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3'),
        ('P4', 'P4'),
        ('P5', 'P5'),
        ('TO', 'TO'),
        ('SO', 'SO'),
        ('MO', 'MO'),
        ('PdM', 'PdM'),
        ('CM', 'CM'),
    )
    mesin_id = models.ForeignKey(Mesin, on_delete=models.CASCADE, verbose_name='Nama Mesin')
    tanggal_jumat =  models.DateField('Tanggal Mulai')
    jumat = models.CharField('Jumat', max_length=20, choices=list_har, default='Standby')
    sabtu = models.CharField('Sabtu', max_length=20, choices=list_har, default='Standby')
    minggu = models.CharField('Minggu', max_length=20, choices=list_har, default='Standby')
    senin = models.CharField('Senin', max_length=20, choices=list_har, default='Standby')
    selasa = models.CharField('Selasa', max_length=20, choices=list_har, default='Standby')
    rabu = models.CharField('Rabu', max_length=20, choices=list_har, default='Standby')
    kamis = models.CharField('Kamis', max_length=20, choices=list_har, default='Standby')
    
    def __str__(self):
        return str(self.mesin_id)

    def tglsabtu(self):
        return self.tanggal_jumat + timedelta(days=1)

    def tglminggu(self):
        return self.tanggal_jumat + timedelta(days=2)

    def tglsenin(self):
        return self.tanggal_jumat + timedelta(days=3)
    
    def tglselasa(self):
        return self.tanggal_jumat + timedelta(days=4)

    def tglrabu(self):
        return self.tanggal_jumat + timedelta(days=5)

    def tglkamis(self):
        return self.tanggal_jumat + timedelta(days=6)
