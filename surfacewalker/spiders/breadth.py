import csv
import scrapy
from cStringIO import StringIO


class Breadth(scrapy.Spider):
    name = 'breadth'

    def start_requests(self):
        yield scrapy.Request('https://moz.com/top500/domains/csv',
                             callback=self.parse_top500)

    def parse_top500(self, response):
        reader = csv.reader(StringIO(response.body))
        for row in reader:
            url = 'http://' + row[1].strip('"')
            yield scrapy.Request(url)

    def parse(self, response):
        yield {'url': response.url}
        depth = response.meta.get('depth', 0)
        if depth > 3:
            return

        for idx, href in enumerate(response.css('a ::attr(href)')):
            if idx > 10:
                return
            url = response.urljoin(href.extract())
            yield scrapy.Request(url)
