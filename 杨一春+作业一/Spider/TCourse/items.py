# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re

def number_processor(s):
    reg = '\d+[\.]?\d*'
    return re.search(reg, s[0]).group()

def price_processor(s):
    reg = '\d+[\.]?\d*'
    if s[0] == '免费':
        return ['0']
    else:
        return re.search(reg, s[0]).group()

class CourseItem(scrapy.Item):
    first_index = scrapy.Field()
    second_index = scrapy.Field()
    third_index = scrapy.Field()
    cname = scrapy.Field()
    company = scrapy.Field()
    link = scrapy.Field()
    number = scrapy.Field(input_processor = number_processor)
    price = scrapy.Field(input_processor = price_processor)



