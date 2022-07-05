from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

tarayici = webdriver.Chrome(ChromeDriverManager().install())

# İnternet sitesine gidelim
tarayici.get("https://www.youtube.com")

# geçerli adresi alalım
print(tarayici.current_url)
sleep(2)

# Başka bir internet sitesine gidelim
tarayici.get("https://www.amazon.com.tr")

# Sayfa başlığını alalım
print(tarayici.title)
sleep(2)

# önce geri gidelim, sonra ileri gidelim
tarayici.back()
sleep(2)
tarayici.forward()
sleep(2)

# tarayıcıyı kapatalım
tarayici.quit()
