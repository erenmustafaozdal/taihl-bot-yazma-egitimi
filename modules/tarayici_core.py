from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from settings import driver_yolu, hangi_driver, gizli_mi

# tarayıcı belirlenir ve çalıştırılır
def tarayiciyi_al():
    if hangi_driver == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = gizli_mi
        tarayici = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=options
        )
    elif hangi_driver == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = gizli_mi
        try:
            tarayici = webdriver.Firefox(
                GeckoDriverManager().install(),
                options=options
            )
        except:
            tarayici = webdriver.Firefox(
                executable_path=driver_yolu,
                options=options
            )
    else:
        print("Yanlış tarayıcı seçtiniz. Lütfen 'chrome' ve 'firefox' "
              "ifadelerinden birini settings.py içindeki 'hangi_driver' "
              "değişkenine aktarın.'")
        exit()

    return tarayici
