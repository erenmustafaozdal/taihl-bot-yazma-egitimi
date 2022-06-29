liste = [1, 2, 3]
tuple_liste = ("bir", "iki", "üç")

# print(liste)
# print(type(liste))
# print(tuple_liste)
# print(type(tuple_liste))

# tuple'ın belirli sıradaki elemanına ulaşalım
# print(tuple_liste[1])

# tuple'ın eleman sayısını alalım
# print(len(tuple_liste))

# liste'nin bir elemanını değiştirelim
# print(liste[0])
# liste[0] = 4
# print(liste[0])

# tuple'ın bir elemanını değiştirelim
# print(tuple_liste[0])
# tuple_liste[0] = "dört"
# print(tuple_liste[0])

# tuple içinde bir değerin kaç defa olduğuna bakalım
tuple_liste2 = ("bir", "iki", "üç", "iki")
# print(tuple_liste2.count("iki"))

# tuple içindeki belirli bir değerin index numarasını alalım
# print(liste.index(2))
# print(tuple_liste.index("üç"))

# iki tuple'ı birleştirelim
tuple1 = (1, 2, 3)
tuple2 = "bir", "iki", "üç"
tuple3 = tuple1 + tuple2
print(tuple3)
