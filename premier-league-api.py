#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:52:28 2024

@author: bchoe
"""

import requests
import pandas as pd


# %%
# =============================================================================
# Goals
# =============================================================================
url = "https://footballapi.pulselive.com/football/stats/ranked/players/goals"

df_goals = pd.DataFrame()
for x in range(0, 10):
    querystring = {"page":f"{x}",
                   "pageSize":"10",
                   "compSeasons":"578",
                   "comps":"1",
                   "compCodeForActivePlayer":"EN_PR",
                   "altIds":"true"}
    
    payload = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.premierleague.com",
        "Connection": "keep-alive",
        "Referer": "https://www.premierleague.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site"
    }
    
    res = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        
    content = res.json()['stats']['content']
    data = pd.json_normalize(content) # Create a DataFrame from the nested dictionary
    df_goals = pd.concat([df_goals, data])
    

# %%
# =============================================================================
# Assists
# =============================================================================

import requests

url = "https://footballapi.pulselive.com/football/stats/ranked/players/goal_assist"

df_assists = pd.DataFrame()
for x in range(0, 10):
    querystring = {"page":"0",
                   "pageSize":"10",
                   "compSeasons":"578",
                   "comps":"1",
                   "compCodeForActivePlayer":"EN_PR",
                   "altIds":"true"}
    
    payload = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.premierleague.com",
        "Connection": "keep-alive",
        "Referer": "https://www.premierleague.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "TE": "trailers"
    }
    
    res = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    # print(response.text)
    
    content = res.json()['stats']['content']
    data = pd.json_normalize(content)
    df_assists = pd.concat([df_assists, data])
    


