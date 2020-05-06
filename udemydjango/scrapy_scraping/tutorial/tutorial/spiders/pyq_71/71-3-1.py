import scrapy

# スクレイピングフレームワークscrapyを使用する


class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domain = ['docs.pyq.jp']
    start_urls = [
        'https://docs.pyq.jp/_static/assets/scraping/test1.html'
    ]

    def parse(self, response):
        print(response.text)
