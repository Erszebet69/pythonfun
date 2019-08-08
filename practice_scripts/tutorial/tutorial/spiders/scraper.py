# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "bnc"
    start_urls = [
        'https://www.bnc.ca'
    ]

    def parse(self, response):
        for link in response.css('p.chapeau3'):
            yield {
                'text': link.css('a::attr(href)').get(),
                #'author': quote.css('small.author::text').get(),
               #'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)