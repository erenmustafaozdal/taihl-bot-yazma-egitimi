from time import sleep
from datetime import date

from selenium.webdriver.common.by import By


def resimleri_al(tarayici):
    resim_yollari = []
    today = date.today()
    tarayici.maximize_window()
    tarayici.get("https://www.bim.com.tr/categories/100/aktuel-urunler.aspx")
    nextweek = tarayici.find_element(By.XPATH, "//div[@class='tabArea']//a[1]").click
    tarayici.find_element(By.CLASS_NAME,"bigArea col-8 col-md-9").click()
    sleep(5)
    resim = f"resimler/bim{today}.png"
    tarayici.find_element(By.CLASS_NAME, "fancybox-image").screenshot(resim)
    return resim_yollari