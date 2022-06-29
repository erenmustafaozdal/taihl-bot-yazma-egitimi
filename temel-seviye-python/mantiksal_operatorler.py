"""
MANTIKSAL OPERATÖRLER
//////////////////////////////////////////////////////////////////////////////
Python'da birden fazla koşulu beraber değerlendirmek için kullanırız.

+----------+----------+-----------------+
| Operatör | Açıklama |    Kullanımı    |
+----------+----------+-----------------+
|    and   | ve       | (x<y) and (a>b) |
+----------+----------+-----------------+
|    or    | veya     |  (x<y) or (a>b) |
+----------+----------+-----------------+
|    not   | değil    |    not (x<y)    |
+----------+----------+-----------------+

"""

# Üç değişkeni tek satırda tanımlayalım
x, y, z = 5, 6, 7
# print(x, y, z)

# Mantıksal operatörler işlemi örneği
# AND
# print("x < y", x < y)
# print("z < y", z < y)
# print("x < y and z < y", x < y and z < y)  # False
# print("x < y and y < z", x < y and y < z)  # False

# OR
# print("x < y", x < y)
# print("z < y", z < y)
# print("x < y or z < y", x < y or z < y)

# NOT
print(not(x < y))
