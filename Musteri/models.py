from django.db import models

# Create your models here.

class Musteri(models.Model):

    class Meta:
        # Customer model
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"

    firma_adi = models.CharField(max_length=60, null=False, blank=False, verbose_name="Firma Adı")
    firma_adresi = models.TextField(max_length=200, null=False, blank=False, verbose_name="Firma Adresi")

    def __str__(self):
        return f"{self.firma_adi}"


class Saha(models.Model):

    class Meta:
        # Site model
        verbose_name = "Saha"
        verbose_name_plural = "Sahalar"

    musteri_saha = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    saha_adi = models.CharField(max_length=30, null=False, blank=False, verbose_name="Saha Adı")
    saha_adresi = models.TextField(max_length=200, null=False, blank=False, verbose_name="Saha Adresi")
    saha_ilgili = models.CharField(max_length=25, null=False, blank=False, verbose_name="Saha İlgilisi")
    saha_ilgili_tel = models.CharField(max_length=12, null=False, blank=False, verbose_name="İlgili Tel.")
    saha_ilgili_eposta = models.EmailField(null=True, blank=False, verbose_name="İlgili E-Posta")

    def __str__(self):
        return f"{self.musteri_saha} || {self.saha_ilgili}"
