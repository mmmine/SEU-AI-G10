# -*- coding: utf-8 -*-
import scrapy
# from items import CourseCategories
from .. import items


class CategoryspiderSpider(scrapy.Spider):
    name = 'categorySpider'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list']

    def parse(self, response):
        categories = response.xpath('//*[@id="auto-test-1"]/div[1]/dl/dd[position()>1]/a/h2/text()')
        href = response.xpath('//*[@id="auto-test-1"]/div[1]/dl/dd[position()>1]/a/@href')
        items_ = []

        if len(categories) == len(href):
            for m, n in zip(categories, href):
                item = items.CourseCategories()
                item["category_name"] = m.get().strip()
                item["category_link"] = n.get().strip()
                items_.append(item)

        for item in items_:
            print("name:\n ", item["category_name"], "link: \n ", item["category_link"])
        return items_

