# Generated by Django 2.0.13 on 2019-11-10 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nino', '0021_nna_otro_dato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nna',
            name='otro_dato',
            field=models.TextField(default='...'),
        ),
    ]
