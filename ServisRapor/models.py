from django.db import models
from Musteri.models import Musteri, Saha
from django.contrib.auth.models import User
from PompaModel.models import PompaModel
from .utilities import createReportNo
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Pompa(models.Model):

    class Meta:
        # Servis sırasında kontrol edilen pompa
        verbose_name = "Pompa"
        verbose_name_plural = "Pompalar"

    servis_pompa = models.ForeignKey(PompaModel, on_delete=models.CASCADE)
    servis_pompa_tip = models.CharField(max_length=20, null=True, blank=False, verbose_name="Pompa Tipi")
    servis_pompa_serino = models.CharField(max_length=20, null=False, blank=False, verbose_name="Pompa Seri No")
    servis_pompa_uretim_yıl = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1871)], null=True, blank=True, verbose_name="Pompa Üretim Yılı")
    debi_birim_sec = (
    ('msa', 'm3/sa'),
    ('lsn', 'lt/sn'),
    ('tsa', 't/sa'),
    ('ksa', 'kg/sn'),
    )
    servis_pompa_debi_birim = models.CharField(max_length=3, choices=debi_birim_sec, null=True, blank=True, verbose_name="Debi Birimi")
    servis_pompa_debi = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True, verbose_name="Pompa Debisi")
    servis_pompa_yukseklik = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True, verbose_name="Basma Yüksekliği [mSS]")
    servis_pompa_fan_capi = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], null=True, blank=True, verbose_name="Fan Çapı [mm]")
    servis_pompa_verim = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True, verbose_name="Verim (%)")
    servis_pompa_devir = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], null=False, blank=False, verbose_name="Devir [RPM]")
    guc_birim_sec = (
    ('kw', 'kW'),
    ('mw', 'MW'),
    ('hp', 'HP'),
    )
    servis_pompa_guc_birim = models.CharField(max_length=2, choices=guc_birim_sec, null=True, blank=True, verbose_name="Motor Güç Birimi")
    servis_pompa_guc = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, verbose_name="Pompa Gücü")
    servis_pompa_giris_b = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Giriş Basıncı [bar]")
    servis_pompa_cikis_b = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Çıkış Basıncı [bar]")
    servis_pompa_uretim_yıl = models.PositiveIntegerField(validators=[MinValueValidator(1871), MaxValueValidator(2023)], null=True, blank=True, verbose_name="Pompa Üretim Yılı")
    servis_pompa_akiskan = models.CharField(max_length=15, null=True, blank=True, verbose_name="Akışkan")
    servis_pompa_akiskan_sicaklık = models.IntegerField(validators=[MinValueValidator(-50), MaxValueValidator(400)], null=True, blank=True, verbose_name="Akışkan Sıcaklığı (C)")
    servis_pompa_titresim = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name="Pompa Titreşimi [mm/sn2]")
    servis_pompa_gerilim = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], null=True, blank=True, verbose_name="Pompa Gerilimi [V]")
    servis_pompa_akim = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)], null=True, blank=True, verbose_name="Pompa Akımı [I]")
    servis_pompa_kaplin_tipi = models.CharField(max_length=5, null=True, blank=True, verbose_name="Kaplin Tipi")
    servis_pompa_durkalk = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], null=True, blank=True, verbose_name="Dur-Kalk Sayısı")
    servis_motor_tipi = models.CharField(max_length=25, null=True, blank=True, verbose_name="Motor Tipi")
    servis_motor_serino = models.CharField(max_length=25, null=True, blank=True, verbose_name="Motor Seri No")
    servis_motor_gerilim = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], null=True, blank=True, verbose_name="Motor Gerilimi [V]")
    servis_motor_akim = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)], null=True, blank=True, verbose_name="Motor Akımı [I]")
    servis_motor_guc_birim = models.CharField(max_length=2, choices=guc_birim_sec, null=True, blank=True, verbose_name="Motor Güç Birimi")
    servis_motor_guc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Motor Gücü")
    servis_motor_cosphi = models.IntegerField(validators=[MinValueValidator(-90), MaxValueValidator(90)], null=True, blank=True, verbose_name="Motor CosPhi")
    servis_motor_devir = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], null=True, blank=True, verbose_name="Devir [RPM]")
    servis_motor_uretim_yil = models.IntegerField(validators=[MinValueValidator(1871), MaxValueValidator(2023)], null=True, blank=True, verbose_name="Motor Üretim Yılı")

    def __str__(self):
        return f"{self.servis_pompa} {self.servis_pompa_tip} - {self.servis_pompa_serino}"

    def __save__(self, *args, **kwargs):
        self.servis_pompa_tip = self.servis_pompa_tip.upper()
        self.servis_pompa_akiskan = self.servis_pompa_akiskan.upper()
        super(Pompa, self).save(*args, **kwargs)


