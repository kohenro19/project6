import requests
import json

REQUEST_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
APP_ID=1035694033279278134

serch_keyword = '米'

serch_params = {
    "format" : "json",
    "keyword" : serch_keyword,
    "applicationId" : [APP_ID],
    "availability" : 1,
    "hits" : 30,
    "page" : 1,
    "sort" : "-updateTimestamp"
}

response = requests.get(REQUEST_URL, serch_params)
response = response.json()

for list in response["Items"]:
    # print(list)
    print(list["Item"]["itemPrice"])

