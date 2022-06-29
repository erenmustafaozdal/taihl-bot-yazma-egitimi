# METOT: range()
# liste = list(range(1, 10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# liste = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# liste = list(range(1, 10, 2))  # [1, 3, 5, 7, 9]
# print(liste)

# 100-200 arasındaki çift sayıları ekrana 1 saniye aralıklarla yazalım
# import time
#
# for i in range(100, 200):
#     if i % 2 == 0:
#         print(i)
#         time.sleep(1)


# METOT: enumerate()
kelime = "python"
kelime_enum = list(enumerate(kelime))
# print(kelime_enum)

for i, harf in enumerate(kelime):
    print(i, harf)
