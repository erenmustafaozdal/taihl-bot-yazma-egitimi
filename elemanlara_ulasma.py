"""
find_element() veya find_elements():  sayfa elemanlarını bulup işlemler yapacağız

KULLANIMI
-----------------
from selenium.webdriver.common.by import By
tarayici.find_element(By.CLASS_NAME, "element_class")
"""

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = "C:\\Users\\erenMustafaOzdal\\.wdm\\drivers\\geckodriver\\win64\\v0.31.0\\geckodriver.exe"
tarayici = webdriver.Firefox(executable_path=driver)
tarayici.maximize_window()
tarayici.get("https://www.amazon.com.tr")

# class name ile elemana ulaşma
# 1. arama kutusunu verir
# arama_kutusu = tarayici.find_element(By.CLASS_NAME, "nav-input")
# Bütün arama kutularını döndürür
arama_kutulari = tarayici.find_elements(By.CLASS_NAME, "nav-input")
# # print("arama_kutusu: ", arama_kutusu)
# print("arama_kutulari sayisi: ", len(arama_kutulari))
# print("arama_kutulari: ", arama_kutulari)

# id ile elemana ulaşma (Çerez penceresini kapatıyorz)
tarayici.find_element(By.ID, "sp-cc-accept").click()

# 1.si arama kutusu
arama_kutulari[0].send_keys("Bluetooth kulaklık")
# 2.si arama tuşu
arama_kutulari[1].click()

# name özniteliği ile elemana ulaşma
# arama_kutusu = tarayici.find_element(By.NAME, "field-keywords")
# arama_kutusu.send_keys("Kulaklık")

# bağlantı metni ile elemana ulaşma
# tarayici.find_element(By.LINK_TEXT, "Çok Satanlar").click()

# kısmi bağlantı metni ile elemana ulaşma
# tarayici.find_element(By.PARTIAL_LINK_TEXT, "Ürünlerinizin Reklamını").click()

# etiket adı ile elemana ulaşma
links = tarayici.find_elements(By.TAG_NAME, "a")
# print("Link sayısı:", len(links))
# Sayfa her yüklendiğinde elemanlar yeniden oluştuğu için sıradaki linklere tıklayamayız
# for link in links:
#     try:
#         link.click()
#         sleep(2)
#         tarayici.back()
#         sleep(2)
#     except:
#         pass

# for i in range(len(links)):
#     links = tarayici.find_elements(By.TAG_NAME, "a")
#     try:
#         links[i].click()
#         sleep(2)
#         tarayici.back()
#         sleep(2)
#     except:
#         pass
#
# imgs = tarayici.find_elements(By.TAG_NAME, "img")
# print("Resim sayısı:", len(imgs))

# css seçici ile elemana ulaşma
# cok_satanlar = tarayici.find_elements(By.CSS_SELECTOR, "span[data-a-badge-color='sx-orange']")
# print(len(cok_satanlar))
# i[class='a-icon a-icon-star-small a-star-small-4 aok-align-bottom']
# i.a-icon.a-star-small-4
# dort_yildiz = tarayici.find_elements(By.CSS_SELECTOR, "i[class='a-icon a-icon-star-small a-star-small-4 aok-align-bottom']")
# dort_yildiz = tarayici.find_elements(By.CSS_SELECTOR, "i.a-icon.a-star-small-4")
# print("dört yıldızlı ürün: ", len(dort_yildiz))

# xpath seçici ile elemana ulaşma
# Chrome: //*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[7]/div/div/div/div/div[3]/div[3]/div/a/span/span[2]/span[1] (Ufak değişiklik sonucunda patlar)
# SelectorsHub: //div[@class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_5']//span[@class='a-price-whole'] (Ufak değişiklik sonucunda patlar) (dinamik olma ihtimali var)
# (//span[@class='a-price-whole'])[5]
fiyatlar = tarayici.find_elements(By.XPATH, "//span[@class='a-price-whole']")
for fiyat in fiyatlar:
    text = int(fiyat.text.replace(".", ""))
    if text < 400:
        print(text)


sleep(3)
tarayici.quit()
