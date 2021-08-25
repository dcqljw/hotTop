import scrapy
from hotTop.items import HottopItem, HotTopDateItem
from hotTop.utils import util


class BilitopSpider(scrapy.Spider):
    name = 'biliTop'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/v/popular/rank/all']

    def start_requests(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        }
        yield scrapy.Request(self.start_urls[0], self.parse, headers=headers)

    def parse(self, response):
        tops = response.xpath('//*[@class="rank-item"]')
        idx = 1
        date = util.getNowDate()
        dateItem = HotTopDateItem()
        dateItem["date"] = date
        dateItem["source"] = self.name
        for top in tops:
            item = HottopItem()
            item["idx"] = idx
            item["title"] = top.xpath('div[2]/div[2]/a/text()').extract_first()
            item["url"] = top.xpath('div[2]/div[2]/a/@href').extract_first()
            item["date"] = date
            item["source"] = self.name
            idx += 1
            yield item
        yield dateItem

