"""
DRY = don't repeat yourself

Yazdığımız yazılım büyüdükçe karmaşıklaşır. Bu sebeple yazılımımızı anlamlı
parçalara (modüllere) ayırmamız gerekir. Her bir modül kendi sorumluluğundaki
işi yapmakla görevli yazılım parçasıdır.

1. Hazır modüller
    1.1. Standart Python modülleri
    1.2. Üçüncü parti modüller
2. Kendi yazdığımız modüller

PYTHON MODÜL HAVUZU
3. parti modüller aşağıdaki havuzdan bulunabilir. 'pip install modul_adi'
şeklinde sistem içine yüklenir.
https://pypi.org
"""

# STANDART PYTHON MODUL ÖRNEĞİ
import random

# dir fonksiyonu ile içeriğine bakalım
# print(dir(random))

# rastgele sayı üretelim
# print(random.randint(1, 100))

# seçenekler arasından rastgele seçim yaptıralım
# egitimler = ["Bot Yazma Eğitmi", "Yapay Zeka Eğitmi", "Excel Eğitimi"]
# print(random.choice(egitimler))

# 3. Parti modül kullanımında birazdan selenium kullanacağız

# Kendi nesnemizi oluşturalım
class Ogrenci:
    okul = "Teknoloji Anadolu İmam Hatip Lisesi"

    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad

    def ad_soyad(self):
        return f"{self.ad} {self.soyad}"


ahmet = Ogrenci("Ahmet", "Yılmaz")
eren = Ogrenci("Eren", "Özdal")

print(ahmet.ad_soyad())
print(eren.ad_soyad())
print(eren.okul)
