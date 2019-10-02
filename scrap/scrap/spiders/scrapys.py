import re

import scrapy

from ..items import ScrapItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.de/gp/bestsellers/ce-de/ref=zg_bs_nav_0/261-1162755-1928137']

    def parse(self, response):
        products = ScrapItem()

        regex_asin = re.compile("dp/(.*)?_")

        all_items_in_lo = response.css('li.zg-item-immersion')
        for item in all_items_in_lo:
            products['asin'] = regex_asin.search(str(item.css('.a-link-normal ::attr(href)')[0].extract())).group(1)[
                               :-1]
            products['product_name'] = str(item.css('.a-section .a-spacing-small img::attr(alt)').extract()).strip(
                '[').strip(']').strip('\'')
            products['price'] = str(item.css('.p13n-sc-price::text').extract())[:-7].strip('[').strip(']').strip(
                '\'').strip('\"')
            products['number_of_reviews'] = str(item.css('.a-size-small.a-link-normal::text').extract()).strip(
                '[').strip(']').strip('\'')
            products['number_of_stars'] = str(item.css('.a-icon-alt::text').extract())[:5].strip('[').strip(']').strip(
                '\'').strip('\"')

            yield products

        for href in response.css('li.a-last a::attr(href)'):
            yield response.follow(href, self.parse)
