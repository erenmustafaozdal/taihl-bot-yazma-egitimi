from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from settings import kullanici_adi, sifre, etiket_oncesi
from modules.tarayici_core import tarayiciyi_al
from modules.twitter_core import login

tarayici = tarayiciyi_al()
bekle = WebDriverWait(tarayici, 30)
kisa_bekle = WebDriverWait(tarayici, 3)
tarayici.maximize_window()


login(tarayici, bekle, kisa_bekle, kullanici_adi, sifre)

tarayici.find_element(By.XPATH, "//div[@aria-label='Fotoğraf veya video ekle']//div[@class='css-901oao r-1awozwy r-1cvl2hr r-6koalj r-18u37").click()