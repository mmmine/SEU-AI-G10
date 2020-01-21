# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentclassspiderItem(scrapy.Item):
    # 课程名称
    name = scrapy.Field()
    # 培训机构
    organization = scrapy.Field()
    # 课程链接
    link = scrapy.Field()
    # 报名人数
    number = scrapy.Field()
    # 课程情况
    status = scrapy.Field()
    # 课程价格
    price = scrapy.Field()



