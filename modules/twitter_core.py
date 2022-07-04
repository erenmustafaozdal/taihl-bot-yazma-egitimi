from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


# twitter'a giriş yap
def login(tarayici, bekle, kisa_bekle, kullanici_adi, sifre):
    tarayici.get("https://twitter.com/i/flow/login")
    bekle.until(ec.visibility_of_element_located(
        (By.NAME, "text")
    )).send_keys(kullanici_adi)
    tarayici.find_element(By.XPATH, "//div[@role='button' and normalize-space()='İleri']").click()
    bekle.until(ec.visibility_of_element_located(
        (By.NAME, "password")
    )).send_keys(sifre)
    tarayici.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']").click()

    kod_kontrol(tarayici, kisa_bekle)
    hata_sayfasini_gec(tarayici, kisa_bekle)


# Kod alanı geldi mi?
def kod_kontrol(tarayici, kisa_bekle):
    try:
        eleman = kisa_bekle.until(ec.visibility_of_element_located(
            (By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']")
        ))
        tarayici.minimize_window()
        kod = input("Kodu Yazın: ")
        tarayici.maximize_window()
        eleman.send_keys(kod)
        tarayici.find_element(By.XPATH, "//div[@role='button' and normalize-space()='İleri']").click()
    except:
        pass

# eğer gelirse hata sayfasını geç
def hata_sayfasini_gec(tarayici, kisa_bekle):
    while True:
        try:
            kisa_bekle.until(ec.visibility_of_element_located(
                (By.XPATH, "//span[text()='Hata']")
            ))
            tarayici.find_element(By.XPATH, "//div[@role='button' and normalize-space()='Yenile']").click()
        except:
            break
