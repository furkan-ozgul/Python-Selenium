import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import random


############################################################################

driver = webdriver.Chrome()
driver.maximize_window()


############################################################################

def Login():
    driver.get('https://devn029.paket.taxi/index.php?action=Login&module=Users')
    ## LOGIN
    # Kullanıcı İsmi Girilimi
    input = driver.find_element(By.ID,'user_name')
    input.send_keys('*******')

    # Şifre Girilimi
    input = driver.find_element(By.ID,'username_password')
    input.send_keys('********')

    # Enter Tuşuna Basma
    input.send_keys(Keys.ENTER)

def CreateOperation():
    #Operasyon Oluştur sayfasını götürür.
    driver.get("https://devn029.paket.taxi/index.php?module=adv_User_Operations&action=EditView&return_module=adv_User_Operations&return_action=DetailView")   

    #Kurye adı girmesi için
    input = driver.find_element(By.XPATH,'//*[@id="employee_name"]')
    input.send_keys('DENEME KURYE')

    #Operayon adı girmesi için
    input = driver.find_element(By.XPATH,'//*[@id="aos_contracts_name"]')
    input.send_keys('Deneme Operasyonu')

    #Başlangıç Tarihi girmesi için
    input = driver.find_element(By.ID,'start_date')
    input.send_keys('01/01/2023')

    #Bitiş Tarihi girmesi için
    input = driver.find_element(By.ID,'end_date')
    input.send_keys('03/01/2023')

    
    input = driver.find_element(By.ID,'assigned_user_name')
    input.send_keys('DENEME KURYE')

    #Çalışma saati girmesi için
    input = driver.find_element(By.ID,'calisma_saati')
    input.send_keys(random.randint(45, 500))

    #Fiyatlandırma girmesi için
    input = driver.find_element(By.ID,'aos_products_name')
    input.send_keys('JOKERSABİTMOTORKİRAÜrünü')

    #Tanım girmesi için
    input = driver.find_element(By.ID,'description')
    input.send_keys('Deneme Tanım')

    time.sleep(1)

    #Kaydet
    input = driver.find_element(By.ID,'SAVE')
    input.click()

############################################################################

Login()

CreateOperation()


time.sleep(5)


