# Generated by Django 2.1.3 on 2018-11-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arac', '0005_auto_20181128_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='arac',
            name='arac_ego_tarih',
            field=models.DateField(blank=True, null=True, verbose_name='Araç Ego Tarihi'),
        ),
    ]
