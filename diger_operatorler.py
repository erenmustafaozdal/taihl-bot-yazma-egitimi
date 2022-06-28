"""
DİĞER OPERATÖRLER
//////////////////////////////////////////////////////////////////////////////

+----------+------------------+-----------+
| Operatör | Açıklama         | Kullanımı |
+----------+------------------+-----------+
| is       | kimlik operatörü | x is y    |
+----------+------------------+-----------+
| in       | üyelik operatörü | "a" in x  |
+----------+------------------+-----------+

"""

# 3 adet değişken oluşturalım
# a = b = [1, 2, 3]
# c = [1, 2, 3]
x = [1, 2, 3]
a = b = x
c = x

# Değişkenlerin değer eşitliği (==) ve
# kimlik eşitliği (is) kontrollerini yapalım
# İS
# print("a == b: ", a == b)  # True
# print("a == c: ", a == c)  # True
# print("a is b: ", a is b)  # True
# print("a is c: ", a is c)  #

# IN
print(1 in x)  # True
print(4 in x)  # False