class ServisRapor(models.Model):

    class Meta:
        # Servis raporlar kayıtları
        verbose_name = "Servis Raporu"
        verbose_name_plural = "Servis Raporları"

    servis_grubu_sec = (
    ('10', 'Merkez Servis'),
    )
    servis_grubu = models.CharField(choices=servis_grubu_sec, max_length=2, null=False, blank=False, verbose_name="Servis Grubu")
    servis_rapor_no = models.CharField(max_length=13, null=False, blank=True, verbose_name="Rapor No")
    servis_turu_sec = (
        ('BK', 'Bakım'),
        ('DA', 'Devreye Alma'),
        ('KG', 'Kontrol-Gözlem'),
        ('KU', 'Kurulum'),
        ('TD', 'Teknik Destek'),
        ('TA', 'Tamir'),
    )
    servis_turu = models.CharField(choices=servis_turu_sec, max_length=2, null=False, blank=False, verbose_name="Servis Türü")
    rapor_musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, verbose_name="Müşteri")
    rapor_saha = models.ForeignKey(Saha, on_delete=models.CASCADE, verbose_name="Müşteri Saha") # TODO: limit_choices_to ile seçenekleri daraltmak gerekiyor.
    rapor_yetkili = models.CharField(max_length=25, null=False, blank=False, verbose_name="Rapor Yetkilisi")
    rapor_yetkili_tel = models.CharField(max_length=12, null=False, blank=False, verbose_name="Yetkili Telefon No")
    rapor_yetkili_eposta = models.EmailField(null=True, blank=True, verbose_name="Yetkili E-Posta")
    servis_gidis_tarih = models.DateTimeField(null=True, blank=False, verbose_name="Servis Gidiş Tarihi")
    servis_donus_tarih = models.DateTimeField(null=True, blank=False, verbose_name="Servis Donüş Tarihi")
    servis_suresi = models.DurationField(null=True, blank=True, verbose_name="Servis Süresi")
    toplam_mesafe = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2040)], null=False, blank=False, verbose_name="Toplam Mesafe [Km]")
    servis_pompa = models.ForeignKey(Pompa, on_delete=models.CASCADE, verbose_name="Pompa")

    kaide_ankraj = models.BooleanField(default=False, verbose_name="Pompa kaide ankraj civataları ile sabitleşmiş mi?")
    kaide_beton = models.BooleanField(default=False, verbose_name="Pompa kaidenin içine (Grout) beton dökülmüş mü?")
    tesisat_borulama = models.BooleanField(default=False, verbose_name="Tesisattaki borulama pompa ölçülerine uygun mu?")
    tesisat_saportlama = models.BooleanField(default=False, verbose_name="Tesisattaki saportlama uygun mu?")
    basma_kompansatör = models.BooleanField(default=False, verbose_name="Basma hattında kompansatör var mı?")
    basma_manometre = models.BooleanField(default=False, verbose_name="Basma hattında manometre var mı?")
    basma_kesme_vanasi = models.BooleanField(default=False, verbose_name="Basma hattında kesme vanası var mı?")
    basma_cekvalf = models.BooleanField(default=False, verbose_name="Basma hattında çekvalf var mı?")
    pompa_havasi = models.BooleanField(default=False, verbose_name="Pompa(lar)ın havası alındı mı?")
    besleme_gerilim = models.BooleanField(default=False, verbose_name="Besleme gerilimi uygun mu? (şebeke / şantiye)")
    motor_baglanti = models.BooleanField(default=False, verbose_name="Elektrik motor bağlantıları ve termik ayarı kontrolü yapıldı mı?")
    motor_isinma = models.BooleanField(default=False, verbose_name="Motorda ısınma var mı?")
    pompa_ses = models.BooleanField(default=False, verbose_name="Pompada ses var mı?")
    genlesme_tanki = models.BooleanField(default=False, verbose_name="Genleşme tankı orijinal KSB ürünü mü?")
    hidrofor_basinc = models.BooleanField(default=False, verbose_name="Hidroforun devreye giriş çıkış basıncı kontrol edildi mi?")
    ilk_devreye_alma = models.BooleanField(default=False, verbose_name="İlk devreye alma yetkili servis tarafından yapıldı mı?")
    beton_kaide = models.BooleanField(default=False, verbose_name="Beton kaide var mı?")
    kaide_pompa_terazi = models.BooleanField(default=False, verbose_name="Kaide(ler) ve pompa(lar) terazisinde mi?")
    tesisat_akiskan = models.BooleanField(default=False, verbose_name="Tesisatta yeterli akışkan var mı?")
    muhafaza = models.BooleanField(default=False, verbose_name="Ürünler uygun muhafaza edilmiş mi?")
    emme_kompansator = models.BooleanField(default=False, verbose_name="Emme hattında kompansatör var mı?")
    emme_manometre = models.BooleanField(default=False, verbose_name="Emme hattında manometre var mı?")
    emme_kesme_vanasi = models.BooleanField(default=False, verbose_name="Emme hattında kesme vanası var mı?")
    emme_filtre = models.BooleanField(default=False, verbose_name="Emme hattına filtre var mı?")
    yag_seviyesi = models.BooleanField(default=False, verbose_name="Yağ seviyesi yeterli mi?")
    motor_etiket_limit = models.BooleanField(default=False, verbose_name="Elektrik motoru etiket bilgileri kullanım limitleri içinde mi?")
    motor_donme_yonu = models.BooleanField(default=False, verbose_name="Elektrik motoru dönme yönü doğru mu?")
    yerlesim_sicaklik = models.BooleanField(default=False, verbose_name="Yerleşim mahalinin sıcaklığı uygun mu?")
    flator_baglantı = models.BooleanField(default=False, verbose_name="Pano flatör bağlantısı yapıldı mı?")
    genlesme_tank_basinc = models.BooleanField(default=False, verbose_name="Genleşme tank basıncı uygun mu?")
    pompa_etiket_calisma = models.BooleanField(default=False, verbose_name="Pompa etiket değerlerinde çalışıyor mu?")
    yerlesim_drenaj = models.BooleanField(default=False, verbose_name="Yerleşim mahalinde drenaj hattı var mı?")

    rapor_detay = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Açıklama")
    servis_personel = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Servis Personeli")
    servis_personel_onay = models.BooleanField(default=False, verbose_name="Servis Personelinin Onayı")
    rapor_musteri_yetkili_onay = models.BooleanField(default=False, verbose_name="Müşteri Yetkilisinin Onayı")

    def __str__(self):
        return f"{self.servis_rapor_no} - {self.servis_pompa.servis_pompa.pompa_model} {self.servis_pompa.servis_pompa_tip} - {self.rapor_musteri.firma_adi}"

    def save(self, *args, **kwargs):
        # duration field kaydet
        self.servis_suresi = self.servis_donus_tarih - self.servis_gidis_tarih
        # yetkili ilk harfleri büyüt
        self.rapor_yetkili = self.rapor_yetkili.title()
        # rapor numarası belirle / rasgele
        report_no = createReportNo(self, self.servis_grubu)
        self.servis_rapor_no = f"{report_no}"
        super(ServisRapor, self).save(*args, **kwargs)
