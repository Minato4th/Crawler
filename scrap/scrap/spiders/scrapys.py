import scrapy

from ..items import ScrapItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.de/gp/bestsellers/ce-de/ref=zg_bs_nav_0/261-1162755-1928137']

    def parse(self, response):
        products = ScrapItem()

        all_items_in_lo = response.css('li.zg-item-immersion')
        for item in all_items_in_lo:
            products['asin'] = item.xpath(
                "descendant-or-self::a[@class and contains(concat(' ', normalize-space(@class), ' '), ' a-link-normal ')]/@href").extract()
            products['product_name'] = item.css('.p13n-sc-truncate.p13n-sc-line-clamp-2::text').extract()
            products['price'] = item.css('.p13n-sc-price::text').extract()
            products['number_of_reviews'] = item.css('.a-size-small.a-link-normal::text').extract()
            products['number_of_stars'] = item.css('.a-icon-alt::text').extract()
            yield products

        for href in response.css('li.a-last a::attr(href)'):
            yield response.follow(href, callback=self.parse)
