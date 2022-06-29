"""
VALUE VERİ TİPİ (VALUE TYPES)
//////////////////////////////////////////////////////////////////////////////
✔ Verileri kendine ayrılmış bir bellekte tutar.
✔ Değişken doğrudan bir değeri tutar.
✔ Başka bir değişkene atarsanız, değer doğrudan kopyalanır.
    ⚫ İki değişken de bağımsız çalışır.
ÖR: string, int, float, bool

REFERANS VERİ TİPİ (REFERENCE TYPES)
//////////////////////////////////////////////////////////////////////////////
✔ Gerçek verilerin bellekteki konumunu tutar.
✔ Verinin kendisini değil, adresini temsil eder.
✔ Başka bir değişkene atarsanız, veriler kopyalanmaz.
    ⚫ Orijinal verinin adresini başka değişkene atamış olursunuz.
ÖR: list, dict
"""

# VALUE TYPES
# iki value veri tipi oluşturalım
a = 1
b = 2
# ikinci değişkeni ilk değişkene atayalım
a = b
# ikinci değişkeni değiştirelim
b = 3
# print(a, b)


# REFERENCE TYPES
# iki referans veri tipi oluşturalım
x = [1, 2, 3]
y = [4, 5, 6]
# print(x, y)
# ikinci değişkeni ilk değişkene atayalım
x = y
# ikinci değişkeni değiştirelim
y[0] = 7
print(x, y)
