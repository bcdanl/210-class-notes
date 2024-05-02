#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:26:23 2024

@author: bchoe
"""


# %%
# =============================================================================
# Python Environment for Web-scrapping with selenium
# selenium webdriver
# =============================================================================

import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException


# Set the working directory path
wd_path = '/Users/bchoe/Documents/websites/210-class-notes'
os.chdir(wd_path)  # Change the current working directory to wd_path

options = Options()
options.add_argument("window-size=1400,1200") # to set the window size

# driver = webdriver.Chrome(options = options)


# %%
# =============================================================================
# try-except
# =============================================================================

a = 5
b = 0
result = a / b
c = a * b


try:
    a = 5
    b = 0
    result = a / b
except:
    pass

c = a * b





# %%
# =============================================================================
# NoSuchElementException
# =============================================================================
driver = webdriver.Chrome(options = options)
url = 'https://www.imdb.com/search/title/?genres=family'

driver.get(url)

elem = driver.find_element(By.XPATH, "element_xpath")

try:
    elem = driver.find_element(By.XPATH, "element_xpath")
    elem.click()
except NoSuchElementException:
    pass




try:
    elem = driver.find_element(By.XPATH, "element_xpath")
    elem.click()
except NoSuchElementException:
    xpath_title = '/html/body/div[2]/main/div[2]/div[3]/section/section/'+\
                  'div/section/section/div[2]/div/section/div[2]/div[2]/'+\
                  'ul/li[1]/div/div/div/div[1]/div[2]/div[1]/a/h3'
    elem = driver.find_element(By.XPATH, xpath_title)


elem.text


# %%
# =============================================================================
# Wait
# =============================================================================
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# example webpage
url = "https://qavbox.github.io/demo/delay/"
driver.get(url)

btn = driver.find_element(By.XPATH, '/html/body/form/fieldset/div/div[1]/input')
btn.click()

element = (  # 10 is timeout in seconds when an expectation is called
  WebDriverWait(driver, 10)
  .until(
    EC.presence_of_element_located(
      (By.ID, "two")
      )
    )
) 

element.text



driver.find_element(By.XPATH, '//*[@id="one"]/input').click()
time.sleep(6)
element = driver.find_element(By.XPATH, '//*[@id="two"]')
element.text




driver.find_element(By.XPATH, '//*[@id="oneMore"]/input[1]').click()
driver.implicitly_wait(6)
element2 = driver.find_element(By.ID, 'delay')

element2.text



# %%
# =============================================================================
# Classwork 13
# Question 2
# =============================================================================

url = 'https://www2.census.gov/programs-surveys/popest/tables/2010-2019/counties/totals/'
driver.get(url)

tbody = driver.find_element(By.TAG_NAME, 'tbody')
rows = tbody.find_elements(By.TAG_NAME, 'tr')


# /html/body/table/tbody/tr[5]/td[2]

for i in range(4,len(rows)):
    xpath = '/html/body/table/tbody/tr['+str(i)+']/td[2]'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    
    
    
# %%
# =============================================================================
# API endpoints
# =============================================================================

import requests
endpoint = 'https://data.cityofnewyork.us/resource/ic3t-wcy2.json'  ## API endpoint
response_API = requests.get(endpoint)
df = pd.read_json(response_API.text)


# %%
# =============================================================================
# FRED API
# =============================================================================


import requests
import json
import pandas as pd
params = {
'api_key': '80657885ed24a6137d5f63590c0e5c4a', ## Change to your own key
'file_type': 'json',
'series_id': 'GDPC1'   ## ID for US real GDP
}
endpoint = "series/observations"
url = "https://api.stlouisfed.org/"
response = requests.get(url + "fred/" + endpoint, params = params)


# Extract the response content (i.e. text).
content = response.content.decode('utf-8')

# Convert JSON response to Python dictionary.
fred = json.loads(content) 

# Extract the "observations" list element.
observations = pd.DataFrame( fred['observations'] )
observations = observations.astype({'value': float})


# %%
# =============================================================================
# 
# =============================================================================


# Blank