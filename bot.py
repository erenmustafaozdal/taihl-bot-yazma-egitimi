from modules.tarayici_core import tarayiciyi_al
from modules.a101 import resimleri_al as a101_resimler
from modules.bim import resimleri_al as bim_resimler
from modules.carrefoursa import resimleri_al as carrefoursa_resimler
from modules.gratis import resimleri_al as gratis_resimler
from modules.hakmar import resimleri_al as hakmar_resimler
from modules.sok import resimleri_al as sok_resimler
import os
from settings import bot_token, telegram_chat_id
import telegram

# Klasör yapısını oluşturalım
klasorler = [
    "resimler/a101",
    "resimler/bim",
    "resimler/careefoursa",
    "resimler/gratis",
    "resimler/hakmar",
    "resimler/sok",
]
for klasor in klasorler:
    if not os.path.exists(klasor):
        os.makedirs(klasor)

telegram_bot = telegram.Bot(token=bot_token)

tarayici = tarayiciyi_al()

a101 = a101_resimler(tarayici)
bim = bim_resimler(tarayici)
carrefoursa = carrefoursa_resimler(tarayici)
gratis = gratis_resimler(tarayici)
hakmar = hakmar_resimler(tarayici)
sok = sok_resimler(tarayici)

kataloglar = {
    "a101": a101,
    "bim": bim,
    "carrefoursa": carrefoursa,
    "gratis": gratis,
    "hakmar": hakmar,
    "sok": sok,
}

for market, resimler in kataloglar.items():
    if not resimler:
        continue

    print(f"{market} marketinin kataloğu gönderiliyor.")
    telegram_bot.send_message(telegram_chat_id, f"{market} marketinin gelecek hafta aktüel ürün kataloğu aşağıda")
    for resim in resimler:
        telegram_bot.send_photo(telegram_chat_id, open(resim, 'rb'))
