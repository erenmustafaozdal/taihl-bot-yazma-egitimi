from time import sleep
from datetime import date

from selenium.webdriver.common.by import By


def resimleri_al(tarayici):
    resim_yollari = []
    today = date.today()
    tarayici.maximize_window()
    tarayici.get("https://www.bim.com.tr/categories/100/aktuel-urunler.aspx")
    sleep(5)
    resim = f"resimler/{today}.png"
    tarayici.find_element(By.CLASS_NAME, "row").screenshot(resim)
    return resim_yollari