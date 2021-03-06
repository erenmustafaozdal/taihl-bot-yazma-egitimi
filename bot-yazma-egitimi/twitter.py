from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from settings import kullanici_adi, sifre, etiket_oncesi
from modules.tarayici_core import tarayiciyi_al
from modules.twitter_core import login
import xlrd
from tqdm import tqdm

gunun_etiketleri = "SurvivorKupası GeriAlınsın #salı Ümraniye #Tozluyaka"

tarayici = tarayiciyi_al()
bekle = WebDriverWait(tarayici, 30)
kisa_bekle = WebDriverWait(tarayici, 3)
tarayici.maximize_window()

# giriş yap
login(tarayici, bekle, kisa_bekle, kullanici_adi, sifre)


def tweetle(tweet, etiket="TeknolojiAihl"):
    tweet = f"{tweet}{etiket_oncesi}#{etiket} {gunun_etiketleri}"

    # tweetle
    while True:
        try:
            # sayfa yüklendi mi
            bekle.until(ec.visibility_of_element_located(
                (By.XPATH, f"//a[@role='link' and @href='/{kullanici_adi}']")
            ))

            tarayici.find_element(By.XPATH, "//div[@class='DraftEditor-root']").click()
            editor = tarayici.find_element(By.XPATH, "//div[contains(@class,'public-DraftEditor-content')]")
            editor.send_keys(tweet)
            eleman = tarayici.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af']")
            tarayici.execute_script("arguments[0].click();", eleman)

            tarayici.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']").click()
            break
        except:
            tarayici.refresh()
            sleep(3)

    sleep(3)

    # etiket sayfasına git
    tarayici.get(f"https://twitter.com/hashtag/{etiket}?src=hashtag_click&f=live")

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

# Excel'den tweetleri çekip paylaş
wb = xlrd.open_workbook("Tweet_Listesi.xls")
ws = wb.sheet_by_index(0)
satir_sayisi = ws.nrows

for i in range(satir_sayisi):
    tarayici.get("https://twitter.com/home")

    t = ws.cell_value(i, 0)
    tweetle(t)
    print(f"{i+1}. TWEET ATILDI: {t}")

    # bir dakika bekle
    for i in tqdm(range(60)):
        sleep(1)

    print("-"*50)


sleep(3)
tarayici.quit()
