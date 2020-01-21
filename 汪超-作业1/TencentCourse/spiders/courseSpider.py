# -*- coding: utf-8 -*-
import scrapy
from .. import Util
from .. import items
import re


class courseSpider3(scrapy.Spider):
    name = 'courseSpider'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/course/list?mt=1001']
    category = Util.getCategory()
    cate_id, cate_link = next(category)

    def parse(self, response):
        select = response.xpath("//section[1]/div/div[3]/ul/li")
        i = 0;

        while True and i < 34:
            # 解析24个课程
            for course in select:
                item = items.Course()
                item["category"] = self.cate_id
                item["course_name"] = course.xpath("h4/a/text()").get()
                item["course_link"] = course.xpath("h4/a/@href").get()
                item["course_img"] = course.xpath("a/img/@src").get()
                item["course_price"] = course.xpath("div[2]/span[1]/text()").get()
                course_num = course.xpath("div[2]/span[2]/text()").get()
                item["course_num"] = re.findall("\\d+", course_num)
                item["course_source"] = course.xpath("div[1]/a/text()").get()
                item["course_tag"] = "tag"
                yield item

            # 产生下一页
            i += 1
            next_page_item = response.xpath("//section[1]/div/div[5]/a[6]/@href").get()

            if next_page_item == "javascript:void(0);":
                break

            if next_page_item is not None:
                yield scrapy.Request(next_page_item, callback=self.parse)

        # 爬取下一类
        try:
            self.cate_id, self.cate_link = next(self.category)
            url = "http://" + self.allowed_domains[0] + "/course/list?" + self.cate_link
            yield scrapy.Request(url, callback=self.parse)
        except StopIteration:
            pass












