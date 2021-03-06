# Generated by Django 2.1.3 on 2018-11-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PompaModel', '0002_auto_20181121_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pompamodel',
            name='pompa',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='Pompa Modeli'),
        ),
        migrations.AlterField(
            model_name='pompamodel',
            name='pompa_aciklama',
            field=models.TextField(max_length=160, null=True, verbose_name='Pompa Açıklaması'),
        ),
        migrations.AlterField(
            model_name='pompamodel',
            name='pompa_bi_kitapcigi',
            field=models.FileField(blank=True, null=True, upload_to='Bakim_İsletme/', verbose_name='Bakım İşletme Kitapçığı'),
        ),
        migrations.AlterField(
            model_name='pompamodel',
            name='pompa_patlamis',
            field=models.FileField(blank=True, null=True, upload_to='Patlamis/', verbose_name='Patlamış Resim'),
        ),
        migrations.AlterField(
            model_name='pompamodel',
            name='pompa_resim',
            field=models.ImageField(null=True, upload_to='Pompa_Resimleri/', verbose_name='Pompa Resmi'),
        ),
        migrations.AlterField(
            model_name='pompamodel',
            name='pompa_tip_kitapcigi',
            field=models.FileField(blank=True, null=True, upload_to='Tip/', verbose_name='Tip Kitapçığı'),
        ),
    ]
