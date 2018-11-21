## Servis Yönetim Sistemi
### Pompa Döküman Arşiv Modülü

- [ ] Pompa dokümanlarının kaydedilmesi / müşteriyle paylaşılması

* **PompaModel  (Class)**
* pompa
* pompa_aciklama
* pompa_bi_kitapcigi
* pompa_tip_kitapcigi
* pompa_patlamis
* pompa_resim

### Servis Talep Modülü

- [ ] Servis organizasyonu talep formu
- [ ] Devreye alma talep formu
- [ ] Bakım sözleşmesi talep formu

* **Talep (Class)**
* talep_firma_adi
* talep_amaci
* talep_yetkili
* talep_yetkili_tel
* talep_pompa_adi | Pompalar.pompa
* talep_pompa_tipi
* talep_pompa_serino
* talep_tarihi
* enerji | bool
* akiskan | bool
* personel | bool
* sizdirmazlik | bool
* hazir | bool
* on_hazirlik | bool
* betonlama | bool
* is_sagligi | bool
* talep_org_tarihi
* onay | bool

### Araç Takip Modülü

- [ ] Personel araç kullanım bilgileri
- [ ] Araç kayıtları (km, sigorta tarihi, muayene tarihi, bakım tarihi)

* **Arac (Class)**
* model
* km

### Raporlama Modülü

- [ ] Servis raporu hazırlama
- [ ] Ürün servis geçmişinin kaydedilmesi
- [ ] Ürün üzerine yapıştırılan QR kodu ile bilgilere erişim

* **ServisRapor (Class)**
* rapor_no
* kontrol_turu
* musteri
* saha
* yetkili_kisi
* yetkili_telefon
* yetkili_mail
* talep_tarihi
* gidis_tarihi
* donus_tarihi
* toplam_mesafe
* Pompa (Class)
* Kontrol Tablosu
* aciklama
* servis_personel_onay
* musteri_onay

* **Pompa (Class)**
* Pompalar.pompa
* pompa_tipi
* pompa_serino
* pompa_uretim_yili
* pompa_debi
* pompa_yukseklik
* pompa_debi
* pompa_akiskan
* pompa_akiskan_sicaklik
* motor_tipi
* motor_serino
* motor_guc
* motor_devir
* motor_uretim_yili

* **Musteri (Class)**
* firma_adi
* firma_adresi

* **Saha (Class)**
* saha_adi
* saha_adresi
* saha_adresi
* saha_ilgili
* saha_ilgili_tel
* saha_ilgili_eposta

### Servis Planlama Modülü

- [ ] Organizasyon planlama
- [ ] Personel yönlendirme
- [ ] Personel servis programının kaydı, kontrolü ve takibi

### Periyodik Bakım Modülü

- [ ] Periyodik bakım sözleşmesi oluşturma
- [ ] Periyodik bakım planlama / hatırlatma

### Yetkili Servis Entegrasyon Modülü

- [ ] Servis organizasyon yönlendirme
- [ ] Servis raporu paylaşımı
- [ ] Hakediş hesaplama

___

### Ek Veritabanı Tabloları ###

- [ ] Kullanıcı Ek Bilgileri _Henüz Belirlenmedi_
