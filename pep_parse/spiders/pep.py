import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep_link in response.css('tbody tr a[href^="pep-"]'):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        _, number, _, *name = response.css('h1.page-title::text').get().split()
        data = {
            'number': number,
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
