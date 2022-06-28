# Öğrenci isimlerinden oluşan bir değişken tanımlayalım
ogrenciler = ["Eren", "Mustafa", "Zeynep"]

# Her bir öğrenciyi ekrana yazdıralım
# for ogrenci in ogrenciler:
#     print(ogrenci)

# listenin içinde ikili elemanlar barındıran tuple'lar olsun
sayilar = [(1, 2), (3, 4), (5, 6)]
# for a, b in sayilar:
#     print(f"a+b = {a+b}")

# string bir ifadenin döngüye alınması
egitim = "Bot Yazma Eğitimi"
# for k in egitim:
#     print(k)

# dict veri tipini döngüye alalım
ogrenciler = {
    66: {
        "ad": "Eren",
        "soyad": "Özdal",
        "cinsiyet": True,
        "dersler": ["Matematik", "Fen Bilimleri"]
    },
    75: {
        "ad": "Zeynep",
        "soyad": "Özdal",
        "cinsiyet": False,
        "dersler": ["Türkçe", "İngilizce"]
    }
}
# for no in ogrenciler.keys():
#     print("no:", no)
#     print("Ad:", ogrenciler[no]["ad"])

for no, bilgiler in ogrenciler.items():
    print(f"{no} nolu {bilgiler['ad']} isimli öğrencinin dersleri: {', '.join(bilgiler['dersler'])}")
