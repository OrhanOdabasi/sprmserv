from django.db import models
from Musteri.models import Musteri, Saha
from django.contrib.auth.models import User
from PompaModel.models import PompaModel
from .utilities import createReportNo
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Pompa(models.Model):

    class Meta:
        # Servis sırasında kontrol edilen pompa
        verbose_name = "Pompa"
        verbose_name_plural = "Pompalar"

    servis_pompa = models.ForeignKey(PompaModel, on_delete=models.CASCADE, verbose_name="Pompa Modeli")
    servis_pompa_tip = models.CharField(max_length=20, null=True, blank=False, verbose_name="Pompa Tipi")
    servis_pompa_serino = models.CharField(max_length=20, null=False, blank=False, verbose_name="Pompa Seri No")
    servis_pompa_uretim_yıl = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1871)], null=True, blank=True, verbose_name="Pompa Üretim Yılı")
    debi_birim_sec = (
    ('msa', 'm3/sa'),
    ('lsn', 'lt/sn'),
    ('tsa', 't/sa'),
    ('ksa', 'kg/sn'),
    )
    servis_pompa_debi_birim = models.CharField(choices=debi_birim_sec, null=True, blank=True, verbose_name="Debi Birimi")
    servis_pompa_debi = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True, verbose_name="Pompa Debisi") # NOTE: hangi ölçü biriminden kaydedilecek
    servis_pompa_yukseklik = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True, verbose_name="Basma Yüksekliği [mSS]") # NOTE: hangi ölçü biriminden kaydedilecek
    servis_pompa_fan_capi = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], null=True, blank=True, verbose_name="Fan Çapı")
    servis_pompa_verim = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True, verbose_name="Verim")
    servis_pompa_devir = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], null=False, blank=False, verbose_name="Devir [RPM]")
    pompa guc_birim_sec = (
    ('kw', 'kW'),
    ('mw', 'MW'),
    ('hp', 'HP'),
    )
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
    servis_pompa_durkalk = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], null=True, False=True, verbose_name="Dur-Kalk Sayısı")
    servis_motor_tipi = models.CharField(max_length=25, null=True, blank=True, verbose_name="Motor Tipi")
    servis_motor_serino = models.CharField(max_length=25, null=True, blank=True, verbose_name="Motor Seri No")
    servis_motor_gerilim = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], null=True, blank=True, verbose_name="Motor Gerilimi [V]")
    servis_motor_akim = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)], null=True, blank=True, verbose_name="Motor Akımı [I]")
    motor_guc_birim_sec = (
    ('kw', 'kW'),
    ('mw', 'MW'),
    ('hp', 'HP'),
    )
    servis_motor_guc_birim = models.CharField(choices=motor_guc_birim_sec, null=True, blank=True, verbose_name="Motor Güç Birimi")
    servis_motor_guc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Motor Gücü")
    servis_motor_cosphi = models.IntegerField(validators=[MinValueValidator(-90), MaxValueValidator(90)], null=True, blank=True, verbose_name="Motor CosPhi")
    servis_motor_devir = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], null=True, blank=True, verbose_name="Devir [RPM]")
    servis_motor_uretim_yil = models.IntegerField(validators=[MinValueValidator(1871), MaxValueValidator(2023)], null=True, blank=True, verbose_name="Motor Üretim Yılı")

    def __str__(self):
        return f"{self.servis_pompa} - {self.servis_pompa_tip} - {self.servis_pompa_serino}"

    def __save__(self, *args, **kwargs):
        self.servis_pompa_tip = self.servis_pompa_tip.upper()
        self.servis_pompa_akiskan = self.servis_pompa_akiskan.upper()
        super(Pompa, self).save(*args, **kwargs)


# kontrol edilecek
class ServisRapor(models.Model):

    class Meta:
        # Servis raporlar kayıtları
        verbose_name = "Servis Raporu"
        verbose_name_plural = "Servis Raporları"

    servis_grubu_sec = (
    ('10', 'Merkez Servis'),
    )
    servis_grubu = models.CharField(choices=servis_grubu_sec, max_length=3, null=False, blank=False, verbose_name="Servis Grubu")
    servis_rapor_no = models.CharField(max_length=14, null=False, blank=False, verbose_name="Rapor No")
    kategoriler = (
    ('BK', 'Bakım'),
    ('DA', 'Devreye Alma'),
    ('KG', 'Kontrol-Gözlem'),
    ('KU', 'Kurulum'),
    ('TD', 'Teknik Destek'),
    ('TA', 'Tamir'),
    )
    servis_turu = models.CharField(choices=kategoriler, max_length=2, null=False, blank=False, verbose_name="Servis Türü")
    rapor_musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    rapor_saha = models.ForeignKey(Saha, on_delete=models.CASCADE, limit_choices_to={'musteri_saha' : rapor_musteri})
    rapor_yetkili = models.CharField(max_length=25, null=False, blank=False, verbose_name="Rapor Yetkilisi")
    rapor_yetkili_tel = models.CharField(max_length=12, null=False, blank=False, verbose_name="Yetkili Telefon No")
    rapor_yetkili_eposta = models.EmailField(null=True, blank=True, verbose_name="Yetkili E-Posta")
    servis_talep_tarih = models.DateField(null=True, blank=True, verbose_name="Servis Talep Tarihi")
    servis_suresi = models.DurationField(null=False, blank=False, verbose_name="Servis Süresi")
    toplam_mesafe = models.IntegerField(null=False, blank=False, verbose_name="Toplam Mesafe")
    servis_pompa = models.ForeignKey(Pompa, on_delete=models.CASCADE)

    # TODO: kontrol listesi eklenecek

    rapor_detay = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Açıklama")
    servis_personel = models.ForeignKey(User, on_delete=models.CASCADE)
    servis_personel_onay = models.BooleanField(default=False, verbose_name="Servis Personelinin Onayı")
    rapor_musteri = models.CharField(max_length=25, null=False, blank=False, verbose_name="Müşteri Temsilcisi")
    rapor_musteri_onay = models.BooleanField(default=False, verbose_name="Müşteri Temsilcisinin Onayı")
