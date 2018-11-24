from django.db import models
from PompaModel.models import PompaModel
from .utilities import createRequetNo


class Talep(models.Model):

    class Meta:
        # Service request model
        verbose_name = "Servis Talebi"
        verbose_name_plural = "Servis Talepleri"

    talep_no = models.CharField(max_length=6, null=False, blank=True, verbose_name="Talep No")
    firma_adi = models.CharField(max_length=60, null=False, blank=False, verbose_name="Firma Adı")
    talep_yetkili = models.CharField(max_length=30, null=False, blank=False, verbose_name="Talep Yetkilisi")
    talep_yetkili_tel = models.CharField(max_length=12, null=False, blank=False, verbose_name="Yetkili Telefonu")
    talep_pompa_adi = models.ForeignKey(PompaModel, on_delete=models.CASCADE)
    talep_pompa_tipi = models.CharField(max_length=20, null=True, blank=False   , verbose_name="Pompa Tipi")
    talep_pompa_serino = models.CharField(max_length=20, null=False, blank=False, verbose_name="Pompa Seri No")
    talep_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Talep Tarihi")
    enerji_kontrol = models.BooleanField(default=False, verbose_name="Enerji Kontrolleri")
    akiskan_kontrol = models.BooleanField(default=False, verbose_name="Akışkan Kontrolleri")
    personel = models.BooleanField(default=False, verbose_name="Yardımcı Personel")
    sizdirmazlik = models.BooleanField(default=False, verbose_name="Tesisat Sızdırmazlık Testi")
    pompa_hazir = models.BooleanField(default=False, verbose_name="Pompa Hazır")
    on_hazirlik = models.BooleanField(default=False, verbose_name="Kitapçık Ön Hazırlık")
    betonlama = models.BooleanField(default=False, verbose_name="Grout Betonlama")
    is_sagligi = models.BooleanField(default=False, verbose_name="İş Sağlığı Tedbirleri")
    talep_org_tarihi = models.DateField(verbose_name="Organizasyon Tarih Talebi", blank=False)
    yetkili_onayi = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f"{self.talep_no} || {self.firma_adi} || {self.talep_yetkili}"

    def save(self, *args, **kwargs):
        self.talep_no = createRequetNo(self)
        super(Talep, self).save(*args, **kwargs)
