from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def resimleri_al(tarayici: WebDriver):
    resim_yollari = []

    tarayici.maximize_window()
    tarayici.get("https://www.gratis.com/katalog?k=gratis%20katalog&gclid=CjwKCAjwwo"
                 "-WBhAMEiwAV4dybWIU9qHGXWe2Nus5SjtDMJrSQR4lfPDJzFBe7KyoShrDMFPhGBLerRoCeWwQAvD_BwE&gclsrc=aw.ds")

    sleep(7)

    tarayici.find_element(By.XPATH, '//a[@data-href="download_pdf"]').click()

    sleep(2)



    return resim_yollari
