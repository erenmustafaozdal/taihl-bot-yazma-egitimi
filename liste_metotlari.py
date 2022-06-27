sayilar = [9, 12, 85, 3, 16, 34, 42, 99]
harfler = ["t", "c", "a", "f", "y", "m", "s"]

# listenin eleman sayısını bulalım
# print("sayilar: ", len(sayilar))
# print("harfler: ", len(harfler))

# en büyük değerli elemanı bulalım
# print("sayilar: ", max(sayilar))
# print("harfler: ", max(harfler))
# sayılar integer olduğu için karşılaştırma yapamadı.
# Sayılar string'e dönüştüğünde önde yer alıyor.
# print(max(sayilar + harfler))

# listenin sonuna eleman ekleyelim
sayilar.append(0)
# sayilar.append("Eren")  # altta sıralama esnasında hataya sebep oluyor
# print(sayilar)

# listenin istediğimiz konumuna eleman ekleyelim
harfler.insert(3, "b")
# print(harfler)

# listenin sonuncu elemanını silelim
harfler.pop()
# print(harfler)

# listenin belirli bir konumundaki elemanı silelim
harfler.pop(3)
# print(harfler)

# belirli bir değere sahip elemanları silelim
harfler.remove("f")
harfler.append("y")  # ['t', 'c', 'a', 'y', 'm', 'y']
harfler.remove("y")
# print(harfler)

# listedeki elemanları sıralayalım
# print(sayilar)
# sayilar.sort()
# print(sayilar)
# print("-"*50)
# print(harfler)
# harfler.sort()
# print(harfler)

# listedeki elemanları ters sıralayalım
# print(sayilar)
# sayilar.sort()  # küçükten büyüğe sırala
# sayilar.reverse()  # ters çevir (üstteki satır sayesinde büyükten küçüğe olacak)
# print(sayilar)

# liste içinde bir değerin kaç defa olduğunu bulalım
harfler2 = ["t", "c", "a", "f", "c", "y", "m", "s", "c"]
# print(harfler2.count("c"))

# listeyi temizleyelim
print(harfler2)
harfler2.clear()
print(harfler2)
