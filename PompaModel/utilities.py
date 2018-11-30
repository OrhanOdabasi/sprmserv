# PompaModel için ek fonksiyonlar
import re


def dosya_isimlendirme(dosya_ismi, dosya_yolu, pompa_adi, dosya_tanimi):
    p = re.match(r'(.+)\.([A-z]{3})', str(dosya_ismi))
    return f"{dosya_yolu}{pompa_adi}_{dosya_tanimi}.{p.group(2)}"

def pompa_resim_isimlendirme(instance, filename):
    # upload edilen resmin yeniden isimlendirilmesi
    pompa_adi = instance.pompa_model
    return dosya_isimlendirme(filename, "Pompa_Resimleri/", pompa_adi, "PompaResmi")

def pompa_bi_isimlendirme(instance, filename):
    # upload edilen bi dosyasının isimlendirilmesi
    pompa_adi = instance.pompa_model
    return dosya_isimlendirme(filename, "Bakim_Isletme/", pompa_adi, "BIKitapcik")

def pompa_tip_isimlendirme(instance, filename):
    # upload edilen tip dosyasının isimlendirilmesi
    pompa_adi = instance.pompa_model
    return dosya_isimlendirme(filename, "Tip/", pompa_adi, "TipKitapcigi")

def pompa_patlamis_isimlendirme(instance, filename):
    # upload edilen patlamış resmin isimlendirilmesi
    pompa_adi = instance.pompa_model
    return dosya_isimlendirme(filename, "Patlamis/", pompa_adi, "Patlamis")
