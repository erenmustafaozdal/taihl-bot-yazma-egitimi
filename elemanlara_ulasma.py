"""
find_element() veya find_elements():  sayfa elemanlarını bulup işlemler yapacağız

KULLANIMI
-----------------
from selenium.webdriver.common.by import By
tarayici.find_element(By.CLASS_NAME, "element_class")
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

tarayici = webdriver.Chrome(ChromeDriverManager().install())
tarayici.maximize_window()
tarayici.get("https://www.amazon.com.tr")

# class name ile elemana ulaşma
# 1. arama kutusunu verir
# arama_kutusu = tarayici.find_element(By.CLASS_NAME, "nav-input")
# Bütün arama kutularını döndürür
# arama_kutulari = tarayici.find_elements(By.CLASS_NAME, "nav-input")
# # print("arama_kutusu: ", arama_kutusu)
# print("arama_kutulari sayisi: ", len(arama_kutulari))
# print("arama_kutulari: ", arama_kutulari)

# id ile elemana ulaşma (Çerez penceresini kapatıyorz)
tarayici.find_element(By.ID, "sp-cc-accept").click()

# 1.si arama kutusu
# arama_kutulari[0].send_keys("Bluetooth kulaklık")
# 2.si arama tuşu
# arama_kutulari[1].click()

# name özniteliği ile elemana ulaşma
# arama_kutusu = tarayici.find_element(By.NAME, "field-keywords")
# arama_kutusu.send_keys("Kulaklık")

# bağlantı metni ile elemana ulaşma
tarayici.find_element(By.LINK_TEXT, "Çok Satanlar").click()

# kısmi bağlantı metni ile elemana ulaşma

# etiket adı ile elemana ulaşma

# css seçici ile elemana ulaşma

# xpath seçici ile elemana ulaşma


sleep(3)
tarayici.quit()
