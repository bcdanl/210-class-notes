#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:31:07 2024

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

# Set the working directory path
wd_path = '/Users/bchoe/Documents/websites/210-class-notes'
os.chdir(wd_path)  # Change the current working directory to wd_path

options = Options()
options.add_argument("window-size=1400,1200") # to set the window size

driver = webdriver.Chrome(options = options)



# %%
# =============================================================================
# Classwork 12
# Question 1
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

tbody = driver.find_element(By.TAG_NAME, 'tbody')
rows = tbody.find_elements(By.TAG_NAME, 'tr')
len(rows)

thead = driver.find_element(By.TAG_NAME, 'thead')
cols = thead.find_elements(By.TAG_NAME, 'th')
len(cols)


df = pd.DataFrame()
for row in range(1, len(rows) + 1):
    xpath_1 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr['+str(row)+']/td[1]'
    xpath_2 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr['+str(row)+']/td[2]'
    xpath_3 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr['+str(row)+']/td[3]'
    xpath_4 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr['+str(row)+']/td[4]'
    xpath_5 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr['+str(row)+']/td[5]'
    xpath_6 = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr['+str(row)+']/td[6]'
    
    col_1 = driver.find_element(By.XPATH, xpath_1).text
    col_2 = driver.find_element(By.XPATH, xpath_2).text
    col_3 = driver.find_element(By.XPATH, xpath_3).text
    col_4 = driver.find_element(By.XPATH, xpath_4).text
    col_5 = driver.find_element(By.XPATH, xpath_5).text
    col_6 = driver.find_element(By.XPATH, xpath_6).text
    
    col_1 = pd.DataFrame( [col_1] )
    col_2 = pd.DataFrame( [col_2] )
    col_3 = pd.DataFrame( [col_3] )
    col_4 = pd.DataFrame( [col_4] )
    col_5 = pd.DataFrame( [col_5] )
    col_6 = pd.DataFrame( [col_6] )
    
    obs = pd.concat([col_1, col_2, col_3, col_4, col_5, col_6], axis = 1)
    df = pd.concat([df, obs])



df.columns = ['mon-yr', 'retail_price', 'refining', 'dist_mktg', 'tax', 'crude_oil']
df.to_csv('eia_2024_0425.csv', index = False)



# %%
# =============================================================================
# EIA with nested for-loop
# =============================================================================
tbody = driver.find_element(By.TAG_NAME, 'tbody')
rows = tbody.find_elements(By.TAG_NAME, 'tr')

thead = driver.find_element(By.TAG_NAME, 'thead')
cols = thead.find_elements(By.TAG_NAME, 'th')

df = pd.DataFrame()
# for row in range(1, len(rows) + 1):
#     for col in range(1, len(cols)+1):
#         xpath = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr['+str(row)+']/td['+str(col)+']'
#         print(xpath)
        
df = pd.DataFrame()
for row in range(1, len(rows) + 1):
    obs = []
    for col in range(1, len(cols)+1):
        xpath = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr['+str(row)+']/td['+str(col)+']'
        data = driver.find_element(By.XPATH, xpath).text
        obs.append(data)
    obs = pd.DataFrame(obs).T
    df = pd.concat([df, obs])
        
        




# %%
# =============================================================================
# Classwork 12
# Question 2
# =============================================================================

url = 'http://quotes.toscrape.com'
driver.get(url)

quotes = driver.find_elements(By.CLASS_NAME, 'quote')
quotes[0].find_element(By.CLASS_NAME, 'text').text
quotes[1].find_element(By.CLASS_NAME, 'text').text

quotes[0].find_element(By.CLASS_NAME, 'author').text
quotes[1].find_element(By.CLASS_NAME, 'author').text

quotes[0].find_element(By.CLASS_NAME, 'tags').text
quotes[1].find_element(By.CLASS_NAME, 'tags').text

quotes[0].find_element(By.PARTIAL_LINK_TEXT, 'about').get_attribute('href')
# driver.back()


df = pd.DataFrame()
for page in range(1,11):
    url = 'https://quotes.toscrape.com/page/'+str(page)+'/'
    driver.get(url)
    quotes = driver.find_elements(By.CLASS_NAME, 'quote')
    for i in range(0, len(quotes) ):
        text = quotes[i].find_element(By.CLASS_NAME, 'text').text
        author = quotes[i].find_element(By.CLASS_NAME, 'author').text
        tags = quotes[i].find_element(By.CLASS_NAME, 'tags').text
        about = quotes[i].find_element(By.PARTIAL_LINK_TEXT, 'about').get_attribute('href')
        
        text = pd.DataFrame([text])
        author = pd.DataFrame([author])
        tags = pd.DataFrame([tags])
        about = pd.DataFrame([about])
        
        obs = pd.concat([text, author, tags, about], axis = 1)
        df = pd.concat([df, obs])

df.columns = ['quote', 'author', 'tags', 'author-url']

df['tags'] = df['tags'].str.replace('Tags: ', '')
df['tags'] = df['tags'].str.split(' ')


df_author = pd.DataFrame()
for url_author in df['author-url'].unique():
    driver.get(url_author)
    
    born_date = driver.find_element(By.CLASS_NAME, 'author-born-date').text
    born_location = driver.find_element(By.CLASS_NAME, 'author-born-location').text
    description = driver.find_element(By.CLASS_NAME, 'author-description').text
    
    url_author = pd.DataFrame([url_author])
    born_date = pd.DataFrame([born_date])
    born_location = pd.DataFrame([born_location])
    description = pd.DataFrame([description])
    
    obs = pd.concat([url_author, born_date, born_location, description], axis = 1)
    df_author = pd.concat([df_author, obs])

df_author.columns = ['author-url', 'born_date', 'born_location', 'description']


# %%
# =============================================================================
# Chat GPT's answer for Question 2
# =============================================================================


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Configuration for the WebDriver
driver = webdriver.Chrome()

# Open the target website
driver.get("http://quotes.toscrape.com")

# Prepare to collect data
all_quotes = []

# Start scraping data
try:
    while True:
        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]
            author_url = quote.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
            all_quotes.append({
                "Text": text,
                "Author": author,
                "Tags": tags,
                "Author URL": author_url
            })

        # Navigate to the next page if available
        next_btn = driver.find_elements(By.CSS_SELECTOR, "li.next > a")
        if next_btn:
            next_btn[0].click()
            time.sleep(2)  # Pause for 2 seconds to let the page load
        else:
            break
finally:
    driver.quit()

# Load data into a DataFrame
df = pd.DataFrame(all_quotes)

# Show DataFrame
print(df.head())

# Optionally, save the DataFrame to a CSV file
# df.to_csv("quotes.csv", index=False)

