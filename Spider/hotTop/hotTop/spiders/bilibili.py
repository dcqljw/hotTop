import scrapy
from hotTop.items import HottopItem, HotTopDateItem
from hotTop.utils import util


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://s.search.bilibili.com/main/hotword']

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], self.parse)

    def parse(self, response):
        results = response.json()["list"]
        idx = 1
        date = util.getNowDate()
        dateItem = HotTopDateItem()
        dateItem["date"] = date
        dateItem["source"] = self.name
        for result in results:
            item = HottopItem()
            item["idx"] = idx
            item["title"] = result["keyword"]
            item["url"] = "https://search.bilibili.com/all?keyword=" + result["keyword"]
            item["date"] = date
            item["source"] = self.name
            idx += 1
            yield item
        yield dateItem

