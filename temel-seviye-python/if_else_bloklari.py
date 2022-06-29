# Kullanıcıdan iki sayı alalım ve bu sayıların
# hangisinin büyük olduğunu ekrana yazdıralım
sayi1 = int(input("1. sayıyı yazını: "))
sayi2 = int(input("2. sayıyı yazını: "))

if sayi1 > sayi2:
    print(f"1. sayı ({sayi1}), 2. sayıdan ({sayi2}) büyüktür.")
else:
    print(f"2. sayı ({sayi2}), 1. sayıdan ({sayi1}) büyüktür.")
