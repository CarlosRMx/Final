# Generated by Django 2.0.13 on 2019-11-10 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nino', '0011_nna_oficial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nna',
            name='oficial',
            field=models.CharField(blank=True, choices=[('fr', '1ro'), ('sd', '2do'), ('tr', '3ro'), ('fr', '4to'), ('N', 'Ninguno')], default=True, max_length=4, verbose_name='Oficial'),
        ),
    ]
