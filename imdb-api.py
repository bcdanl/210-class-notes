#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:18:56 2024

@author: bchoe
"""

import requests
import pandas as pd
url = "https://caching.graphql.imdb.com/"

querystring = {"operationName":"AdvancedTitleSearch",
               "variables":"{\"before\":\"eyJlc1Rva2VuIjpbIjk4NyIsIjk4NyIsInR0MzUyMTE2NCJdLCJmaWx0ZXIiOiJ7XCJjb25zdHJhaW50c1wiOntcImdlbnJlQ29uc3RyYWludFwiOntcImFsbEdlbnJlSWRzXCI6W1wiRmFtaWx5XCJdLFwiZXhjbHVkZUdlbnJlSWRzXCI6W119fSxcImxhbmd1YWdlXCI6XCJlbi1VU1wiLFwic29ydFwiOntcInNvcnRCeVwiOlwiUE9QVUxBUklUWVwiLFwic29ydE9yZGVyXCI6XCJBU0NcIn0sXCJyZXN1bHRJbmRleFwiOjQ5fSJ9\",\"first\":500,\"genreConstraint\":{\"allGenreIds\":[\"Family\"],\"excludeGenreIds\":[]},\"locale\":\"en-US\",\"sortBy\":\"POPULARITY\",\"sortOrder\":\"ASC\"}",
               "extensions":"{\"persistedQuery\":{\"sha256Hash\":\"42714660b115c035a3c14572bfd2765c622e2659f7b346e2ee7a1f24296f08e7\",\"version\":1}}"}

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "application/graphql+json, application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.imdb.com/",
    "content-type": "application/json",
    "x-imdb-client-name": "imdb-web-next-localized",
    "x-amzn-sessionid": "140-0026983-3966373",
    "x-imdb-client-rid": "AASNDDB87M5YYRV372B8",
    "x-imdb-user-language": "en-US",
    "x-imdb-user-country": "US",
    "x-imdb-weblab-treatment-overrides": "{'IMDB_NAV_PRO_FLY_OUT_Q1_REFRESH_848923':'T1'}",
    "Origin": "https://www.imdb.com",
    "Connection": "keep-alive",
    "Cookie": "session-id=140-0026983-3966373; session-id-time=2082787201l; ubid-main=133-6361421-3126768; ad-oo=0; ci=e30; session-token=58sUum+QFoyQ8XilbaLtw8q4izKQAgJGOZsHBN83fI5iMQaUN8ws18EIZ0IDH5f1k78E+kPuzkdmLMgeZ5RyeKSdLZ5mYw03ppI2k/X9ya4F5hP+3KbPkL2TX6GigGlWITZD91AyRFXjns4P0pr4Is4LGUD8CcpkFML61zT8UCE6PRxPxkfU9lym3JdzGoO5yV+wgHW7Zn+GyglXL84asrXWIXSkPFQ8gxpIFY6U47plgRb6UwDsF0tQpGgAAF7sP6uONCLxj7F24lqF/OabUrPlwPbuc7BIK63WZH5tuz863i5W7etNLTDvx8DxKPdBN04QXY/RbNkMjk6DsRHYgAf+RSjV0R2h",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)


data = response.json()['data']['advancedTitleSearch']['edges']

data = pd.json_normalize(data)
data.columns
data.columns = data.columns.str.strip('node.title.')
