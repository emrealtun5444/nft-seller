from selenium import webdriver
import random
import time
from datetime import datetime, timedelta
from importlib import reload
# from minimum_fiyat import telegram_bot_sendtext,fiyat_al
from itertools import cycle

import pandas as pd
import pause
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from renkler import bcolors
from token_id_link_listesi import liste_125_uzeri, liste_130_uzeri, liste_140_uzeri, liste_150_uzeri, liste_160_uzeri, \
    liste_ozel

########################################################################
myIterator = cycle(range(3))
########################################################################
bb_saat=0
b_dakika=0
gurp_sayi=60
gurup_dakika=1
bekle_sure_nft_sayisi_az=60*10
###############  manul Baslamak icin Bekleme Suresi  ###################
bekleme=datetime.now()+timedelta(hours=bb_saat,minutes=b_dakika)
#######################################################################

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--user-data-dir=~/Library/Application Support/Google/Chrome/Profile 1")
chrome_options.add_argument('--disable-extensions')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.set_page_load_timeout(10)
wait = WebDriverWait(driver, 20)
########################################################################
def rand_zaman():
    rand_bekleme=0.0
    rand1 = random.randint(500,700)
    rand_bekleme=rand1/1000
    return rand_bekleme
########################################################################
"""fiyatlar belirleme"""
def fiyat_isim_token_id(isim,token_id):
    if token_id in liste_ozel:
        return "6.9"
    if token_id in liste_160_uzeri:
        return "5.9"
    if token_id in liste_150_uzeri:
        return "4.9"
    if token_id in liste_140_uzeri:
        return "3.39"
    if token_id in liste_130_uzeri:
        return "2.39"
    if token_id in liste_125_uzeri:
        return "2.19"
    return fiyat_listesi(isim)
##############################################################################################

login_1="https://accounts.binance.com/en/login"
nft_asset="https://www.binance.com/en/nft/my-nfts/collected/digitialman-248d0a068cf0360878e974bb4ea03b4e"

###########  login yapmak icin sayfa ac ve tusa basilmasini bekle #####
driver.get(login_1)
print(bcolors.IBlue,"-------------------------BULENT----------------------------",bcolors.ENDC)
print(bcolors.IBlue,"-----------------------------------------------------------",bcolors.ENDC)
print(bcolors.IBlue,"-----------------------------------------------------------",bcolors.ENDC)
keyword = input("**** DEVAM icin bir tusa BAS ****")
########################################################################
print(bcolors.IPurple," ---- > bekleme süresi basladi  ---- >",bekleme,bcolors.ENDC)
pause.until(bekleme)
print("bekleme süresi bitti")
########################################################################
"""driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[0])"""
########################################################################
"""degiskenler"""
nft_listem=[]
hata_yenileme_sayi=0
hata_yenileme_sayi_ilk_nft=0
nft_id_bir_onceki=""
rechapta_sayi=0
listeleme_toplam_sure=0
########################################################################
dosya_tarih = time.strftime("%m%d-%H%M")
########################################################################

