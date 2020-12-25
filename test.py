# coding:utf-8
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()

# chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('-kiosk')
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
url = "http://www.baidu.com"
driver.get(url)
# kill_cmd = 'taskkill /f /IM %s' % 'chrome.exe'
# os.system(kill_cmd)
# driver = webdriver.Chrome(chrome_options=option)
# driver.get("http://www.baidu.com")

