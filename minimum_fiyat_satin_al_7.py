from selenium.webdriver.common.by import By
import time

import numpy as np
import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from renkler import bcolors

'''myIterator = cycle(range(2))'''
########################################################################
'''firefox_options1 = myfirefox_options()
profile_path1="C://Users//windows10bulent//AppData//Roaming//Mozilla//Firefox//Profiles//dtyux9h2.nurten"
firefox_options1.add_argument("-profile")
firefox_options1.add_argument(profile_path1)
firefox_options1.add_argument('--disable-extensions')
driver_nurten = webdriver.Firefox(service=Service(GeckoDriverManager(path = ".//Drivers").install()),options=firefox_options1)
driver_nurten.set_page_load_timeout(10)
wait = WebDriverWait(driver_nurten, 20)'''
########################################################################
'''chrome_options = mychrome_options()
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--user-data-dir=/home/mint/.config/google-chrome/Profile 1")
chrome_options.add_argument('--disable-extensions')
driver_ben = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver_ben.set_page_load_timeout(10)
wait = WebDriverWait(driver_ben, 20)'''
########################################################################
'''login_nurten="https://accounts.binance.com/en/login"
nft_asset_nurten="https://www.binance.com/en/nft/my-nfts/batman06-808c7362b972513978969143b22ea8c2"

login_ben="https://accounts.binance.com/en/login"
nft_asset_ben="https://www.binance.com/en/nft/profile/catwoman-0c22fd6bd8f4af395da3f903a83a76d2"'''
###########  login yapmak icin sayfa ac ve tusa basilmasini bekle #####
###########  login yapmak icin sayfa ac ve tusa basilmasini bekle #####
'''driver_ben.get(login_ben)
print(bcolors.IGreen,"---------------------------------------------------",bcolors.ENDC)
print(bcolors.IGreen,"---------------------------------------------------",bcolors.ENDC)
print(bcolors.IGreen,"---------------------------------------------------",bcolors.ENDC)
keyword = input("**** DEVAM icin bir tusa BAS ****")'''
######################################################
def telegram_bot_sendtext(bot_message):
    bot_token = '1186915274:AAEvWTUvT9hQawu5o77tC0gjM2_nuESGUMw'
    bot_chatID = '685190703'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
#######################################################################
toplam_alinan=0
fiyat_arastirmasi_yap_ben=1
fiyat_arastirmasi_yap_nurten=1
#######################################################################
def fiyat_ara_satin_al(mydriver,secim:int):
    global toplam_alinan
    fiyat_nftpassport="0.32"
    fiyat_argentina="0.16"
    ########################################################################
    nftpassport_fiyat_url="https://www.binance.com/en/nft/marketplace?amountTo=0.11&currency=BUSD&tradeType=0&networks=BSC&isVerified=1&assetType=1&order=favorites%40-1"
    argentina_fiyat_url="https://www.binance.com/en/nft/marketplace?amountTo=0.11&currency=BUSD&tradeType=0&networks=BSC&isVerified=1&assetType=1&order=score%40-1"

    url_list=[nftpassport_fiyat_url,argentina_fiyat_url]
    fiyat_secim=[fiyat_nftpassport,fiyat_argentina]
    ##############################################################################################
    for_uzunlugu=3
    adim=0
    while adim < for_uzunlugu:
        try:
            mydriver.get(url_list[secim])
            time.sleep(5)
        except TimeoutException as hata:
            print("hata  -> driver.get() ")
        ##############################################################################################
        time.sleep(1)
        try:
            nft_fiyata_bak=WebDriverWait(mydriver,20).until(lambda mydriver: mydriver.find_elements(By.CLASS_NAME,"css-vurnku"))
        except Exception as hata:
            print("hata")
            time.sleep(10)
            continue

        try:

            for nft_fiyata_bak_inx in range(0,len(nft_fiyata_bak)):

                is_item_nft = nft_fiyata_bak[nft_fiyata_bak_inx].find_elements(By.CLASS_NAME, 'J-buynow')

                if len(is_item_nft) > 0:
                    time.sleep(4)
                    nft_fiyata_bak[nft_fiyata_bak_inx].click()
                    time.sleep(2)
                    #css-6xx5k5
                    buy_butonu=WebDriverWait(mydriver,5).until(lambda mydriver: mydriver.find_elements(By.CLASS_NAME,"css-6xx5k5"))
                    time.sleep(2)
                    buy_butonu[0].click()
                    time.sleep(2)
                    confirm_payment=WebDriverWait(mydriver,5).until(lambda mydriver: mydriver.find_elements(By.CLASS_NAME,"css-1ryj5g3"))
                    print(confirm_payment[0].text)
                    time.sleep(2)
                    #css-1jer9wy
                    total_payment=WebDriverWait(mydriver,5).until(lambda mydriver: mydriver.find_elements(By.CLASS_NAME,"css-1jer9wy"))
                    print(total_payment[0].text)
                    time.sleep(2)
                    payment_text=total_payment[0].text
                    payment_text_split=payment_text.split(" ")
                    payment_text_fiyat=payment_text_split[0]
                    payment_text_birim=payment_text_split[1]
                    payment_text_fiyat_float=float(payment_text_fiyat)
                    print(str(payment_text_fiyat_float),payment_text_birim)
                    time.sleep(2)
                    if payment_text_birim=="BUSD" and payment_text_fiyat_float <=float(fiyat_secim[secim]):
                        print("alim icin uygun")
                        confirm_buton=WebDriverWait(mydriver,5).until(lambda mydriver: mydriver.find_elements(By.CLASS_NAME,"css-zwojhg"))
                        confirm_buton[0].click()
                        time.sleep(2)
                        print("alindi")
                        toplam_alinan=toplam_alinan+1
                        if toplam_alinan>50:
                            input("toplam_alinan 15  dikkat ")
                    else:
                        print("alim icin uygun degil")
                    time.sleep(10)
                    break

        except TimeoutException  as hata:
            print("alimda hata")
            #time.sleep(4)

        print(bcolors.IBlue, adim," --------------------------------------------------",bcolors.ENDC)
        adim=adim+1



'''
for ttt in range(0,300):
    fiyat_ara_satin_al(driver_ben,next(myIterator))
    print(bcolors.IGreen,"-------30 sn genel ara verildi------",bcolors.ENDC)
    time.sleep(30)'''
