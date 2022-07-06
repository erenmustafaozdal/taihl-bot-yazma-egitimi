from modules.tarayici_core import tarayiciyi_al
from modules.a101 import resimleri_al as a101_resimler
from modules.bim import resimleri_al as bim_resimler
from modules.carrefoursa import resimleri_al as carrefoursa_resimler
from modules.gratis import resimleri_al as gratis_resimler
from modules.hakmar import resimleri_al as hakmar_resimler
from modules.sok import resimleri_al as sok_resimler

tarayici = tarayiciyi_al()

a101 = a101_resimler(tarayici)
bim = bim_resimler(tarayici)
carrefoursa = carrefoursa_resimler(tarayici)
gratis = gratis_resimler(tarayici)
hakmar = hakmar_resimler(tarayici)
sok = sok_resimler(tarayici)

liste = a101 + bim + carrefoursa + gratis + hakmar + sok

for resim in liste:
    print(resim)
