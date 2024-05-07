#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 6 20:10:43 2024

@author: byeong-hakchoe
"""

# %%
# loading libraries
import pandas as pd
import numpy as np
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
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

url = 'https://www.imdb.com/search/title/?genres=family'
driver.get(url)

# %%

xpath = '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section'+\
    '/div[2]/div/section/div[2]/div[2]/div[2]/div/span/button/span'
btn = driver.find_element(By.XPATH, xpath)

for i in range(0,3):
    try:
        btn.click()
        # time.sleep(5)
    except:
        btn.click()
        time.sleep(5)

xpath_lst = '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul'
lst = driver.find_element(By.XPATH, xpath_lst)
items = lst.find_elements(By.TAG_NAME, 'li')

df = pd.DataFrame()
for i in range(0, len(items)):
    ranking_title = items[i].find_element(By.CLASS_NAME, 'ipc-title__text').text
    
    try:
        xpath_meta = '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li['+str(i+1)+']/div/div/div/div[1]/div[2]/div[2]'
        year_runtime_rating = driver.find_element(By.XPATH, xpath_meta)
        year_runtime_rating = year_runtime_rating.find_elements(By.TAG_NAME, 'span')
        
        if len(year_runtime_rating) == 3:
            year =  year_runtime_rating[0].text
            runtime = year_runtime_rating[1].text
            rating = year_runtime_rating[2].text
        elif len(year_runtime_rating) == 1:
            year =  year_runtime_rating[0].text
            runtime = ''
            rating = ''
        else:
            year =  year_runtime_rating[0].text
            
            if ('h' in year_runtime_rating[1].text) & ('m' in year_runtime_rating[1].text):
                runtime = year_runtime_rating[1].text
                rating = ''
            else:
                runtime = ''
                rating = year_runtime_rating[1].text
    except:
        year = ''
        runtime = ''
        rating = ''
        
    try:
        xpath_imdb_score = '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li['+str(i+1)+']/div/div/div/div[1]/div[2]/span/div/span'
        imdb_score = driver.find_element(By.XPATH, xpath_imdb_score).get_attribute('aria-label')
    except:
        imdb_score = ''
    
    try:
        vote = items[i].find_element(By.CLASS_NAME, 'ipc-rating-star--voteCount').text
    except:
        vote = ''

    try:    
        xpath_metascore = '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li['+str(i+1)+']/div/div/div/div[1]/div[2]/span/span/span[1]'
        metascore = driver.find_element(By.XPATH, xpath_metascore).text
    except:
        metascore = ''
    
    plot = items[i].find_element(By.CLASS_NAME, 'ipc-html-content-inner-div').text
    
    ranking_title = pd.DataFrame([ranking_title])
    year = pd.DataFrame([year])
    runtime = pd.DataFrame([runtime])
    rating = pd.DataFrame([rating])
    imdb_score = pd.DataFrame([imdb_score])
    vote = pd.DataFrame([vote])
    metascore = pd.DataFrame([metascore])
    plot = pd.DataFrame([plot])
    
    obs = pd.concat([ranking_title, year, runtime, rating, 
                     imdb_score, vote, metascore, plot], axis = 1)
    df = pd.concat([df, obs])
    

df.columns = ['ranking_title', 'year', 'runtime', 'rating', 
                 'imdb_score', 'vote', 'metascore', 'plot']
df[['ranking', 'title']] = df['ranking_title'].str.split('.', n=1, expand=True)
df = df.drop(columns=['ranking_title'])
df['imdb_score'] = df['imdb_score'].str.replace('This title is currently not ratable', '')
df['imdb_score'] = df['imdb_score'].str.replace('IMDb rating: ', '')
df['vote'] = df['vote'].str.replace(' (', '')
df['vote'] = df['vote'].str.replace(')', '')


df.to_csv('imdb_family_2024_0506.csv')

# %%
# =============================================================================
# 
# =============================================================================

# Blank
