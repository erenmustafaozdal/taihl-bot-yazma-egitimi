# 0'da 10'a kadar olan sayıları 5 hariç yazalım
# sayi = 0
# for sayi in range(10):
#     if sayi == 5:
#         continue
#
#     print(sayi)

# 0'da 10'a kadar olan sayıları yazdıralım. 5'e gelince duralım
sayi = 0
for sayi in range(10):
    if sayi == 5:
        break

    print(sayi)
