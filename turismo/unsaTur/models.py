from django.db import models

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
        db_table = 'usucab'



class Zontur(models.Model):
    zonturide = models.IntegerField(primary_key=True)
    zonturnom = models.CharField(max_length=50)
    zonturdir = models.CharField(max_length=200)
    zonturpun = models.IntegerField()
    zonturima = models.CharField(max_length=100)
    zonturdes = models.TextField()
    zonturnumvis = models.IntegerField()
    fecpub = models.DateField()
    fecingusu = models.DateField()
    identificador_usuario = models.ForeignKey(Usucab, on_delete=models.CASCADE, db_column='identificador_usuario')

    class Meta:
        db_table = 'zontur'
        unique_together = (('zonturide', 'identificador_usuario'),)


class Atr(models.Model):
    zonturide = models.ForeignKey(Zontur ,on_delete=models.CASCADE, db_column='zonturide')
    atride = models.IntegerField(primary_key=True)
    atrnom = models.CharField(max_length=50)
    atrdes = models.TextField()
    tipatride = models.ForeignKey('Tipatr',on_delete=models.CASCADE, db_column='tipatride', blank=True, null=True)

    class Meta:
        db_table = 'atr'
        unique_together = (('zonturide', 'atride'),)


class List(models.Model):
    idelis = models.IntegerField(primary_key=True)
    nomlis = models.CharField(max_length=50)
    idezontur = models.CharField(max_length=100)
    ideusu = models.ForeignKey('Usucab', on_delete=models.CASCADE, db_column='ideusu')

    class Meta:
        db_table = 'list'
        unique_together = (('idelis', 'ideusu'),)


class Tipatr(models.Model):
    tipatride = models.IntegerField(primary_key=True)
    tipatrnom = models.CharField(max_length=50)
    tipatrideest = models.BooleanField()

    class Meta:
        db_table = 'tipatr'



class ZonturList(models.Model):
    zonturide = models.OneToOneField(Zontur, on_delete=models.CASCADE, db_column='zonturide', primary_key=True)
    idelis = models.ForeignKey(List, on_delete=models.CASCADE, db_column='idelis')
    ideusu = models.IntegerField()
    atride = models.IntegerField()

    class Meta:
        db_table = 'zontur_list'
        unique_together = (('zonturide', 'idelis', 'ideusu', 'atride'),)

class Zonturcom(models.Model):
    comide = models.IntegerField(primary_key=True)
    comcon = models.TextField()
    comnumlik = models.IntegerField()
    ideusu = models.ForeignKey(Usucab,on_delete=models.CASCADE, db_column='ideusu')
    zonturide = models.ForeignKey(Zontur,on_delete=models.CASCADE, db_column='zonturide')
    atride = models.IntegerField()

    class Meta:
        db_table = 'zonturcom'
        unique_together = (('comide', 'ideusu', 'zonturide', 'atride'),)

class Zonturhor(models.Model):
    zonturide = models.IntegerField(primary_key=True)
    zonturing = models.TimeField()
    zontursal = models.TimeField()
    zonturdia = models.CharField(max_length=50)

    class Meta:
        db_table = 'zonturhor'