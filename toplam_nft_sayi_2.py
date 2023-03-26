import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from renkler import bcolors


def gg(driver):
    def sayfa_asagi(kac_kere):
        for ii in range(0,kac_kere):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

    nft_asset="https://www.binance.com/en/nft/profile/catwomen-0c22fd6bd8f4af395da3f903a83a76d2"

    #driver.execute_script("window.open('');")
    #driver.switch_to.window(driver.window_handles[0])

    driver.get(nft_asset)
    sayfa_asagi(5)
    time.sleep(1)
    dict1={}
    nft_sayilari=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-75hexo"))
    nft_gurup_isimleri=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-11iyu7"))
    listelenmis_nft_sayilari=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-yf51xf"))
    toplam_sayi=0
    listelenmis_toplam_sayi=0
    for ii,aa in enumerate(nft_sayilari):
        #print(nft_gurup_isimleri[ii].text," = ",aa.text , "adet toplam")
        dict1[nft_gurup_isimleri[ii].text]=int(aa.text)
        toplam_sayi=toplam_sayi+int(aa.text)
    for bb in listelenmis_nft_sayilari:
        listelenmis_toplam_sayi=listelenmis_toplam_sayi+int(bb.text)

    print(bcolors.IBlue,"**********************************************************",bcolors.ENDC)
    print(bcolors.IRed,"toplam_sayi = ",toplam_sayi,bcolors.ENDC)
    print(bcolors.IBlue,"listelenmis_toplam_sayi = ",listelenmis_toplam_sayi,bcolors.ENDC)
    print(bcolors.IBlue,"**********************************************************",bcolors.ENDC)
    print(bcolors.OKGREEN,dict1,bcolors.ENDC)
    print(bcolors.IBlue,"**********************************************************",bcolors.ENDC)
    print(bcolors.IPurple,max(dict1, key=dict1.get), f"  {dict1[max(dict1, key=dict1.get)]}",bcolors.ENDC)


