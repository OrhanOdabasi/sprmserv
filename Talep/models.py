from django.db import models
from PompaModel.models import PompaModel
from .utilities import createRequetNo


class Talep(models.Model):

    class Meta:
        # Servis taleplerinin kaydedilmesi
        verbose_name = "Servis Talebi"
        verbose_name_plural = "Servis Talepleri"

    talep_no = models.CharField(max_length=6, null=False, blank=True, verbose_name="Talep No")
    firma_adi = models.CharField(max_length=60, null=False, blank=False, verbose_name="Firma Adı")
    talep_yetkili = models.CharField(max_length=30, null=False, blank=False, verbose_name="Talep Yetkilisi")
    talep_yetkili_tel = models.CharField(max_length=12, null=False, blank=False, verbose_name="Yetkili Telefonu")
    talep_pompa_adi = models.ForeignKey(PompaModel, on_delete=models.CASCADE, verbose_name="Pompa")
    talep_pompa_tipi = models.CharField(max_length=20, null=True, blank=False, verbose_name="Pompa Tipi")
    talep_pompa_serino = models.CharField(max_length=20, null=False, blank=False, verbose_name="Pompa Seri No")
    talep_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Talep Tarihi")
    enerji_kontrol = models.BooleanField(default=False, verbose_name="Sistem enerji ve bağlantıları hazır mı?")
    akiskan_kontrol = models.BooleanField(default=False, verbose_name="Sistem içinde akışkan var mı?")
    personel = models.BooleanField(default=False, verbose_name="Yardımcı teknik personel var mı?")
    sizdirmazlik = models.BooleanField(default=False, verbose_name="Tesisatın sızdırmazlık testi yapıldı mı?")
    pompa_hazir = models.BooleanField(default=False, verbose_name="Pompa(lar) çalışmaya hazır mı?")
    on_hazirlik = models.BooleanField(default=False, verbose_name="Pompa(lar) ile beraber gönderilen bakım kitapçığı okundu mu?")
    betonlama = models.BooleanField(default=False, verbose_name="Pompa kaidesi betonla (grout) sabitlendi mi?")
    is_sagligi = models.BooleanField(default=False, verbose_name="İş Sağlığı ve güvenliği çerçevesinde gerekli önlemler alındı mı?")
    talep_org_tarihi = models.DateField(blank=False, verbose_name="Organizasyon Tarih Talebi")
    yetkili_onayi = models.BooleanField(default=False, null=False, blank=False, verbose_name="Yetkili Onayı")

    def __str__(self):
        return f"{self.talep_no} || {self.firma_adi} || {self.talep_yetkili}"

    def save(self, *args, **kwargs):
        self.talep_no = createRequetNo(self)
        self.firma_adi = self.firma_adi.lower().title()
        self.talep_yetkili = self.talep_yetkili.title()
        self.talep_pompa_tipi = self.talep_pompa_tipi.upper()
        super(Talep, self).save(*args, **kwargs)
