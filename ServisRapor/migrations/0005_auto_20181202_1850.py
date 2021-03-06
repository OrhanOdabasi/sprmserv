# Generated by Django 2.1.3 on 2018-12-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServisRapor', '0004_auto_20181202_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='servisrapor',
            name='servis_donus_tarih',
            field=models.DateTimeField(null=True, verbose_name='Servis Donüş Tarihi'),
        ),
        migrations.AddField(
            model_name='servisrapor',
            name='servis_gidis_tarih',
            field=models.DateTimeField(null=True, verbose_name='Servis Gidiş Tarihi'),
        ),
        migrations.AlterField(
            model_name='servisrapor',
            name='servis_suresi',
            field=models.DurationField(blank=True, null=True, verbose_name='Servis Süresi'),
        ),
    ]
