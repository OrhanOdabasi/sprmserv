from django.db import models


class Musteri(models.Model):

    class Meta:
        # Müşteri bilgilerinin kaydedilmesi
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"

    firma_adi = models.CharField(max_length=60, null=False, blank=False, verbose_name="Firma Adı")
    firma_adresi = models.TextField(max_length=200, null=False, blank=False, verbose_name="Firma Adresi")

    def __str__(self):
        return f"{self.firma_adi}"

    def save(self, *args, **kwargs):
        self.firma_adi = self.firma_adi.lower().title()
        self.firma_adresi = self.firma_adresi.lower().title()
        super(Musteri, self).save(*args, **kwargs)


class Saha(models.Model):

    class Meta:
        # Müşterinin saha bilgilerinin kaydedilmesi
        verbose_name = "Saha"
        verbose_name_plural = "Sahalar"

    musteri_saha = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    saha_adi = models.CharField(max_length=30, null=False, blank=False, verbose_name="Saha Adı")
    saha_adresi = models.TextField(max_length=200, null=False, blank=False, verbose_name="Saha Adresi")

    def __str__(self):
        return f"{self.musteri_saha} - {self.saha_adi}"

    def save(self, *args, **kwargs):
        self.saha_adi = self.saha_adi.lower().title()
        self.saha_adresi = self.saha_adresi.lower().title()
        super(Saha, self).save(*args, **kwargs)        
