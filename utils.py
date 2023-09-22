from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
from dotenv import load_dotenv
import time

def preload(): #打開瀏覽器
    options = Options()
    options.add_argument("--disable-notifications")
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    chrome.maximize_window()    
    chrome.implicitly_wait(5)   #隱式等待 最多給五秒等待，提早載入好，提早往下走
    # chrome.get("http://localhost:8000/")
    chrome.get('https://www.youtube.com/')
    return chrome

def login(chrome,mail,password): #登入會員
    index_login_btn=chrome.find_element(By.XPATH,"//*[@id='navbarTogglerDemo03']/form/a[1]") 
    index_login_btn.click()
    chrome.find_element(By.ID, "ic_id").send_keys(mail)
    chrome.find_element(By.ID, "ic_password").send_keys(password)
    chrome.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/form/input[2]').click() #按下登入按鈕  

def modify_profile(chrome,phone): #修改會員資料
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(0.5)
    chrome.find_element(By.ID,"modify_form").click() #按下修改按鈕
    form_phone = chrome.find_element(By.ID,"icphonenumber")
    form_phone.clear()
    form_phone.send_keys(phone)

    time.sleep(0.5)
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(0.5)
    chrome.find_element(By.XPATH, '//*[@id="form_profile_modify"]/div[10]/div[1]/button').click()
    #time.sleep(2)
    #modify_finish_btn.click()
    time.sleep(0.5)
    modify_close_btnd = chrome.find_element(By.XPATH,'//*[@id="messageModal"]/div/div/div[3]/button')
    modify_close_btnd.click()

def test_sign_up(chrome): #報名考試
    chrome.find_element(By.XPATH,'//*[@id="navbarTogglerDemo03"]/ul[1]/li[2]/a').click()
    chrome.execute_script("window.scrollTo(0,828.5)")
    time.sleep(0.5)
    chrome.find_element(By.XPATH,'//*[@id="selectCourse1"]').click()
    chrome.find_element(By.ID,'btn_test_reg').click()

def score_search(chrome): #下載成績單
    chrome.execute_script("window.location.href = 'http://localhost:8000/profile'")
    time.sleep(0.5)
    chrome.find_element(By.XPATH,'//*[@id="v-pills-messages-tab"]').click()
    time.sleep(0.5)
    chrome.find_element(By.XPATH,'//*[@id="v-pills-messages"]/div/table/tbody/tr/td/button').click()

def brief_download(chrome): #簡章下載
    chrome.execute_script("window.location.href = 'http://localhost:8000/ictestinfo'")
    time.sleep(0.5)
    chrome.find_element(By.XPATH,'/html/body/div/div[1]/div/ul/li[1]/a').click()

def questions_bank_download(chrome): #題庫下載
    chrome.execute_script("window.location.href = 'http://localhost:8000/ictestinfo'")
    time.sleep(0.5)
    chrome.find_element(By.XPATH,'/html/body/div/div[1]/div/ul/li[2]/a').click()
