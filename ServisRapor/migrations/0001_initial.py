# Generated by Django 2.1.3 on 2018-11-28 06:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PompaModel', '0004_auto_20181128_0659'),
        ('Musteri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pompa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servis_pompa_tip', models.CharField(max_length=20, null=True, verbose_name='Pompa Tipi')),
                ('servis_pompa_serino', models.CharField(max_length=20, verbose_name='Pompa Seri No')),
                ('servis_pompa_debi_birim', models.CharField(blank=True, choices=[('msa', 'm3/sa'), ('lsn', 'lt/sn'), ('tsa', 't/sa'), ('ksa', 'kg/sn')], max_length=3, null=True, verbose_name='Debi Birimi')),
                ('servis_pompa_debi', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True, verbose_name='Pompa Debisi')),
                ('servis_pompa_yukseklik', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True, verbose_name='Basma Yüksekliği [mSS]')),
                ('servis_pompa_fan_capi', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Fan Çapı')),
                ('servis_pompa_verim', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Verim')),
                ('servis_pompa_devir', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)], verbose_name='Devir [RPM]')),
                ('servis_pompa_guc', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Pompa Gücü')),
                ('servis_pompa_giris_b', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Giriş Basıncı [bar]')),
                ('servis_pompa_cikis_b', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Çıkış Basıncı [bar]')),
                ('servis_pompa_uretim_yıl', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1871), django.core.validators.MaxValueValidator(2023)], verbose_name='Pompa Üretim Yılı')),
                ('servis_pompa_akiskan', models.CharField(blank=True, max_length=15, null=True, verbose_name='Akışkan')),
                ('servis_pompa_akiskan_sicaklık', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-50), django.core.validators.MaxValueValidator(400)], verbose_name='Akışkan Sıcaklığı (C)')),
                ('servis_pompa_titresim', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Pompa Titreşimi [mm/sn2]')),
                ('servis_pompa_gerilim', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Pompa Gerilimi [V]')),
                ('servis_pompa_akim', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)], verbose_name='Pompa Akımı [I]')),
                ('servis_pompa_kaplin_tipi', models.CharField(blank=True, max_length=5, null=True, verbose_name='Kaplin Tipi')),
                ('servis_pompa_durkalk', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Dur-Kalk Sayısı')),
                ('servis_motor_tipi', models.CharField(blank=True, max_length=25, null=True, verbose_name='Motor Tipi')),
                ('servis_motor_serino', models.CharField(blank=True, max_length=25, null=True, verbose_name='Motor Seri No')),
                ('servis_motor_gerilim', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Motor Gerilimi [V]')),
                ('servis_motor_akim', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)], verbose_name='Motor Akımı [I]')),
                ('servis_motor_guc_birim', models.CharField(blank=True, choices=[('kw', 'kW'), ('mw', 'MW'), ('hp', 'HP')], max_length=2, null=True, verbose_name='Motor Güç Birimi')),
                ('servis_motor_guc', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Motor Gücü')),
                ('servis_motor_cosphi', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)], verbose_name='Motor CosPhi')),
                ('servis_motor_devir', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)], verbose_name='Devir [RPM]')),
                ('servis_motor_uretim_yil', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1871), django.core.validators.MaxValueValidator(2023)], verbose_name='Motor Üretim Yılı')),
                ('servis_pompa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PompaModel.PompaModel')),
            ],
            options={
                'verbose_name': 'Pompa',
                'verbose_name_plural': 'Pompalar',
            },
        ),
        migrations.CreateModel(
            name='ServisRapor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servis_grubu', models.CharField(choices=[('10', 'Merkez Servis')], max_length=2, verbose_name='Servis Grubu')),
                ('servis_rapor_no', models.CharField(max_length=13, verbose_name='Rapor No')),
                ('servis_turu', models.CharField(choices=[('BK', 'Bakım'), ('DA', 'Devreye Alma'), ('KG', 'Kontrol-Gözlem'), ('KU', 'Kurulum'), ('TD', 'Teknik Destek'), ('TA', 'Tamir')], max_length=2, verbose_name='Servis Türü')),
                ('rapor_yetkili', models.CharField(max_length=25, verbose_name='Rapor Yetkilisi')),
                ('rapor_yetkili_tel', models.CharField(max_length=12, verbose_name='Yetkili Telefon No')),
                ('rapor_yetkili_eposta', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Yetkili E-Posta')),
                ('servis_talep_tarih', models.DateField(blank=True, null=True, verbose_name='Servis Talep Tarihi')),
                ('servis_suresi', models.DurationField(verbose_name='Servis Süresi')),
                ('toplam_mesafe', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2040)], verbose_name='Toplam Mesafe')),
                ('kaide_ankraj', models.BooleanField(default=False, verbose_name='Pompa kaide ankraj civataları ile sabitleşmiş mi?')),
                ('kaide_beton', models.BooleanField(default=False, verbose_name='Pompa kaidenin içine (Grout) beton dökülmüş mü?')),
                ('tesisat_borulama', models.BooleanField(default=False, verbose_name='Tesisattaki borulama pompa ölçülerine uygun mu?')),
                ('tesisat_saportlama', models.BooleanField(default=False, verbose_name='Tesisattaki saportlama uygun mu?')),
                ('basma_kompansatör', models.BooleanField(default=False, verbose_name='Basma hattında kompansatör var mı?')),
                ('basma_manometre', models.BooleanField(default=False, verbose_name='Basma hattında manometre var mı?')),
                ('basma_kesme_vanasi', models.BooleanField(default=False, verbose_name='Basma hattında kesme vanası var mı?')),
                ('basma_cekvalf', models.BooleanField(default=False, verbose_name='Basma hattında çekvalf var mı?')),
                ('pompa_havasi', models.BooleanField(default=False, verbose_name='Pompa(lar)ın havası alındı mı?')),
                ('besleme_gerilim', models.BooleanField(default=False, verbose_name='Besleme gerilimi uygun mu? (şebeke / şantiye)')),
                ('motor_baglanti', models.BooleanField(default=False, verbose_name='Elektrik motor bağlantıları ve termik ayarı kontrolü yapıldı mı?')),
                ('motor_isinma', models.BooleanField(default=False, verbose_name='Motorda ısınma var mı?')),
                ('pompa_ses', models.BooleanField(default=False, verbose_name='Pompada ses var mı?')),
                ('genlesme_tanki', models.BooleanField(default=False, verbose_name='Genleşme tankı orijinal KSB ürünü mü?')),
                ('hidrofor_basinc', models.BooleanField(default=False, verbose_name='Hidroforun devreye giriş çıkış basıncı kontrol edildi mi?')),
                ('ilk_devreye_alma', models.BooleanField(default=False, verbose_name='İlk devreye alma yetkili servis tarafından yapıldı mı?')),
                ('beton_kaide', models.BooleanField(default=False, verbose_name='Beton kaide var mı?')),
                ('kaide_pompa_terazi', models.BooleanField(default=False, verbose_name='Kaide(ler) ve pompa(lar) terazisinde mi?')),
                ('tesisat_akiskan', models.BooleanField(default=False, verbose_name='Tesisatta yeterli akışkan var mı?')),
                ('muhafaza', models.BooleanField(default=False, verbose_name='Ürünler uygun muhafaza edilmiş mi?')),
                ('emme_kompansator', models.BooleanField(default=False, verbose_name='Emme hattında kompansatör var mı?')),
                ('emme_manometre', models.BooleanField(default=False, verbose_name='Emme hattında manometre var mı?')),
                ('emme_kesme_vanasi', models.BooleanField(default=False, verbose_name='Emme hattında kesme vanası var mı?')),
                ('emme_filtre', models.BooleanField(default=False, verbose_name='Emme hattına filtre var mı?')),
                ('yag_seviyesi', models.BooleanField(default=False, verbose_name='Yağ seviyesi yeterli mi?')),
                ('motor_etiket_limit', models.BooleanField(default=False, verbose_name='Elektrik motoru etiket bilgileri kullanım limitleri içinde mi?')),
                ('motor_donme_yonu', models.BooleanField(default=False, verbose_name='Elektrik motoru dönme yönü doğru mu?')),
                ('yerlesim_sicaklik', models.BooleanField(default=False, verbose_name='Yerleşim mahalinin sıcaklığı uygun mu?')),
                ('flator_baglantı', models.BooleanField(default=False, verbose_name='Pano flatör bağlantısı yapıldı mı?')),
                ('genlesme_tank_basinc', models.BooleanField(default=False, verbose_name='Genleşme tank basıncı uygun mu?')),
                ('pompa_etiket_calisma', models.BooleanField(default=False, verbose_name='Pompa etiket değerlerinde çalışıyor mu?')),
                ('yerlesim_drenaj', models.BooleanField(default=False, verbose_name='Yerleşim mahalinde drenaj hattı var mı?')),
                ('rapor_detay', models.TextField(max_length=3000, verbose_name='Açıklama')),
                ('servis_personel_onay', models.BooleanField(default=False, verbose_name='Servis Personelinin Onayı')),
                ('rapor_musteri_yetkili_onay', models.BooleanField(default=False, verbose_name='Müşteri Yetkilisinin Onayı')),
                ('rapor_musteri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musteri.Musteri')),
                ('rapor_saha', models.ForeignKey(limit_choices_to={'musteri_saha': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musteri.Musteri')}, on_delete=django.db.models.deletion.CASCADE, to='Musteri.Saha')),
                ('servis_personel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('servis_pompa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServisRapor.Pompa')),
            ],
            options={
                'verbose_name': 'Servis Raporu',
                'verbose_name_plural': 'Servis Raporları',
            },
        ),
    ]