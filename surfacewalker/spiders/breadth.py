import scrapy


class Breadth(scrapy.Spider):
    name = 'breadth'

    def parse(self, response):
        for href in response.css('a ::attr(href)'):
            yield scrapy.Request(response.urljoin(href.extract_first()))
