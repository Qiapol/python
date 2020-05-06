import requests
from bs4 import BeautifulSoup

# HTMLファイルの取得
url = 'https://docs.pyq.jp/_static/assets/scraping/item-list.html'
html = requests.get(url)
html.encoding = html.apparent_encoding
soup = BeautifulSoup(html.content, 'html.parser')

# タグで目的のデータを取り出すために絞り込む
# まずは大枠として、商品リストの大きな枠を持ってくる
div_item_list = soup.select('div.item-list')

# その中で、個々の商品の枠を持ってくる
for div_item in div_item_list[0].select('div.item'):
    # 商品名を取得
    item_name_tags = div_item.select('a.item-name')
    item_name_tag = item_name_tags[0]
    item_name = item_name_tag.text.strip()

    # 値段を取得
    item_price_tags = div_item.select('span.item-price')
    item_price_tag = item_price_tags[0]
    item_price = item_price_tag.text.strip()

    # 表示
    print('商品名: {} 価格: {}'.format(item_name, item_price))
