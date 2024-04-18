#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:26:58 2024

@author: bchoe
"""

# %%
# =============================================================================
# Libraries
# =============================================================================

import pandas as pd

# Import the os module to interact with the operating system
import os  


# %%
# =============================================================================
# pd.read_html()
# =============================================================================
url = "https://www.nps.gov/orgs/1207/national-park-visitation-sets-new-record-as-economic-engines.htm"
tables = pd.read_html(url)
len(tables)
df_0 = tables[0]
df_1 = tables[1]

df_1.columns = df_1.iloc[0] 
df_1 = df_1.drop(index = df_1.index[0])

# Set the working directory path
wd_path = '/Users/bchoe/Documents/websites/210-class-notes'
os.chdir(wd_path)  # Change the current working directory to wd_path
os.getcwd()  # Retrieve and return the current working directory

# index=False to not write the row index in the CSV output
tables[0].to_csv('table.csv', index =False)