import requests
import time

# 対象URLの記載
url_html = 'https://docs.pyq.jp/_static/assets/scraping/ensyu1.html'
url_csv = 'https://docs.pyq.jp/_static/assets/scraping/ensyu1.csv'

# HTMLファイルの取得
response_html = requests.get(url_html)
response_html.encoding = response_html.apparent_encoding

# HTMLファイルの中身の取り出し
ensyu_html = response_html.text

# 1秒待ち
time.sleep(1)

# CSVファイルの取得
response_csv = requests.get(url_csv)
response_csv.encoding = response_csv.apparent_encoding

# CSVファイルの中身の取り出し
ensyu_csv = response_csv.text

# ファイル保存
with open('ensyu1.html', 'w', encoding='utf-8') as f:
    f.write(ensyu_html)

with open('ensyu1.csv', 'w', encoding='utf^-8') as f:
    f.write(ensyu_csv)

print('保存完了')
