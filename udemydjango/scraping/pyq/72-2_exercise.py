import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 発売日(fromdate)
FROM_DATE = datetime(2017, 5, 1)
# 発売日(todate):指定したいtodateから+1日を指定
TO_DATE = datetime(2017, 9, 1)

# HTMLの取得
url = 'https://docs.pyq.jp/_static/assets/scraping/item-list.html'
html = requests.get(url)
html.encoding = html.apparent_encoding
soup = BeautifulSoup(html.content, 'html.parser')

# 発売日の取得
div_item_list = soup.select('div.item-list')

for div_item in div_item_list[0].select('div.item'):
    item_release_date = div_item.select_one('span.item-release-date').text.strip()
    datetime_item_release_date = datetime.strptime(item_release_date, '%Y-%m-%d')

    if FROM_DATE <= datetime_item_release_date < TO_DATE:
        # 商品名の取得
        item_name = div_item.select_one('a.item-name').text.strip()
        # 価格の取得
        item_price = div_item.select_one('span.item-price').text.strip()
        item_price = item_price.replace(',', '').replace('円', '')
        # 表示
        print(f'{item_name} {item_price}')
