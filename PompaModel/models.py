from django.db import models

# Create your models here.
class PompaModel(models.Model):

    class Meta:
        # KSB pompa modelleri listesi
        verbose_name = "Pompa Modeli"
        verbose_name_plural = "Pompa Modelleri"

    pompa = models.CharField(max_length=20, verbose_name="Pompa Modeli")
    pompa_aciklama = models.TextField(max_length=160, verbose_name="Pompa Açıklaması")
    # TODO: pompa_resim
    # TODO: pompa_bi_kitapcigi
    # TODO: pompa_tip_kitapcigi
    # TODO: pompa_patlamis

    def __str__(self):
        return "{pompa} - {pompa_aciklama}".format(pompa=self.pompa, pompa_aciklama=self.pompa_aciklama)
