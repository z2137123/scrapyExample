# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ngaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topic = scrapy.Field()
    link = scrapy.Field()
    replies = scrapy.Field()
    id = scrapy.Field()
    replies = scrapy.Field()
    context = scrapy.Field()
   
