# Generated by Django 2.1.3 on 2018-11-29 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Arac', '0008_auto_20181129_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arackullanim',
            name='arac_saha_dest',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Musteri.Saha', verbose_name='Aracın Gittiği Saha'),
        ),
    ]
