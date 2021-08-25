import scrapy
from hotTop.items import HottopItem, HotTopDateItem
from hotTop.utils import util


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], self.parse)

    def parse(self, response):
        tops = response.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
        idx = 1
        date = util.getNowDate()
        dateItem = HotTopDateItem()
        dateItem["date"] = date
        dateItem["source"] = self.name
        baseUrl = "https://s.weibo.com"
        for top in tops:
            ranktop = top.xpath("td/@class").extract_first().split(" ")
            if "ranktop" in ranktop:
                item = HottopItem()
                item["idx"] = idx
                title = top.xpath("td[2]/a/text()").extract_first()
                if title != "•":
                    item["title"] = title
                    item["url"] = baseUrl + top.xpath("td[2]/a/@href").extract_first()
                    item["date"] = date
                    item["source"] = self.name
                    idx += 1
                    yield item
        yield dateItem
