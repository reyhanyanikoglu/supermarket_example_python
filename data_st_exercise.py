from merhaba import toplam
from project3 import value

alisveris_listesi = ["süt", "elma", "portakal", "patates", "ekmek"]

#listeye muz ve soğan ekleme
alisveris_listesi.append("muz")
#listenin belirli bir yerine soğan ekleme
alisveris_listesi.insert(1,"soğan")

print(alisveris_listesi)

alisveris_listesi.remove("patates")

#tuple yapısı ile reyon bilgisi eklemek
alisveris_listesi = [("süt","süt ürünleri"),("elma", "meyve"),("portakal", "meyve"),("ekmek","fırın"),("muz","meyve"),("soğan", "sebze")]

print(alisveris_listesi)

#dict yapısı ile reyon eklemek
alisveris_listesi = {
    "süt": "süt ürünleri",
    "elma": "meyve",
    "portakal": "meyve",
    "ekmek": "fırın",
    "muz": "meyve",
    "soğan": "sebze"
}

#sözlükteki keys values ve key/value değerlerini yazdırma
print("ürünler", alisveris_listesi.keys())
print("reyonlar",alisveris_listesi.values())
print("Ürün ve reyon bilgileri: ",alisveris_listesi.items())

#stok içeren bir envanter kullanma
#her ürün için fiyat, stok bilgisi ve reyon bilgisi bulunuyor
envanter = {
    "süt": [10, 20, "süt ürünleri"],
    "elma": [5, 50, "meyve"],
    "portakal": [7, 30, "meyve"],
    "ekmek": [2, 40, "fırın"],
    "muz": [8, 25, "meyve"],
    "soğan": [3,60, "sebze"]
}

#müşterinin alışveriş listesini oluşturma
musteri_alisveris_listesi = [("süt", 80), ("elma", 5), ("ekmek", 1)] # ürün , adet

#stok kontrol fonksiyonu
def stok_kontrol(alisveris_listesi, envanter):
    guncel_liste = []
    for urun, miktar in alisveris_listesi:
        stok = envanter[urun][1]  #ürün anahtarına karşılık gelen değerden stok miktarını alıyor
        if miktar > stok:
            print(f"{urun} stokta yetersiz.")
            guncel_liste.append((urun,stok))
        else:
            guncel_liste.append((urun,miktar))
    return guncel_liste

guncel_alisveris_listesi = stok_kontrol(musteri_alisveris_listesi, envanter)
print("Güncellenmiş alışveriş listesi: ",guncel_alisveris_listesi)


def fatura_hesapla(guncel_liste, envanter):
    toplam_fiyat = 0
    for urun, miktar in guncel_liste:
        fiyat = envanter[urun][0]
        toplam_fiyat += fiyat*miktar
    return toplam_fiyat

toplam_fiyat = fatura_hesapla(guncel_alisveris_listesi, envanter)
print("Toplam fiyat: ",toplam_fiyat, "$")

#stok güncelleme fonksiyonu
#alışveriş sonrası envanterdeki stokları günceller
def stok_guncelle(guncel_liste, envanter):
    for urun, miktar in guncel_liste:
        envanter[urun][1] -= miktar
    print("stoklar güncellendi: ",envanter)

stok_guncelle(guncel_alisveris_listesi, envanter)