from time import sleep
from datetime import date

from selenium.webdriver.common.by import By


def resimleri_al(tarayici):
    resim_yollari = []
    today = date.today()
    tarayici.maximize_window()
    tarayici.get("https://www.bim.com.tr/Categories/680/afisler.aspx")
    sleep(2)
    # çerezleri kabul et
    tarayici.find_element(By.XPATH, "//button[text()='Çerezleri kabul edin']").click()
    tarayici.find_element(By.XPATH, "//a[normalize-space()='GELECEK HAFTA']").click()
    sleep(2)
    fancyboxs = tarayici.find_elements(By.XPATH,"//a[@class='fancyboxImage']")
    fancyboxs[-1].click()
    sleep(2)
    resim_index = 1
    resim = f"resimler/bim/{today}-{resim_index}.png"
    tarayici.find_element(By.CLASS_NAME, "fancybox-image").screenshot(resim)
    resim_yollari.append(resim)
    while True:
        resim_index += 1
        resim = f"resimler/bim/{today}-{resim_index}.png"


        resim_yollari.append(resim)


    return resim_yollari
