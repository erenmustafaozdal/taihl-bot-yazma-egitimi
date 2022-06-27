"""
Dictionary veri tipinde "anahtar", "değer" ikilileri vardır
    66 => Eren
    75 => Mustafa
"""

# Belirli bir numaraya sahip öğrenciyi bulma
# işlemini liste ile yapalım
# numaralar = [66, 75]
# isimler = ["Eren", "Mustafa"]
# numara = int(input("Öğrenci No: "))
# index = numaralar.index(numara)  # arama yapıyoruz
# print(f"{numara} nolu öğrenci: {isimler[index]}")

# Belirli bir numaraya sahip öğrenciyi bulma
# işlemini dictionary ile yapalım
ogrenciler = {66: "Eren", 75: "Mustafa"}
# numara = int(input("Öğrenci No: "))
# print(f"{numara} nolu öğrenci: {ogrenciler[numara]}")

# dictionary verisini ekrana yazdıralım
# print(ogrenciler)
# print(type(ogrenciler))

# Detaylı Örnek
ogrenciler2 = {
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
print(ogrenciler2[66])  # Eren öğrencisini döndürür
print(ogrenciler2[66]["dersler"])  # Eren'in derslerini döndürür
