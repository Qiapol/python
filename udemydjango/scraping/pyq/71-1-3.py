# 1回のpythonファイル実行で複数のファイルを取得する
# time.sleepを実装する

import time
import requests

# 取得したいURL書きましょう
url_html = 'https://docs.pyq.jp/_static/assets/scraping/test1.html'
url_csv = 'https://docs.pyq.jp/_static/assets/scraping/test2.csv'
# HTMLの取得と表示
response = requests.get(url_html)
response.encoding = response.apparent_encoding

print("HTMLの取得と表示 ----")
print(response.text)

# 1秒スリープ
time.sleep(1)

# CSVの取得と表示
response = requests.get(url_csv)
response.encoding = response.apparent_encoding

print("CSVの取得と表示 ----")
print(response.text)
