import time
import os
import glob
def download_wait():
    download_path = f"{os.path.expanduser('~')}/downloads"
    dl_wait = True
    while dl_wait:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(download_path):
            if fname.endswith('.crdownload'):
                dl_wait = True

    dosyalar = glob.glob(download_path + "/*")
    return max(dosyalar, key=os.path.getctime)
