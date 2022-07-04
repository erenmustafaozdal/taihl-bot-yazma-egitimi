import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.linkedin.com/"
driver.get(url)

driver.maximize_window()
oturum_ac  = driver.find_element_by_xpath("/html/body/nav/div/a[2]")
oturum_ac.click()
time.sleep(1)

user_name = driver.find_element_by_name("session_key")
password = driver.find_element_by_name("session_password")

user_name.send_keys("kullanıcıadı")
password.send_keys("şifre")

login = driver.find_element_by_xpath("/html/body/div/main/div[2]/div[1]/form/div[3]/button")
login.click()
time.sleep(1)

profil  = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div/div/div[1]/div[1]/a/div[2]")
profil.click()

time.sleep(5)
driver.close()