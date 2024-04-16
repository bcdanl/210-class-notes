#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:33:44 2024

@author: bchoe
"""

# %%
# =============================================================================
# Python libraries
# =============================================================================
import pandas as pd


# %%
# =============================================================================
# pd.read_html()
# =============================================================================
url = "https://www.nps.gov/orgs/1207/national-park-visitation-sets-new-record-as-economic-engines.htm"

tables = pd.read_html(url)
len(tables)
tables[0]
tables[1]
