import os
import time
import webbrowser
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import strftime
from datetime import datetime
from datetime import date
import datetime
from selenium.webdriver.support.ui import Select


# webdriver.setProperty("C:Windows\chromedriver.exe");               # No windows 10 e colocado na pasta - system32
driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(4)

# Nomes das buscas
buscas = ['GitHub', 'coronavirus']

for i in range(0, 3):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[i])
    driver.get("https://www.google.com.br")
    time.sleep(3)
    caixabusca = driver.find_element_by_name('q')
    caixabusca.send_keys(str(buscas[i]))
    caixabusca.submit()


# HD --
