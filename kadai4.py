import requests

# 定数は上部で定義する
RAKUTEN_PRODUCT_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
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

for list in response["Items"]:
    global tmp
    # print(list["Item"])
    tmp = str(list["Item"]["rank"]) + ": " + list["Item"]["itemName"] + "\r\n"

    with open("output.csv", mode='a', encoding="utf8") as f:
        f.write(tmp)
        f.close