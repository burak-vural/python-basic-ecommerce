import requests
from bs4 import BeautifulSoup

def get_top_products():
    url = input("İnternet sitesinin linkini girin: ")
    category = input("Kategori girin: ")

    # İnternet sitesine istek gönder
    response = requests.get(url)
    if response.status_code != 200:
        print("Hata: İnternet sitesine erişilemedi.")
        return

    # Sayfanın HTML içeriğini analiz et
    soup = BeautifulSoup(response.content, 'html.parser')

    # Kategoriye göre ürünleri seç
    products = soup.find_all('div', class_='product', attrs={'category': category})

    # Değerlendirme sayılarına göre ürünleri sırala
    sorted_products = sorted(products, key=lambda x: int(x['reviews']), reverse=True)

    # İlk 10 ürünü yazdır
    for i, product in enumerate(sorted_products[:10]):
        name = product.find('h3').text.strip()
        price = product.find('span', class_='price').text.strip()
        reviews = product['reviews']
        link = product.find('a')['href']
        print(f"{i+1}. Ürün: {name}")
        print(f"Fiyat: {price}")
        print(f"Değerlendirme Sayısı: {reviews}")
        print(f"Link: {link}")
        print()

# Fonksiyonu çağır
get_top_products()
