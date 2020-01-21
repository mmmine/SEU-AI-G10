# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#定义爬取字段
class CourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    课程名称 = scrapy.Field()
    培训机构 = scrapy.Field()
    费用 = scrapy.Field()
    课程参与人数 = scrapy.Field()
