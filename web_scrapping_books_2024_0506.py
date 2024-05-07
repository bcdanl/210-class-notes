#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:09:31 2024

@author: byeong-hakchoe
"""
# %%
# loading libraries
import pandas as pd
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# %%
# working directory

# wd_path = '/Users/byeong-hakchoe/Downloads'
wd_path = '/Users/bchoe/My Drive/suny-geneseo/spring2024/lecture-codes'
os.chdir(wd_path)
os.getcwd()

# %%
# chrome browser with options
# options = Options()
# options.add_argument("window-size=1400,1200")
# driver_path = "/Users/byeong-hakchoe/Downloads/chromedriver-mac-x64/chromedriver"
# s = Service(driver_path)  
# driver = webdriver.Chrome(options = options, service=s)
driver = webdriver.Chrome()
# driver.implicitly_wait(5)

url = "http://books.toscrape.com/"
driver.get(url)

# %%

xpath_cats = '/html/body/div/div/div/aside/div[2]/ul/li/ul'
cats = driver.find_element(By.XPATH, xpath_cats)
n_cat = cats.find_elements(By.TAG_NAME, 'li')

df = pd.DataFrame()
for i in range(1, len(n_cat) + 1):
    xpath_cat = '/html/body/div/div/div/aside/div[2]/ul/li/ul/li['+str(i)+']/a'
    cat = driver.find_element(By.XPATH, xpath_cat)
    cat.click()
    xpath_category = xpath_cat + '/strong'
    category = driver.find_element(By.XPATH, xpath_category).text
    category = pd.DataFrame([category])

    while True:
        try:
            btn = driver.find_element(By.LINK_TEXT, 'next')
        except:
            btn = []
        
        xpath_books = '/html/body/div/div/div/div/section/div[2]/ol'
        book_list = driver.find_element(By.XPATH, xpath_books)
        books = book_list.find_elements(By.TAG_NAME, 'li')
        
        for j in range(0, len(books)):
            title = books[j].find_element(By.TAG_NAME, 'h3').find_element(By.TAG_NAME, 'a').get_attribute('title')
            price = books[j].find_element(By.CLASS_NAME, 'price_color').text
            title = pd.DataFrame([title])   
            price = pd.DataFrame([price])
            obs = pd.concat([category, title, price], axis = 1)
            df = pd.concat([df, obs])
        
        if btn != []:
            btn.click()
        else:
            break

df.columns = ['category', 'title', 'price']
df.to_csv('books_toscrape_2024_0506.csv', index = False)