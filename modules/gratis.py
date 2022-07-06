from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from modules.yardimcilar import download_wait, pdf2image
from datetime import date


def resimleri_al(tarayici: WebDriver):
    resim_yollari = []

    tarayici.maximize_window()
    tarayici.get("https://view.publitas.com/gratis")

    bekle = WebDriverWait(tarayici, 30)
    bekle.until(ec.visibility_of_element_located(
        (By.XPATH, '//a[@data-href="download_pdf"]')
    )).click()

    pdf = download_wait()
    resimler = pdf2image(pdf)
    today = date.today()

    for i in range(len(resimler)):
        resim = f"resimler/gratis/{today}-{i}.png"
        resimler[i].save(resim, 'PNG')
        resim_yollari.append(resim)

    return resim_yollari
