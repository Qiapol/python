# HTMLの取得

import requests
# 取得したいURLを書きます
url = "https://docs.pyq.jp/_static/assets/scraping/test1.html"

# HTTPリクエストを送信してHTMLを取得します
response = requests.get(url)
response.encoding = response.apparent_encoding

# 取得したHTMLを表示します
print(response.text)
