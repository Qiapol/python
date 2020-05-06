import requests
from bs4 import BeautifulSoup

# HTMLの取得
url = 'https://docs.pyq.jp/_static/assets/scraping/item-list.html'
html = requests.get(url)
html.encoding = html.apparent_encoding

# リストの準備
stock_list = []  # 在庫数の格納
price_list = []  # 価格の格納

# HTML解析
soup = BeautifulSoup(html.content, 'html.parser')
div_item_list = soup.select('div.item-list')
for div_item in div_item_list[0].select('div.item'):
    # 在庫の取得
    item_stock_tag = div_item.select_one('span.item-stock')
    item_stock = item_stock_tag.text.strip()
    if item_stock != '無し':
        # 価格の取得
        item_price_tag = div_item.select_one('span.item-price')
        item_price = item_price_tag.text.strip()

        # 以下はsum()できる形にデータを整形

        # item_price:'円'、','を取り除く
        item_price = item_price.replace('円', '').replace(',', '')

        # item_stock:'個',','を取り除く
        item_stock = item_stock.replace('個', '').replace(',', '')

        # リストに追加する
        stock_list.append(int(item_stock))
        price_list.append(int(item_price))

# 表示
print(f'合計在庫数：{sum(stock_list)}個')
print(f'合計金額：{sum(price_list)}円')
