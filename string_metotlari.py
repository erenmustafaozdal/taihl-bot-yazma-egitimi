ders = " Bot Yazma Eğitimi "

# Tüm karakterleri büyük yazalım
# print(ders.upper())

# Tüm harfleri küçük yapalım
lower = ders.lower()
# print(lower)

# Her kelimenin ilk harfini büyük yapalım
# print(lower.title())

# Sadece ilk karakteri büyük yazalım
# print(lower.capitalize())

# Belirli bir ifadenin kaç defa geçtiğini bulalım
# print(ders.count("i"))
# print(ders.count(" "))
# print(ders.count("Bot"))

# Soldaki ve sağdaki boşluk karakterlerini temizleyelim
# print(ders + "-")
# print(ders.strip() + "-")

# Soldaki ve sağdaki belirli karakterleri temizleyelim
# print(ders.strip(" Bot"))
ogrenci = "TAİHL - Eren Özdal"
# print(ogrenci.strip("TAİHL - "))

# Soldaki boşluğu temizleyelim
# print(ders)
# print(ders.lstrip() + "-")

# Sağdaki boşluğu temizleyelim
# print(ders + "-")
# print(ders.rstrip() + "-")

# İfadeyi istediğimiz ifadelerle bölelim
# print(ders.split())
# print(ders.split("a"))

# Liste halindeki karakter dizilerini birleştirelim
liste = ders.split()
# print(liste)
# print(" ".join(liste))
# print("-".join(liste))

# Belirli bir genişlik uzunluğundaki bir dizgede ortalanmış dönüş
# ***************      EREN      ********************
print("EREN".center(50, "-"))
