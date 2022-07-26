# Generated by Django 3.2.4 on 2022-07-26 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipatr',
            fields=[
                ('tipatride', models.IntegerField(primary_key=True, serialize=False)),
                ('tipatrnom', models.CharField(max_length=50)),
                ('tipatrideest', models.BooleanField()),
            ],
            options={
                'db_table': 'tipatr',
            },
        ),
        migrations.CreateModel(
            name='Usucab',
            fields=[
                ('ideusu', models.IntegerField(primary_key=True, serialize=False)),
                ('prinomusu', models.CharField(max_length=50)),
                ('segnomusu', models.CharField(max_length=50)),
                ('priapeusu', models.CharField(max_length=50)),
                ('segapeusu', models.CharField(max_length=50)),
                ('sexusu', models.CharField(max_length=1)),
                ('corusu', models.CharField(max_length=50)),
                ('imgusu', models.CharField(max_length=100)),
                ('conusu', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usucab',
            },
        ),
        migrations.CreateModel(
            name='Zontur',
            fields=[
                ('zonturide', models.IntegerField(primary_key=True, serialize=False)),
                ('zonturnom', models.CharField(max_length=50)),
                ('zonturdir', models.CharField(max_length=200)),
                ('zonturpun', models.IntegerField()),
                ('zonturima', models.CharField(max_length=100)),
                ('zonturdes', models.TextField()),
                ('zonturnumvis', models.IntegerField()),
                ('fecpub', models.DateField()),
                ('fecingusu', models.DateField()),
                ('identificador_usuario', models.ForeignKey(blank=True, db_column='identificador_usuario', null=True, on_delete=django.db.models.deletion.CASCADE, to='unsaTur.usucab')),
            ],
            options={
                'db_table': 'zontur',
                'unique_together': {('zonturide', 'identificador_usuario')},
            },
        ),
        migrations.CreateModel(
            name='Zonturhor',
            fields=[
                ('zonturide', models.IntegerField(primary_key=True, serialize=False)),
                ('zonturing', models.TimeField()),
                ('zontursal', models.TimeField()),
                ('zonturdia', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'zonturhor',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('idelis', models.IntegerField(primary_key=True, serialize=False)),
                ('nomlis', models.CharField(max_length=50)),
                ('idezontur', models.CharField(max_length=100)),
                ('ideusu', models.ForeignKey(db_column='ideusu', on_delete=django.db.models.deletion.CASCADE, to='unsaTur.usucab')),
            ],
            options={
                'db_table': 'list',
                'unique_together': {('idelis', 'ideusu')},
            },
        ),
        migrations.CreateModel(
            name='Zonturcom',
            fields=[
                ('comide', models.IntegerField(primary_key=True, serialize=False)),
                ('comcon', models.TextField()),
                ('comnumlik', models.IntegerField()),
                ('atride', models.IntegerField()),
                ('ideusu', models.ForeignKey(db_column='ideusu', on_delete=django.db.models.deletion.CASCADE, to='unsaTur.usucab')),
                ('zonturide', models.ForeignKey(db_column='zonturide', on_delete=django.db.models.deletion.CASCADE, to='unsaTur.zontur')),
            ],
            options={
                'db_table': 'zonturcom',
                'unique_together': {('comide', 'ideusu', 'zonturide', 'atride')},
            },
        ),
        migrations.CreateModel(
            name='Atr',
            fields=[
                ('atride', models.IntegerField(primary_key=True, serialize=False)),
                ('atrnom', models.CharField(max_length=50)),
                ('atrdes', models.TextField()),
                ('tipatride', models.ForeignKey(blank=True, db_column='tipatride', null=True, on_delete=django.db.models.deletion.CASCADE, to='unsaTur.tipatr')),
                ('zonturide', models.ForeignKey(db_column='zonturide', on_delete=django.db.models.deletion.CASCADE, to='unsaTur.zontur')),
            ],
            options={
                'db_table': 'atr',
                'unique_together': {('zonturide', 'atride')},
            },
        ),
        migrations.CreateModel(
            name='ZonturList',
            fields=[
                ('zonturide', models.OneToOneField(db_column='zonturide', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='unsaTur.zontur')),
                ('ideusu', models.IntegerField()),
                ('atride', models.IntegerField()),
                ('idelis', models.ForeignKey(db_column='idelis', on_delete=django.db.models.deletion.CASCADE, to='unsaTur.list')),
            ],
            options={
                'db_table': 'zontur_list',
                'unique_together': {('zonturide', 'idelis', 'ideusu', 'atride')},
            },
        ),
    ]
