# Generated by Django 2.1.3 on 2018-11-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Talep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talep',
            name='talep_no',
            field=models.CharField(blank=True, max_length=6, verbose_name='Talep No'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='talep_pompa_tipi',
            field=models.CharField(max_length=20, null=True, verbose_name='Pompa Tipi'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='yetkili_onayi',
            field=models.BooleanField(default=False),
        ),
    ]
