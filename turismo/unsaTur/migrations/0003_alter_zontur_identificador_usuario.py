# Generated by Django 3.2.4 on 2022-07-26 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unsaTur', '0002_alter_zontur_identificador_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zontur',
            name='identificador_usuario',
            field=models.ForeignKey(blank=True, db_column='identificador_usuario', on_delete=django.db.models.deletion.CASCADE, to='unsaTur.usucab'),
        ),
    ]
