# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Pm25ProItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 统计时间
    pmTime = scrapy.Field()
    # 空气质量状况
    airCondition = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 省份
    province = scrapy.Field()
    # AQI
    AQI = scrapy.Field()
    # pm2.5浓度
    pmConcentration = scrapy.Field()
    pass
