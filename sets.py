"""
✔ sets listeleri süslü parantezler '{}' içinde tanımlanır
✔ sets listelerine indeks numaraları ile ulaşılamaz
✔ sets liste elemanlarına döngü içinde ulaşılır
✔ sets listeleri sıralanamaz
✔ sets listeleri içinde aynı eleman birden fazla yer alamaz (*)
"""

# sets listesi oluşturalım
sets_liste = {1, 2, 3, 4}
# print(sets_liste)
# print(type(sets_liste))

# sets listesinin içindeki bir elemana ulaşalım
# print(sets_liste[0])  # hata

# sets listesinin içindeki elemanlara döngü ile ulaşalım
# for x in sets_liste:
#     print(x)

# sets listesine bir eleman ekleyelim
# print("önce: ", sets_liste)
# sets_liste.add(5)
# print("sonra: ", sets_liste)

# sets listesine bir veya birden fazla eleman ekleyelim
sets_liste.update([9, 15, 13])
sets_liste.update([9, 15, 13])  # aynıları olduğu için ekleme yapmıyor
# print(sets_liste)

# sets listesinden bir eleman silelim
sets_liste.remove(2)
# print(sets_liste)

# sets listesini temizleyelim
sets_liste.clear()
# print(sets_liste)

# tekrarlayan verilerin yer aldığı bir listeyi sets listesine çevirelim
liste = [1, 1, 3, 8, 1, 16, 16, 1, 3]
sets_liste2 = set(liste)
print(sets_liste2)
