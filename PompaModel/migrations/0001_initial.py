# Generated by Django 2.1.3 on 2018-11-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PompaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pompa', models.CharField(max_length=20, verbose_name='Pompa Modeli')),
                ('pompa_aciklama', models.TextField(max_length=160, verbose_name='Pompa Açıklaması')),
            ],
            options={
                'verbose_name': 'Pompa Modeli',
                'verbose_name_plural': 'Pompa Modelleri',
            },
        ),
    ]
