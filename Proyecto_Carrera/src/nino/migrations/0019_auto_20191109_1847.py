# Generated by Django 2.0.13 on 2019-11-10 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nino', '0018_auto_20191109_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nna',
            name='fecha_resolucion',
            field=models.CharField(default='...', max_length=30, verbose_name='Fecha de resolución'),
        ),
    ]
