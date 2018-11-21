from django.db import models
# from.utilities import *

# Create your models here.
class PompaModel(models.Model):

    class Meta:
        # KSB pompa modelleri listesi
        verbose_name = "Pompa Modeli"
        verbose_name_plural = "Pompa Modelleri"

    pompa = models.CharField(max_length=20, null=True, blank=False, unique=True, verbose_name="Pompa Modeli")
    pompa_aciklama = models.TextField(max_length=160,null=True, blank=False, verbose_name="Pompa Açıklaması")
    pompa_resim = models.ImageField(upload_to="Pompa_Resimleri/", null=True, blank=False, verbose_name="Pompa Resmi")
    pompa_bi_kitapcigi = models.FileField(upload_to="Bakim_İsletme/", null=True, blank=True, verbose_name="Bakım İşletme Kitapçığı")
    pompa_tip_kitapcigi = models.FileField(upload_to="Tip/", null=True, blank=True, verbose_name="Tip Kitapçığı")
    pompa_patlamis = models.FileField(upload_to="Patlamis/", null=True, blank=True, verbose_name="Patlamış Resim")

    def __str__(self):
        return "{pompa} - {pompa_aciklama}".format(pompa=self.pompa, pompa_aciklama=self.pompa_aciklama)

    def save(self, *args, **kwargs):
        self.pompa = self.pompa.upper()
        super(PompaModel, self).save(*args, **kwargs)

    # TODO: Delete media file when the instance is deleted