for xx in range(0,50):
    for aa in range(0,gurp_sayi):

        import fiyat
        fiyat = reload(fiyat)
        from fiyat import fiyat_listesi11 as fiyat_listesi
        import minimum_fiyat_satin_al_7
        minimum_fiyat_satin_al_7=reload(minimum_fiyat_satin_al_7)
        from minimum_fiyat_satin_al_7 import fiyat_ara_satin_al

        print(bcolors.IBlue,"-bulent----------------------------------------------------------------",bcolors.ENDC)
        print(bcolors.ICyan,"listelenmiş toplam sayi = ",bcolors.ENDC,bcolors.IYellow,len(nft_listem),bcolors.ENDC)
        start = time.time()
        tarih_al=datetime.now()+timedelta(hours=12,minutes=3)
        tarih_formatli=datetime.strftime(tarih_al,"%Y/%m/%d %H:%M:%S")
        tarih=tarih_formatli
        fiyat_arastirma_yap=False
        if minimum_fiyat_satin_al_7.fiyat_arastirmasi_yap_ben == 1:
            if len(nft_listem) % 10 == 0:
                print(bcolors.IPurple,"--------------Fiyat Arastirmasi Basla------------",bcolors.ENDC)
                fiyat_ara_satin_al(driver,0)
                print("toplam_alinan",minimum_fiyat_satin_al_7.toplam_alinan)
                print(bcolors.IPurple,"--------------Fiyat Arastirmasi SON-------------",bcolors.ENDC)
        while True:
            ##############################################################################################
            try:
                driver.get(nft_asset)
                time.sleep(rand_zaman())
                driver.execute_script("window.scrollTo(0, 300);")
                time.sleep(rand_zaman()+1)
            except Exception as hata:
                print(bcolors.IRed,"hata  -> driver.get(nft_asset) ",bcolors.ENDC)
                time.sleep(20)
                continue
            try:
                not_listed_box=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-1iztezc"))
                not_listed_box_1=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-1iztezc"))
                time.sleep(rand_zaman())
            except Exception as hata:
                print(bcolors.IRed,"hata not_listed_box find",bcolors.ENDC)
                time.sleep(10)
                continue

            try:
                not_listed_box_1=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-1iztezc"))
                not_listed_box_1[3].click()
                time.sleep(rand_zaman())
            except Exception as hata:
                hata_yenileme_sayi=hata_yenileme_sayi+1
                print(bcolors.IRed,"hata not_listed_box_click = ",hata_yenileme_sayi,bcolors.ENDC)
                driver.get(nft_asset)
                bekleme11=datetime.now()+timedelta(hours=0,minutes=0,seconds=10)
                pause.until(bekleme11)
                continue

            ##############################################################################################
            #https://stackoverflow.com/questions/2083987/how-to-retry-after-exception

            try:
                #bir onceki versiyonda direkt list butonun basabiliyorduk
                # burada once ilk nft ye basip sonra list butonuna basiyoruz
                #driver.execute_script("window.scrollTo(0, 200);")
                time.sleep(rand_zaman())
                #driver.execute_script("window.scrollTo(0, -200);")
                ilk_nft=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-2r2ti0"))
                sayfada_listelenecek_nft_sayisi=len(ilk_nft)
                #print("ilk sayfadaki listelenencek nft sayisi = ",sayfada_listelenecek_nft_sayisi)
                if sayfada_listelenecek_nft_sayisi < 4 :
                    print(bcolors.IPurple, str(bekle_sure_nft_sayisi_az)+" saniye ara verildi cunkü listelenecek sayisi 4 un altina indi",bcolors.ENDC)
                    time.sleep(bekle_sure_nft_sayisi_az)
                ilk_nft[0].click()
                time.sleep(rand_zaman())
                #keyword = input("11111111111111")
            except Exception as hata:
                hata_yenileme_sayi_ilk_nft=hata_yenileme_sayi_ilk_nft+1
                print(bcolors.IRed,"hata var ilk_nft kisminda = ",hata_yenileme_sayi_ilk_nft,bcolors.ENDC)
                print(bcolors.IGreen,"listelenmiş toplam sayi = ",len(nft_listem),bcolors.ENDC)
                #winsound.Beep(400, 1000)
                bekleme11=datetime.now()+timedelta(hours=0,minutes=10,seconds=0)
                print(bcolors.IRed,"hatadan beklemeye girdi = ",bekleme11,bcolors.ENDC)
                #pause.until(bekleme11)
                if hata_yenileme_sayi_ilk_nft==100:
                    keyword = input("hata_yenileme_sayi_ilk_nft = "+str(hata_yenileme_sayi_ilk_nft)+" oldu")
                continue


            try:
                isim_bul = WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-1e8252r"))
                isim_text=isim_bul[0]
                isim111=isim_text.text
                print(bcolors.IPurple,"nft ismi = ",bcolors.ENDC,bcolors.IYellow,isim111,bcolors.ENDC,end =" ")
            except Exception as hata:
                print(bcolors.IRed,"isim_bul da hata var, 5 sn ara",bcolors.ENDC)
                time.sleep(5)
                continue #how-to-retry-after-exception
            ##############################################################################################
            # yeni details tikla
            try:
                # details farklı nftlerde farklı. bazılarında ek bilgiler var
                # o yuzden bulmam zor oldu cözümü
                # detailse tıklamamın amcaı tokenid yi alabilmek.
                # token id ye gore kız kartlarının fiyatı belirleniyor
                driver.execute_script("window.scrollTo(0, 300);")
                time.sleep(1)
                details=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-g30str"))

                if len(details)==4:
                    print("tiklama")
                if len(details)==5:
                    details[1].click()
                    details[1].click()
                if len(details)==6:
                    details[2].click()

            except Exception as hata:
                print(bcolors.IRed,"details hata var",bcolors.ENDC)
                time.sleep(10)
                continue
                ##############################################################################################
            # token id
            try:
                # tokenid numarası aslında benim için gerekli ama
                # farklı nftlerde yeri degisişik olduğu icin hatalı oluyordu
                # o yüzden aldığım bilginin textinin "token id" stringi olduğunu
                # kontrol edip ona göre token id numarasını alıyorum
                #css-pqo48b
                #css-1xjvxb2
                #css-1xjvxb2
                token_id_number=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-pqo48b"))
                token_id_text=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-1xjvxb2"))

                token_id_number_txt=token_id_number[5].text
                token_id_name_txt=token_id_text[5].text

                if token_id_name_txt != "Token ID" :
                    token_id_number_txt=token_id_number[4].text
                    token_id_name_txt=token_id_text[4].text
                    if token_id_name_txt != "Token ID" :
                        print(bcolors.IPurple,token_id_name_txt,"=",bcolors.ENDC,token_id_number_txt)
                        input("token id de problem var, tusa basılması bekleniyor")
                print(bcolors.IPurple,token_id_name_txt,"=",bcolors.ENDC,token_id_number_txt)
                nft_url=driver.current_url

            except Exception as hata:
                print(hata)
                print(bcolors.IRed,"token_id de hata var",bcolors.ENDC)
                input("token id de problem var, tusa basın")
                continue
            ##############################################################################################
            # rechapta kontrolu
            if token_id_number_txt==nft_id_bir_onceki:
                rechapta_sayi=rechapta_sayi+1
                print(bcolors.IRed,"rechapta VAR, sayisi = ",rechapta_sayi,bcolors.ENDC)
                #keyword = input("rechapta VAR tusa bas")
            else:
                nft_id_bir_onceki=token_id_number_txt
                #print("rechapta YOK")
            if rechapta_sayi==10:
                rechapta_sayi=0
                print(bcolors.IRed,"rechapta dan dolayi beklemeye gir = 5 sn",bcolors.ENDC)
                time.sleep(15)
                continue
                ##############################################################################################
            # nft sayfasindaki list butonu
            try:
                driver.execute_script("window.scrollTo(0, -200);")
                list_buton=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-1py3v1y"))
                time.sleep(rand_zaman())

                list_buton[0].click()
            except Exception as hata:
                print("hata list buton",hata)
                time.sleep(10)
                continue
            #############################################################################################
            try:
                busd_menu = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CLASS_NAME,"css-1t72ivm"))
                )
                busd_menu.click()
                time.sleep(rand_zaman())
            except Exception as hata:
                print(bcolors.IRed,"busd_menu hata var",bcolors.ENDC)
                time.sleep(5)
                continue
            ##############################################################################################
            try:
                busd_secim= WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.ID,"BUSD"))
                )
                busd_secim.click()
                time.sleep(rand_zaman())
            except Exception as hata:
                print(bcolors.IRed,"busd_secim hata",bcolors.ENDC)
                time.sleep(5)
                continue
            ##############################################################################################
            try:
                deg3="css-16fg16t"
                fiyat_yazilacak_kutu =WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,deg3))
            except Exception as hata:
                print(bcolors.IRed,"fiyat_yazilacak_kutu hata var",bcolors.ENDC)
                time.sleep(10)
                continue
            ##############################################################################################
            # fiyat yazılacak kutuya tıkla
            try:
                time.sleep(rand_zaman())
                fiyat_yazilacak_kutu[1].click()
            except Exception as hata:
                print("fiyat yazilacak kutu click hata")
                time.sleep(10)
                continue
            ##############################################################################################
            # fiyatı fonksiyondan al
            # kutuya yaz. copy past ten "Keys.CONTROL, 'v'" vazgectim caliyor gibi bu halide
            try:
                fiyat_txt= fiyat_isim_token_id(isim111,token_id_number_txt)
                #pyperclip.copy(fiyat_txt)
                #fiyat_yazilacak_kutu[1].send_keys(Keys.CONTROL, 'v')
                fiyat_yazilacak_kutu[1].send_keys(fiyat_txt)
                time.sleep(rand_zaman())
            except Exception as hata:
                print(hata)
                time.sleep(5)
                continue
            ##############################################################################################
            #tarih kutusunu bulma
            try:
                time.sleep(rand_zaman())
                css1="div.rc-picker-input:nth-child(3) > input:nth-child(1)"
                tarih_kutusu= WebDriverWait(driver,20).until(lambda driver: driver.find_element(By.CSS_SELECTOR,css1))
            except Exception as hata:
                print("tarihi kutusu bulma hata")
                time.sleep(10)
                continue
                ##############################################################################################
            # tarih kutusunu tıklama
            try:
                time.sleep(rand_zaman())
                tarih_kutusu.click()
            except Exception as hata:
                print("tarih_kutusu  click hata var")
                time.sleep(10)
                continue
            ########################################################################################
            # oniki saat butonunu bulma
            try:
                time.sleep(rand_zaman())
                onikisaat_3 = WebDriverWait(driver,20).until(lambda driver: driver.find_element(By.CSS_SELECTOR,"div.css-1kxmfj1:nth-child(1)"))
            except Exception as hata:
                print("hata onikisaat bul")
                time.sleep(20)
                continue
            ##############################################################################################
            # oniki saat butonunu buluyor yukarıda ama
            # eger sayfa ilgili browserda on planda degilse bulamıyor
            # bulana kadar for döngusue giriyor
            # gidip elle on plana cıkarınca sayfayı devam edebiliyor
            for deneme in range (0,10):
                try:
                    time.sleep(rand_zaman())
                    onikisaat_3.click()
                    time.sleep(rand_zaman())
                    break
                except Exception as hata:
                    print(deneme, " hata onikisaat click")
                    time.sleep(10)
            ##############################################################################################
            # zaman dialogu confirm butonu bul
            try:
                time.sleep(rand_zaman())
                confirmzaman = driver.find_element(By.CLASS_NAME,"css-snax1n")
            except Exception as hata:
                print("confirmzaman hata")
                time.sleep(10)
                continue
            ##############################################################################################
            # zaman dialogu confirm tıkla
            try:
                time.sleep(rand_zaman())
                confirmzaman.click()
            except Exception as hata:
                print("confirmzaman.click hata")
                time.sleep(10)
                continue
            ############################################################################################
            try:
                fiyat_kontrol=WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-1egrtsu"))
                #time.sleep(rand_zaman())
                dd33=fiyat_kontrol[0].text
                fff44=dd33.split(" ")
                print(bcolors.IPurple,"fiyat = ",bcolors.IYellow,fff44[0],"-",fff44[1],bcolors.ENDC,end=" ")
                if float(fff44[0])==float(fiyat_txt):
                    print(bcolors.IGreen,"fiyat ok problem yok",bcolors.ENDC,end=" ")
                else:
                    print("hatali fiyat")
                    keyword = input("Dikkat Hatali Fiyat")
            except Exception as hata:
                keyword = input("fiyat konntrolde problem var ")
                print("hata varrrrrr8=>")
                keyword = input("Dikkat Hatali Fiyat")
            ##############################################################################################
            try:
                confirmfiyat_butonu= WebDriverWait(driver,20).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-7nzfwg"))
                time.sleep(rand_zaman())
                confirmfiyat_butonu[0].click()
            except Exception as hata:
                print("confirmfiyat butonu hata")
                time.sleep(10)
                continue
                ############################################################################################
            try:
                time.sleep(rand_zaman())
                completed=WebDriverWait(driver,15).until(lambda driver: driver.find_elements(By.CLASS_NAME,"css-1lf0s96"))
                completed_txt=completed[0].text
                if completed_txt !="Listing Completed":
                    keyword = input("hata1313")
            except Exception as hata:
                print("completed hatasi var 20 sn ara verildi")
                time.sleep(20)
                continue
            ############################################################################################
            try:
                listeleme_suresi=time.time() - start
                listeleme_suresi=round(listeleme_suresi,1)
                listeleme_toplam_sure=listeleme_toplam_sure+listeleme_suresi
                listeleme_toplam_sure=round(listeleme_toplam_sure/60,1)
                print(bcolors.IPurple,"suresi = ",bcolors.IYellow,listeleme_suresi,"sn",bcolors.ENDC)
            except Exception as hata:
                print("listeleme suresi hatasi var")

            ##############################################################################################
            # csv dosyasina kayit
            try:
                dict22={"bitis_zaman":tarih,"isim":isim111,"token_id":token_id_number_txt,"fiyat":fiyat_txt,"lst_suresi":listeleme_suresi}
                nft_listem.append(dict22)
                df = pd.DataFrame(nft_listem)
                #df.to_csv("csv_1//"+dosya_tarih+"-nftlistesi.csv", index=False)
                df.to_csv("csv_1//nftlistesi.csv", index=False)
            except Exception as hata:
                print("csv kayit hata var")
                time.sleep(10)
                continue

            #############################################################################################
            break # while True: icin
    ##############################################################################################
    bekleme991=datetime.now()+timedelta(hours=0,minutes=gurup_dakika,seconds=0)
    print("diger "+str(gurp_sayi)+ " luk gurub icin bekleme",bekleme991)
    pause.until(bekleme991)

#sbc.set_brightness(0, display=0)

keyword = input("SON a geldi")
