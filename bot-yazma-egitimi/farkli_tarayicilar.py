from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Firefox çalıştır
# webdriver.Firefox(executable_path="C:/Users/erenMustafaOzdal/Downloads/geckodriver.exe")

# Chrome çalıştır
# webdriver.Chrome(executable_path="C:/Users/erenMustafaOzdal/Downloads/chromedriver.exe")

# Web Driver Manager ile tarayıcı çalıştıralım
webdriver.Chrome(ChromeDriverManager().install())
