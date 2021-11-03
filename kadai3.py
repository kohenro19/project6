import requests

# 定数は上部で定義する
RAKUTEN_PRODUCT_URL = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
APP_ID = "1035694033279278134"

serch_keyword = '米'

serch_params = {
    "format" : "json",
    "keyword" : serch_keyword,
    "applicationId" : [APP_ID],
    "availability" : 1,
    "hits" : 30,
    "page" : 1,
}

response = requests.get(RAKUTEN_PRODUCT_URL, serch_params)
response = response.json()

for product_list in response["Products"]:
    print(product_list["Product"]["maxPrice"])

# for product_list in response["Items"]:
#     # print(product_list)
#     print(product_list["Item"]["itemPrice"])
