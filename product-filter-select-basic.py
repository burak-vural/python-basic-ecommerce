import requests
from bs4 import BeautifulSoup

def urun_bilgilerini_cek(urun_linki):
    response = requests.get(urun_linki)
    soup = BeautifulSoup(response.text, "html.parser")

    urun_adi = soup.find("h1", class_="product-name").text.strip()
    urun_fotografi = soup.find("img", class_="product-image").get("src")
    urun_fiyati = soup.find("span", class_="product-price").text.strip()
    urun_yorum_sayisi = len(soup.find_all("div", class_="comment"))
    urun_degerlendirme_sayisi = len(soup.find_all("div", class_="rating"))

    return urun_adi, urun_fotografi, urun_fiyati, urun_yorum_sayisi, urun_degerlendirme_sayisi

def en_ucuz_listelenmis_5_urun():
    # En ucuz listelenmiş ilk 5 ürünü getir
    # Kodu buraya yazın
    pass

def en_pahali_listelenmis_5_urun():
    # En pahalı listelenmiş ilk 5 ürünü getir
    # Kodu buraya yazın
    pass

def en_cok_yorum_alan_5_urun():
    # En çok yorum almış ilk 5 ürünü getir
    # Kodu buraya yazın
    pass

def en_cok_yorum_alan_ve_en_ucuz_urun():
    # En çok yorum almış ve en ucuz ürünü getir
    # Kodu buraya yazın
    pass

def en_cok_yorum_alan_ve_en_pahali_urun():
    # En çok yorum almış ve en pahalı ürünü getir
    # Kodu buraya yazın
    pass

# Kullanıcıdan ürün linkini al
urun_linki = input("İlk ürün linkini girin: ")

# Ürün bilgilerini çekme ve listeleme
urun_adi, urun_fotografi, urun_fiyati, urun_yorum_sayisi, urun_degerlendirme_sayisi = urun_bilgilerini_cek(urun_linki)

print("Ürünün adı:", urun_adi)
print("Ürünün Fotoğraf Linki:", urun_fotografi)
print("Ürünün fiyatı:", urun_fiyati)
print("Ürüne kaç adet yorum yapılmış:", urun_yorum_sayisi)
print("Ürün kaç değerlendirme almış:", urun_degerlendirme_sayisi)

# Kullanıcıya sorular sor
secim = input("Seçiminizi yapın (1-5): ")

# Seçime göre işlem yap
if secim == "1":
    en_ucuz_listelenmis_5_urun()
elif secim == "2":
    en_pahali_listelenmis_5_urun()
elif secim == "3":
    en_cok_yorum_alan_5_urun()
elif secim == "4":
    en_cok_yorum_alan_ve_en_ucuz_urun()
elif secim == "5":
    en_cok_yorum_alan_ve_en_pahali_urun()

# Seçilen ürünün linkini ekrana yazdır
print("Seçtiğiniz ürünün linki: ", urun_linki)
