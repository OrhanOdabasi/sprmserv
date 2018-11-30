from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from .models import PompaModel
import os


@receiver(post_save, sender=PompaModel)
def deneme(sender, created, instance, **kwargs):
    print("signal recieved")

@receiver(pre_delete, sender=PompaModel)
def pompa_dosya_silme(sender, instance, **kwargs):
    # Pompa kaydı silindiğinde pompaya ait dosyaları da siler
    print("signal recieved")
    pompa_dosyalari =   [instance.pompa_resim,
                        instance.pompa_bi_kitapcigi,
                        instance.pompa_tip_kitapcigi,
                        instance.pompa_patlamis]
    for _ in pompa_dosyalari:
        if os.path.exists(_.path):
            os.remove(_.path)
            print(f"{_.path} Silindi!")
