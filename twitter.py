from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from settings import kullanici_adi, sifre
import random

driver = "C:\\Users\\erenMustafaOzdal\\.wdm\\drivers\\geckodriver\\win64\\v0.31.0\\geckodriver.exe"
tarayici = webdriver.Firefox(executable_path=driver)
tarayici.maximize_window()
tarayici.get("https://twitter.com/i/flow/login")

bekle = WebDriverWait(tarayici, 30)
kisa_bekle = WebDriverWait(tarayici, 3)

# giriş yap
bekle.until(ec.visibility_of_element_located(
    (By.NAME, "text")
)).send_keys(kullanici_adi)
tarayici.find_element(By.XPATH, "//div[@role='button' and normalize-space()='İleri']").click()
bekle.until(ec.visibility_of_element_located(
    (By.NAME, "password")
)).send_keys(sifre)
tarayici.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']").click()

# Kod alanı geldi mi?
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

# hata sayfası mı geldi
while True:
    try:
        kisa_bekle.until(ec.visibility_of_element_located(
            (By.XPATH, "//span[text()='Hata']")
        ))
        tarayici.find_element(By.XPATH, "//div[@role='button' and normalize-space()='Yenile']").click()
    except:
        break


def tweetle(tweet, etiket="SancaktepeTeknolojiAihl"):
    tweet = f"{tweet}\n#{etiket}"

    # sayfa yüklendi mi
    bekle.until(ec.visibility_of_element_located(
        (By.XPATH, f"//a[@role='link' and @href='/{kullanici_adi}']")
    ))

    # tweetle
    tarayici.find_element(By.XPATH, "//div[@class='DraftEditor-root']").click()
    editor = tarayici.find_element(By.XPATH, "//div[contains(@class,'public-DraftEditor-content')]")
    editor.send_keys(tweet)
    tarayici.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af']").click()

    tarayici.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']").click()

    sleep(3)

    # etiket sayfasına git
    tarayici.get(f"https://twitter.com/hashtag/{etiket}?src=hashtag_click")

    try:
        retweets = kisa_bekle.until(ec.visibility_of_all_elements_located(
            (By.XPATH, '//div[@role="button" and contains(@aria-label,"Retweet") and not(contains(@aria-label,"retweetledi"))]')
        ))
    except:
        return

    for retweet in retweets:
        retweet.click()
        bekle.until(ec.visibility_of_element_located(
            (By.XPATH, '//div[@role="menuitem" and normalize-space()="Retweet"]')
        )).click()


tweets = [
    "Adımız duyualacak!",
    "Bot yazıyoruz!",
    "Bot yazarak tarayıcımızda otomatik işlemler yapıyoruz. Bu tweet gibi 😎!",
    "Selim Hoca kraldır.",
    "Bir sabah gelecek kardan aydınlık",
    "Menemen soğansız olmaz.",
    "\"Baban da mı botçuydu!\"",
    "Toprağım sıkıntı yok.",
    "Herkes bilecek.",
    "Menemen yumurtasız da olmaz",
    "biz bot yazdık la",
    "Ağzını kırarım bebe!",
    "Ömer zafer müdür yardımcısı olsun",
    "\"Ya ben İstanbulu alacağım yada o beni\"",
    "Bu gün hashtag biziz",
    "Aynen kardeşim Aras kargo",
    "Toroslar şehirde",
    "ilim akılla iman irade ile olur",
    "İhanetin nedeni olmaz, bedeli olur",
    "Sadece ölüler görür",
]

tweet_sayisi = 10

for i in range(tweet_sayisi):
    tarayici.get("https://twitter.com/home")

    t = random.choice(tweets)
    tweetle(t)

    # bir dakika bekle
    sleep(10)


sleep(3)
tarayici.quit()
