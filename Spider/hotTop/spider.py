import os

spiders = os.popen("scrapy list")

for i in spiders:
    spider = i.replace("\n", "")
    cmd = "scrapy crawl " + spider
    os.system("scrapy crawl " + spider)
