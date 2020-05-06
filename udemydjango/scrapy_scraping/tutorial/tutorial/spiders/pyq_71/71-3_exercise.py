from datetime import datetime
import scrapy

# 定数
FROM_DATE = datetime(2017, 5, 1)
TO_DATE = datetime(2017, 9, 1)
STRPTIME_FORMAT = '%Y-%m-%d'


class EnsyuSpider(scrapy.Spider):
    name = 'ensyu'
    allowed_domains = ['docs.pyq.jp']
    start_urls = [
        'https://docs.pyq.jp/_static/assets/scraping/item-list.html'
    ]

    # ある期間の商品化判定し、商品ページに処理を飛ばすまでの処理を定義
    def parse(self, response):
        # 発売日を取得
        div_item_list = response.css('div.item-list')[0]
        for div_item in div_item_list.css('div.item'):
            item_release_date = div_item.css('span.item-release-date::text').extract_first()
            datetime_item_release_date = datetime.strptime(item_release_date, STRPTIME_FORMAT)

            # ある期間の商品のみを取得
            if FROM_DATE <= datetime_item_release_date < TO_DATE:
                # 商品ページクロールのために商品URL取得
                item_url = div_item.css('a.item-name::attr(href)').extract_first()
                # 商品URLを個別にスクレイピング
                yield scrapy.Request(item_url, callback=self.parse_item_page)

    # 商品ページのスクレイピング処理を定義
    def parse_item_page(self, response):
        # 商品名の取得
        item_name = response.css('h1.item-name::text').extract_first()
        # 価格情報(int)の取得
        item_price = response.css('span.item-price::text').extract_first()
        item_price = int(item_price.replace(',', '').replace('円', ''))

        # 発売日の取得
        item_release_date = response.css('span.item-release-date::text').extract_first()

        # 辞書item_info作成(return作成)
        item_info = {
            '商品名': item_name,
            '価格': item_price,
            '発売日': item_release_date,
        }

        return item_info
