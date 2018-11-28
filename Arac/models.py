from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Arac(models.Model):

    class Meta:
    # Model for vehicle and their drivers
        verbose_name = "Araç"
        verbose_name_plural = "Araçlar"

    arac_plaka = models.CharField(max_length=11, null=False, blank=False, unique=True, verbose_name="Araç Plakası")
    arac_model = models.CharField(max_length=25, null=False, blank=False, verbose_name="Araç Modeli")
    arac_sigorta_tarih = models.DateField(verbose_name="Araç Sigorta Tarihi")
    arac_muayene_tarih = models.DateField(verbose_name="Araç Muayene Tarihi")
    arac_bakim_tarih = models.DateField(verbose_name="Araç Bakım Tarihi")
    arac_ego_tarih = models.DateField(null=True, blank=True, verbose_name="Araç Ego Tarihi")

    def __str__(self):
        return f"{self.arac_plaka} || {self.arac_model}"

    def save(self, *args, **kwargs):
        self.arac_plaka = self.arac_plaka.upper()
        self.arac_model = self.arac_model.lower().title()
        super(Arac, self).save(*args, **kwargs)


class AracKullanim(models.Model):

    class Meta:
        # Vehicle driving details
        verbose_name = "Araç Kullanımı"
        verbose_name_plural = "Araç Kullanımları"

    arac_surucu = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Araç Sürücüsü")
    arac_kullanim = models.ForeignKey(Arac, default=0, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Kullandığı Araç") # fix default=0
    arac_alis_tarih = models.DateTimeField(null=False, blank=False, verbose_name="Araç Alış Tarihi")
    arac_teslim_tarihi = models.DateTimeField(null=False, blank=False, verbose_name="Araç Teslim Tarihi")
    arac_teslim_km = models.IntegerField(null=False, blank=False, verbose_name="Teslim KM")

    def __str__(self):
        return f"{self.arac_surucu} || {self.arac_teslim_km}"
