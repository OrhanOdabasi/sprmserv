# Generated by Django 2.1.3 on 2018-11-29 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Musteri', '0002_auto_20181128_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saha',
            name='musteri_saha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musteri.Musteri', verbose_name='Müşteri'),
        ),
    ]
