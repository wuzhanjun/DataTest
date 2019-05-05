# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
import os
from Pm25pro.optMysql import  Sql

class Pm25ProPipeline(object):
    def process_item(self, item, spider):
        try:
            Sql.insert_pm25(item)
        except Exception as ex:
            print(ex.args)
        return item

    def close_spider(self,item,spider):
        Sql.closeMysql()