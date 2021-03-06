from django.db import models
import os
from .utilities import (pompa_resim_isimlendirme,
                        pompa_bi_isimlendirme,
                        pompa_tip_isimlendirme,
                        pompa_patlamis_isimlendirme)


class PompaModel(models.Model):

    class Meta:
        # KSB Pompa tiplerinin kaydedilmesi
        verbose_name = "Pompa Modeli"
        verbose_name_plural = "Pompa Modelleri"

    pompa_model = models.CharField(max_length=20, null=True, blank=False, unique=True, verbose_name="Pompa Modeli") # TODO: null must be false in production
    pompa_aciklama = models.TextField(max_length=160, null=True, blank=False, verbose_name="Pompa Açıklaması") # TODO: null must be false in production
    pompa_resim = models.ImageField(upload_to=pompa_resim_isimlendirme, null=True, blank=False, verbose_name="Pompa Resmi")
    pompa_bi_kitapcigi = models.FileField(upload_to=pompa_bi_isimlendirme, null=True, blank=True, verbose_name="Bakım İşletme Kitapçığı")
    pompa_tip_kitapcigi = models.FileField(upload_to=pompa_tip_isimlendirme, null=True, blank=True, verbose_name="Tip Kitapçığı")
    pompa_patlamis = models.FileField(upload_to=pompa_patlamis_isimlendirme, null=True, blank=True, verbose_name="Patlamış Resim")

    def __str__(self):
        return f"{self.pompa_model} - {self.pompa_aciklama}"

    def save(self, *args, **kwargs):
        self.pompa_model = self.pompa_model.upper()
        self.pompa_aciklama = self.pompa_aciklama.lower().capitalize()
        super(PompaModel, self).save(*args, **kwargs)
