from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import scrapy,time
from scrapy import Request
import requests
from Pm25pro.items import Pm25ProItem

class MySpider(CrawlSpider):
    name = 'pm25'
    allowed_domains = ['www.pm25.com']
    start_urls = ['http://www.pm25.com']
    rules = (
        Rule(LinkExtractor(allow=(r'/rank.html')),
            follow = True,
            callback = 'parse_item',
             ),
    )

    @staticmethod
    def parse_item(response):
        # 获取网站div的所有内容
        allHtmlData = response.xpath('//div[@class="pj_area_data rank_data"]/ul[@class="pj_area_data_details rrank_box"]/li')
        # print(len(allHtmlData))
        try:
            for pItem in allHtmlData:
                pmData = {}
                pmData['pmTime'] = pItem.xpath('//div[@class="rank_banner"]/div[@class="rank_banner_right"]/span/text()').extract_first()
                pmData['airCondition'] = pItem.xpath('.//span[@class="pjadt_quality"]/em/text()').extract_first()
                pmData['city'] = pItem.xpath('.//a/text()').extract_first()
                pmData['province'] = pItem.xpath('.//span[@class="pjadt_sheng"]/text()').extract_first()
                pmData['AQI'] = pItem.xpath('.//span[@class="pjadt_aqi"]/text()').extract_first()
                pmData['pmConcentration'] = pItem.xpath('.//span[@class="pjadt_pm25"]/text()').extract_first()
                print(pmData)
                yield pmData
                pass
        except Exception as ex:
            print(ex.args)
            pass
        pass