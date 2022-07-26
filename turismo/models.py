from django.db import models


class Atr(models.Model):
    atride = models.IntegerField(primary_key=True)
    atrnom = models.CharField(max_length=50)
    atrdes = models.TextField()
    tipatride = models.ForeignKey('Tipatr', models.DO_NOTHING, db_column='tipatride', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atr'


class List(models.Model):
    idelis = models.IntegerField(primary_key=True)
    nomlis = models.CharField(max_length=50)
    idezontur = models.CharField(max_length=100)
    ideusu = models.ForeignKey('Usucab', models.DO_NOTHING, db_column='ideusu')

    class Meta:
        managed = False
        db_table = 'list'
        unique_together = (('idelis', 'ideusu'),)


class Tipatr(models.Model):
    tipatride = models.IntegerField(primary_key=True)
    tipatrnom = models.CharField(max_length=50)
    tipatrideest = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tipatr'


class Usucab(models.Model):
    ideusu = models.IntegerField(primary_key=True)
    prinomusu = models.CharField(max_length=50)
    segnomusu = models.CharField(max_length=50)
    priapeusu = models.CharField(max_length=50)
    segapeusu = models.CharField(max_length=50)
    sexusu = models.CharField(max_length=1)
    corusu = models.CharField(max_length=50)
    imgusu = models.CharField(max_length=100)
    conusu = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'usucab'


class Zontur(models.Model):
    zonturide = models.OneToOneField('Zonturhor', models.DO_NOTHING, db_column='zonturide', primary_key=True)
    zonturnom = models.CharField(max_length=50)
    zonturdir = models.CharField(max_length=200)
    zonturpun = models.IntegerField()
    zonturima = models.CharField(max_length=100)
    zonturdes = models.TextField()
    zonturnumvis = models.IntegerField()
    fecpub = models.DateField()
    fecingusu = models.DateField()
    atride = models.ForeignKey(Atr, models.DO_NOTHING, db_column='atride')
    identificador_usuario = models.ForeignKey(Usucab, models.DO_NOTHING, db_column='identificador_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zontur'
        unique_together = (('zonturide', 'atride'),)


class ZonturList(models.Model):
    zonturide = models.OneToOneField(Zontur, models.DO_NOTHING, db_column='zonturide', primary_key=True)
    idelis = models.ForeignKey(List, models.DO_NOTHING, db_column='idelis')
    ideusu = models.IntegerField()
    atride = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zontur_list'
        unique_together = (('zonturide', 'idelis', 'ideusu', 'atride'),)


class Zonturcom(models.Model):
    comide = models.IntegerField(primary_key=True)
    comcon = models.TextField()
    comnumlik = models.IntegerField()
    ideusu = models.ForeignKey(Usucab, models.DO_NOTHING, db_column='ideusu')
    zonturide = models.ForeignKey(Zontur, models.DO_NOTHING, db_column='zonturide')
    atride = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zonturcom'
        unique_together = (('comide', 'ideusu', 'zonturide', 'atride'),)


class Zonturhor(models.Model):
    zonturide = models.IntegerField(primary_key=True)
    zonturing = models.TimeField()
    zontursal = models.TimeField()
    zonturdia = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'zonturhor'
