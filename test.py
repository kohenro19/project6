import requests
import numpy as np
import pandas as pd

REQUEST_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
APP_ID=1035694033279278134

serch_keyword = 'メークイン'

serch_params = {
    "format" : "json",
    "keyword" : serch_keyword,
    "applicationId" : [APP_ID],
    "availability" : 0,
    "hits" : 30,
    "page" : 1,
    "sort" : "-updateTimestamp"
}

response = requests.get(REQUEST_URL, serch_params)
result = response.json()

print(result)