# CSVの取得

import requests

# 取得したいCSVのURLを書きます
url = "https://docs.pyq.jp/_static/assets/scraping/test2.csv"

# HTTPリクエストを送信してCSVを取得します
response = requests.get(url)
response.encoding = response.apparent_encoding

# 取得したCSVを表示します
print(response.text)
