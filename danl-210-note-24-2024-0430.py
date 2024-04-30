#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:28:20 2024

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

# Set the working directory path
wd_path = '/Users/bchoe/Documents/websites/210-class-notes'
os.chdir(wd_path)  # Change the current working directory to wd_path

options = Options()
options.add_argument("window-size=1400,1200") # to set the window size

# driver = webdriver.Chrome(options = options)

# %%
# =============================================================================
# Project
# =============================================================================

esg_proj = pd.read_csv("https://bcdanl.github.io/data/esg_proj.csv")


# %%
# =============================================================================
# Classwork 11 Review
# =============================================================================

driver = webdriver.Chrome(options = options)
url = 'http://quotes.toscrape.com'
driver.get(url)

df = pd.DataFrame()
for page in range(1, 11):
    url = 'https://quotes.toscrape.com/page/'+str(page)+'/'
    driver.get(url)
    time.sleep(3)
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


df['tags'].iloc[0]
df['tags'].iloc[1]
df['tags'].iloc[2]

df_tags = pd.DataFrame()
for i in range(0, len(df)):
    df_tag = pd.DataFrame(df['tags'].iloc[i])
    df_tags = pd.concat([df_tags, df_tag])
df_tags.columns = ['tag']

tag_count = df_tags['tag'].value_counts()



# %%
# =============================================================================
# Do Q2 in Classwork 11 with While True if else break
# =============================================================================

# driver = webdriver.Chrome(options = options)
url = 'http://quotes.toscrape.com'
driver.get(url)

next_btn = driver.find_element(By.PARTIAL_LINK_TEXT, 'Next')

df = pd.DataFrame()
while True:
    quotes = driver.find_elements(By.CLASS_NAME, 'quote')
    try:
        next_btn = driver.find_element(By.PARTIAL_LINK_TEXT, 'Next')
    except:
        next_btn = []
        
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
        
    if next_btn != []:
       next_btn.click()
    else:
        break


df.columns = ['quote', 'author', 'tags', 'about']
df.to_csv('quote_2024_0430.csv', index = False)

# %%
# =============================================================================
# while
# =============================================================================


i = 1
while i < 6:
  print(i)
  i += 1  # i = i + 1


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
# %%
# =============================================================================
# yfinance
# =============================================================================
  
import yfinance as yf
from datetime import datetime

# Create the ticker for Nvidia
nvda = yf.Ticker("NVDA")

# Get today's date and convert it to a string with YYYY-MM-DD format
  # (yfinance expects that format)
end_date = datetime.now().strftime('%Y-%m-%d')

nvda_hist = nvda.history(start='2024-01-01', end=end_date)


nvda_hist_min = nvda.history(end = end_date, interval = '1m', period = 'max')
nvda_hist_min = nvda.history(end = end_date, interval = '1m')

# NVDA: 1m data not available for startTime=1711830306 and endTime=1714508706. 
# Only 7 days worth of 1m granularity data are allowed to be fetched per request.


companies = ['AMZN', 'APPL', 'GOOG', 'MSFT', 'NVDA', 'TSLA', 'META'] 
tickers = yf.Tickers(companies)
tickers_hist = tickers.history(start='2024-01-01', end=end_date)

tickers_hist_long = (
    tickers_hist
    .stack()   # stacking, similar to DataFrame.melt()
    .rename_axis(['Date', 'Ticker']) # rename row index
    .reset_index()
)



msft = yf.Ticker("MSFT")
# get all stock info
msft.info 


# show meta information about the history (requires history() to be called first)
msft.history_metadata

# show share count
# - accurate time-series count:
msft.get_shares_full(start="2022-01-01", end=None)

# show financials:
# - income statement
df_income_stmt = msft.income_stmt.T
df_income_stmt.columns

df_income_stmt_q = msft.quarterly_income_stmt.T


# - balance sheet
df_balance_sheet = msft.balance_sheet.T
df_balance_sheet.columns

df_balance_sheet_q = msft.quarterly_balance_sheet.T
df_balance_sheet_q.columns

# - cash flow statement
msft.cashflow
msft.quarterly_cashflow
  # see `Ticker.get_income_stmt()` for more options


# show holders
msft.major_holders
msft.institutional_holders
msft.mutualfund_holders

# show news
msft.news

# %%
# =============================================================================
# 
# =============================================================================

# Blank

















