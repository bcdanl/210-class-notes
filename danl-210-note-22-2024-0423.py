#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:31:07 2024

@author: bchoe
"""

# %%
# =============================================================================
# Python libraries
# selenium webdriver
# =============================================================================

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("window-size=1400,1200") # to set the window size

driver = webdriver.Chrome(options = options)


# %%
# =============================================================================
# By.ID
# =============================================================================

form_url = "https://qavbox.github.io/demo/webtable/"
driver.get(form_url)
# driver.close()
# driver.quit()

form = driver.find_element(By.ID, "form1")
form

form.text  # text attribute if there is any


# %%
# =============================================================================
# By.CLASS_NAME
# =============================================================================

home_button = driver.find_element(By.CLASS_NAME, "homebtn")
home_button.click() # click the home_button object
driver.back() # back to the previous page


# %%
# =============================================================================
# By.NAME
# =============================================================================
home_button2 = driver.find_element(By.NAME, "home")
home_button2.click()
driver.back()


# %%
# =============================================================================
# 
# =============================================================================
# body > div > a > input
home_button3 = driver.find_element(By.CSS_SELECTOR, "body > div > a > input")
home_button3.click()
driver.back()


# %%
# =============================================================================
# 
# =============================================================================

table01 = driver.find_element(By.ID, "table01")
thead = table01.find_element(By.TAG_NAME, "thead")
thead.text

# %%
# =============================================================================
# 
# =============================================================================
selenium_link = driver.find_element(By.LINK_TEXT, "Selenium")
selenium_link.click()


# %%
# =============================================================================
# 
# =============================================================================
Selen_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "qav")
print(len(Selen_links))
Selen_links[0].click()
driver.back()

Selen_links[1].click()
driver.back()


# %%
# =============================================================================
# 
# =============================================================================

'//*[@id="table02"]/tbody/tr[1]/td[1]'
'/html/body/form/fieldset/div/div/table/tbody/tr[1]/td[1]'

elt = driver.find_element(By.XPATH, '//*[@id="table02"]/tbody/tr[1]/td[1]')
elt.text




# %%
# =============================================================================
# 
# =============================================================================

(
    driver
    .find_element(By.XPATH, 
                  '//*[@id="table01"]/tbody/tr[2]/td[3]/a')
    .get_attribute('href') 
 )


driver.find_element(By.ID, "table01").text

driver.find_element(By.XPATH, '//*[@id="btn"]').get_attribute('value')


# %%
# =============================================================================
# Classwork 12
# =============================================================================
url = "https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php"

driver.get(url)


# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td[1]

# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[1]/td[2]


tbody = driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody')


trows = tbody.find_elements(By.TAG_NAME, 'tr')


df = pd.DataFrame()

for row in range(1, len(trows) + 1):
    xpath = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[' + str(row) + ']/td[1]'
    print(xpath)

# To add a new column to the DataFrame, df
col = pd.DataFrame(['text_I_want_to_have'])
col2 = pd.DataFrame(['text_I_wanted_to_have'])

df = pd.concat([df, col], axis = 1 )
df = pd.concat([df, col2], axis = 1 )

# to get example dataframe
row_eg = pd.DataFrame(['cell_1', 'cell_2']).T

# to rename vairables
df.columns = ['col_1', 'col_2']
row_eg.columns = ['col_1', 'col_2']
df = pd.concat([df, row_eg])


# %%
# =============================================================================
# Classwork 12
# =============================================================================
url = "https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php"

driver.get(url)
tbody = driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody')
trows = tbody.find_elements(By.TAG_NAME, 'tr')

col_1 = pd.DataFrame()
col_2 = pd.DataFrame()
col_3 = pd.DataFrame()
col_4 = pd.DataFrame()
col_5 = pd.DataFrame()
col_6 = pd.DataFrame()
for row in range(1, len(trows) + 1):
    xpath_1 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[' + str(row) + ']/td[1]'
    xpath_2 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[' + str(row) + ']/td[2]'
    xpath_3 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[' + str(row) + ']/td[3]'
    xpath_4 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[' + str(row) + ']/td[4]'
    xpath_5 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[' + str(row) + ']/td[5]'
    xpath_6 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[' + str(row) + ']/td[6]'
    
    mon_yr = driver.find_element(By.XPATH, xpath_1).text
    price = driver.find_element(By.XPATH, xpath_2).text
    refining = driver.find_element(By.XPATH, xpath_3).text
    dist_mktg = driver.find_element(By.XPATH, xpath_4).text
    tax = driver.find_element(By.XPATH, xpath_5).text
    crude_oil = driver.find_element(By.XPATH, xpath_6).text
    
    mon_yr = pd.DataFrame([mon_yr])
    price = pd.DataFrame([price])
    refining = pd.DataFrame([refining])
    dist_mktg = pd.DataFrame([dist_mktg])
    tax = pd.DataFrame([tax])
    crude_oil = pd.DataFrame([crude_oil])

    col_1 = pd.concat([col_1, mon_yr])
    col_2 = pd.concat([col_2, price])
    col_3 = pd.concat([col_3, refining])
    col_4 = pd.concat([col_4, dist_mktg])
    col_5 = pd.concat([col_5, tax])
    col_6 = pd.concat([col_6, crude_oil])
    

df = pd.concat([col_1, col_2, col_3, col_4, col_5, col_6], axis = 1)
df.columns = ['mon-yr', 'price', 'refining', 'dist_mktg', 'tax', 'crude_oil']

# %%
# =============================================================================
# 
# =============================================================================




