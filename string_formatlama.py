# Değişkenler oluşturalım
ad = "Eren Mustafa"
soyad = "Özdal"
yas = "36"

# Değişkenlerdeki bilgileri birleştirelim
# print("Adınız: " + ad + ", Soyadınız: " + soyad + ", Yaşınız: " + yas)
# print("Adınız: " + ad + "\nSoyadınız: " + soyad + "\nYaşınız: " + yas)

# print("Adınız: {}, Soyadınız: {}, Yaşınız: {}".format(ad, soyad, yas))
# print("Adınız: {2}, Soyadınız: {0}, Yaşınız: {1}".format(ad, soyad, yas))
# print("Adınız: {x}, Soyadınız: {y}, Yaşınız: {z}".format(x=ad, y=soyad, z=yas))

# f string ile formatlama
# print(f"Adınız: {ad}, Soyadınız: {soyad}, Yaşınız: {yas}")

# UYGULAMA
ders = "Bot Yazma Eğitimi"

# 1. Bot kelimesini ekrana yazalım
# print(ders[0:3])

# 2. Eğitim kelimesini ekrana yazalım
# print(ders[10:])
# print(ders[10:-1])
# print(ders[10:16])


# 3. Bütün yazıyı tersten yazalım
print(ders[::-1])
print(ders[::2])
print(ders[::-2])



