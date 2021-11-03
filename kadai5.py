import requests
# import pytest


# @pytest.fixture
def write_products_list_to(search_keyword):
    RAKUTEN_PRODUCT_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
    APP_ID = "1035694033279278134"

    search_params = {
        "format" : "json",
        "keyword" : search_keyword,
        "applicationId" : [APP_ID],
        "availability" : 1,
        "hits" : 30,
        "page" : 1,

    }

    response = requests.get(RAKUTEN_PRODUCT_URL, search_params)
    response = response.json()

    assert response["Items"]

    for product_list in response["Items"]:

        tmp = str(product_list["Item"]["rank"]) + ": " + product_list["Item"]["itemName"] + "\r\n"

        with open("output.csv", mode='a', encoding="utf8") as f:
            f.write(tmp)
            f.close

if __name__ == "__main__":
    search_keyword = "米"
    write_products_list_to(search_keyword)

