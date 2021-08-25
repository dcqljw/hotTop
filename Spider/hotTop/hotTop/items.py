# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HottopItem(scrapy.Item):
    collection = tabel = "HotTop"
    id = scrapy.Field()
    idx = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()


class HotTopDateItem(scrapy.Item):
    collection = table = "HotTopDate"
    id = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
