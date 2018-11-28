## Servis Yönetim Sistemi
### Pompa Döküman Arşiv Modülü

Pompa dokümanlarının kaydedilmesi / müşteriyle paylaşılması
- [x] Veritabanı
- [ ] Back End
- [ ] Front End

* **PompaModel  (Class)**
* pompa
* pompa_aciklama
* pompa_bi_kitapcigi
* pompa_tip_kitapcigi
* pompa_patlamis
* pompa_resim

### Servis Talep Modülü

Servis organizasyonu talep formu
Devreye alma talep formu
Bakım sözleşmesi talep formu

- [x] Veritabanı
- [ ] Back End
- [ ] Front End

* **Talep (Class)**
* talep_no
* talep_firma_adi
* talep_amaci
* talep_yetkili
* talep_yetkili_tel
* talep_pompa_adi -> PompaModel.pompa
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

Personel araç kullanım bilgileri
Araç kayıtları (sigorta tarihi, muayene tarihi, bakım tarihi)

- [x] Veritabanı
- [ ] Back End
- [ ] Front End

* **Arac (Class)**
* plaka
* model
* sigorta_tarihi
* muayene_tarihi
* bakim_tarihi

* **AracKullanim (Class)**
* arac_surucu -> User
* arac_kullanim -> Arac
* alis_tarih
* teslim_tarih
* teslim_km
_Servis yönlendirme eklenecek_

### Müşteri Bilgi Modülü

Temel müşteri bilgileri
Servis raporu için saha bilgileri

- [x] Veritabanı
- [ ] Back End
- [ ] Front End

* **Musteri (Class)**
* firma_adi
* firma_adresi

* **Saha (Class)**
* musteri_saha -> Musteri
* saha_adi
* saha_adresi
* saha_ilgili
* saha_ilgili_tel
* saha_ilgili_eposta


### Raporlama Modülü

Servis raporu hazırlama
Ürün servis geçmişinin kaydedilmesi
Ürün üzerine yapıştırılan QR kodu ile bilgilere erişim

- [x] Veritabanı
- [ ] Back End
- [ ] Front End

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


### Servis Planlama Modülü

Organizasyon planlama
Personel yönlendirme
Personel servis programının kaydı, kontrolü ve takibi

- [ ] Veritabanı
- [ ] Back End
- [ ] Front End

### Periyodik Bakım Modülü

Periyodik bakım sözleşmesi oluşturma
Periyodik bakım planlama / hatırlatma

- [ ] Veritabanı
- [ ] Back End
- [ ] Front End

### Yetkili Servis Entegrasyon Modülü

Servis organizasyon yönlendirme
Servis raporu paylaşımı
Hakediş hesaplama

- [ ] Veritabanı
- [ ] Back End
- [ ] Front End
___

### Ek Veritabanı Tabloları ###

- [ ] Kullanıcı Ek Bilgileri _Henüz Belirlenmedi_
