# Generated by Django 2.1.3 on 2018-11-28 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Talep', '0002_auto_20181123_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talep',
            name='akiskan_kontrol',
            field=models.BooleanField(default=False, verbose_name='Sistem içinde akışkan var mı?'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='betonlama',
            field=models.BooleanField(default=False, verbose_name='Pompa kaidesi betonla (grout) sabitlendi mi?'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='enerji_kontrol',
            field=models.BooleanField(default=False, verbose_name='Sistem enerji ve bağlantıları hazır mı?'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='is_sagligi',
            field=models.BooleanField(default=False, verbose_name='İş Sağlığı ve güvenliği çerçevesinde gerekli önlemler alındı mı?'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='on_hazirlik',
            field=models.BooleanField(default=False, verbose_name='Pompa(lar) ile beraber gönderilen bakım kitapçığı okundu mu?'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='personel',
            field=models.BooleanField(default=False, verbose_name='Yardımcı teknik personel var mı?'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='pompa_hazir',
            field=models.BooleanField(default=False, verbose_name='Pompa(lar) çalışmaya hazır mı?'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='sizdirmazlik',
            field=models.BooleanField(default=False, verbose_name='Tesisatın sızdırmazlık testi yapıldı mı?'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='talep_pompa_adi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PompaModel.PompaModel', verbose_name='Pompa'),
        ),
    ]