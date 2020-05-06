# BeautifulSoupを使用したHTMLタグの解析
# 71-1で取得したHTMLファイルからタグを使用して、目的のデータを取得する

import requests
from bs4 import BeautifulSoup

# 目的URLからHTMLファイルを取得する
url = 'https://docs.pyq.jp/_static/assets/scraping/parse1.html'
html = requests.get(url)
html.encoding = html.apparent_encoding

# BeautifulSoupでHTMLの解析をする
soup = BeautifulSoup(html.text, 'html.parser')

# ulタグで囲まれた部分を抽出
ul_tag = soup.find('ul')

# 更にaタグで絞る
for a_tag in ul_tag.find_all('a'):

    # a_tagのテキスト部分を抽出
    a_tag_text = a_tag.text

    # a_tagのhref属性を抽出
    a_tag_href = a_tag['href']

    # 表示
    print(f'{a_tag_text}: {a_tag_href}')
