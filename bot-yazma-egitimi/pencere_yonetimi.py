from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

tarayici = webdriver.Chrome(ChromeDriverManager().install())

# Tarayıcı boyutlarını aldık
boyutlar = tarayici.get_window_size()
print("genişlik: ", boyutlar.get("width"))
print("yükseklik: ", boyutlar.get("height"))
sleep(2)

# Tarayıcıya boyut belirleyelim
tarayici.set_window_size(300, 200)

# Tarayıcının pozisyonunu alalım
pozisyon = tarayici.get_window_position()
print("x: ", pozisyon.get("x"))
print("y: ", pozisyon.get("y"))
sleep(2)

# Tarayıcı pozisyonunu ayarlayalım
pozisyonlar = [(0, 0), (500, 250), (400, 600)]
for x, y in pozisyonlar:
    tarayici.set_window_position(x, y)
    sleep(1)

# Büyütelim
tarayici.maximize_window()
sleep(2)

# Küçültelim
tarayici.minimize_window()
sleep(2)

# Tam ekran yapalım
tarayici.fullscreen_window()
sleep(2)

# Ekran görüntüsü alalım.
tarayici.get("https://teknolojiaihl.meb.k12.tr/")
tarayici.maximize_window()
tarayici.save_screenshot("resimler/ekran_goruntusu.png")

sleep(2)
tarayici.quit()
