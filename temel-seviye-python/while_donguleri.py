# 0'da 10'a kadar olan sayıları yazalım
# sayi = 0
# while sayi <= 10:
#     print(sayi)
#     sayi += 1

# 1'den 100'e kadar tek ve çift sayıları ekrana yazdıralım
# sayi = 1
# while sayi <= 100:
#     if sayi % 2 == 0:
#         print(f"{sayi}: çift")
#     else:
#         print(f"{sayi}: tek")
#
#     sayi += 1


# Excel'deki verileri okumak için xlrd modülünü kullanacağız
# komut isteminde: pip install xlrd
import xlrd

# Excel dosyasını açalım
ck = xlrd.open_workbook("kitabimi_bitirdim.xlsx")

# Excel çalışma sayfasını alalım
# cs = ck.sheet_by_index(0)  # index ile aldık
cs = ck.sheet_by_name("yanıtlar")  # sayfa adı ile aldık

# satır ve sütun sayısını alalım
toplam_satir = cs.nrows
# print("satır sayısı: ", cs.nrows)
# print("sütun sayısı: ", cs.ncols)

# Öğrenci adı, kitap adı ve sayfa sayısını yazdıralım
satir = 1
toplam_sayfa = 0
while satir < toplam_satir:
    ad = cs.cell_value(satir, 1)
    kitap = cs.cell_value(satir, 2)
    sayfa = int(cs.cell_value(satir, 5))

    print(f"{ad}, {sayfa} sayfalık {kitap} kitabını okudu.")
    toplam_sayfa += sayfa
    satir += 1

print("-"*50)
print(f"Toplam {toplam_sayfa} sayfa kitap okunmuş.")


