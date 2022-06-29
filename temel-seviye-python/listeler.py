# boş liste tanımlayalım -> []
liste = []
# print(liste)
# print(type(liste))

kelimeler = "Teknoloji Anadolu İmam Hatip Lisesi".split()
# print(kelimeler)

# kelimelere tek tek ulaşalım
# print(len(kelimeler))
# print(kelimeler[0])
# print(kelimeler[1])
# print(kelimeler[2])
# print(kelimeler[3])
# print(kelimeler[4])

# Yeni ve karışık verilerden bir liste oluşturalım
liste2 = [42, 65, "Eren", 0.6, True, ["a", "b", "c", [1, 2]]]
# print(liste2)
# print(liste2[5][1])  # b'ye ulaştık
# print(liste2[5][3][1])  # 2'ye ulaştık

# 2 liste tanımlayalım ve onları birleştirelim
liste3 = [1, 2, 3]
liste4 = ["a", "b", "c"]
liste5 = liste3 + liste4
liste6 = liste4 + liste3
print("liste5", liste5)
print("liste6", liste6)
