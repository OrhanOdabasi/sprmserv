from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from PompaModel.models import PompaModel
import os


@receiver(post_delete, sender=PompaModel)
def pompa_dosya_silme(sender, instance, **kwargs):
    # Pompa kaydı silindiğinde pompaya ait dosyaları da siler
    pompa_dosyalari =   [instance.pompa_resim,
                        instance.pompa_bi_kitapcigi,
                        instance.pompa_tip_kitapcigi,
                        instance.pompa_patlamis]
    for member in pompa_dosyalari:
        if member:
            if os.path.exists(member.path):
                os.remove(member.path)
