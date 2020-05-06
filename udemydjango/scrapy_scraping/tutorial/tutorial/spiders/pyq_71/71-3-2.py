import scrapy

# 複数のURLからファイルを取得する


class MultipleSpider(scrapy.Spider):
    name = 'multiple'
    allowed_domain = ['docs.pyq.jp']
    start_urls = [
        'https://docs.pyq.jp/_static/assets/scraping/test1.html',
        'https://docs.pyq.jp/_static/assets/scraping/test2.csv',
    ]

    def parse(self, response):
        print(response.url)
        print(response.text)
