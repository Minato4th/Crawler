# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapItem(scrapy.Item):
    # define the fields for your item here like:
    asin = scrapy.Field()
    product_name = scrapy.Field()
    price = scrapy.Field()
    number_of_reviews = scrapy.Field()
    number_of_stars = scrapy.Field()
    # pass
