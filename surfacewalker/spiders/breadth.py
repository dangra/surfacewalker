import scrapy


class Breadth(scrapy.Spider):
    name = 'breadth'
    #start_urls = ('file://top500-seed.txt',)

    def parse(self, response):
        for href in response.css('a ::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href))
