from time import sleep


def resimleri_al(tarayici):

    resim_yollari = []

    # from selenium.webdriver.common.by import By

    tarayici.maximize_window()
    tarayici.get(
        "https://view.publitas.com/72755/1500235/pdfs/b8fd8f3e-0bdb-4cb9-933e-ae1d8b62c485.pdf?response-content"
        "-disposition=attachment%3B+filename%2A%3DUTF-8%27%27GRATIS%2520-%2520TEMMUZ%2520publish.pdf")
    sleep(3)


    return resim_yollari
