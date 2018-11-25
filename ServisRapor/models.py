from django.db import models
from Musteri.models import Musteri
from django.contrib.auth.models import User

# Create your models here.
class ServisRapor(models.Model):

    class Meta:
        # Servis raporlar kayıtları
        verbose_name = "Servis Raporu"
        verbose_name_plural = "Servis Raporları"

    # TODO: Servis rapor numarası ekle
    kategoriler = (
    ('BK', 'Bakım Kontrolü'),
    ('DA', 'Devreye Alma'),
    ('KG', 'Kontrol-Gözlem'),
    ('KU', 'Kurulum'),
    ('TD', 'Teknik Destek'),
    ('TA', 'Tamir'),
    )
    servis_turu = models.CharField(choices=kategoriler, max_length=2, null=False, blank=False, verbose_name="Servis Türü")
    rapor_musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    # burada sıkıntı çıkabilir. sadece müşterinin saha bilgileri olmalı rapor_saha
    rapor_yetkili = models.CharField(max_length=25, null=False, blank=False, verbose_name="Rapor Yetkilisi")
    rapor_yetkili_tel = models.CharField(max_length=12, null=False, blank=False, verbose_name="Yetkili Telefon No")
    rapor_yetkili_eposta = models.EmailField(null=True, blank=True, verbose_name="Yetkili E-Posta")
    servis_talep_tarih = models.DateField(null=True, blank=True, verbose_name="Servis Talep Tarihi")
    gidis_tarih = models.DateTimeField(null=False, blank=False, verbose_name="Gidiş Tarihi")
    donus_tarih = models.DateTimeField(null=False, blank=False, verbose_name="Dönüş Tarihi")
    toplam_mesafe = models.IntegerField(null=False, blank=False, verbose_name="Toplam Mesafe")
    # TODO: class pompa yaratılacak
    # TODO: kontrol listesi eklenecek
    rapor_detay = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Açıklama")
    servis_personel = models.ForeignKey(User, on_delete=models.CASCADE) # WARNING: kullanıcı silinirse servis raporu silinmemeli
    servis_personel_onay = models.BooleanField(default=False, verbose_name="Servis Personelinin Onayı")
    rapor_musteri = models.CharField(max_length=25, null=False, blank=False, verbose_name="Müşteri Temsilcisi")
    rapor_musteri_onay = models.BooleanField(default=False, verbose_name="Müşteri Temsilcisinin Onayı")
