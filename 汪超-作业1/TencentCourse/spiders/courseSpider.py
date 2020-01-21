# -*- coding: utf-8 -*-
import scrapy
from .. import Util
from .. import items


class courseSpider3(scrapy.Spider):
    name = 'courseSpider'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/course/list?mt=1001']
    category = Util.getCategory()
    cate_id, cate_link = next(category)

    def parse(self, response):
        select = response.xpath("//section[1]/div/div[3]/ul/li")
        print("############# select_len", len(select))
        i = 0;

        while True:
            # 解析24个课程
            for course in select:
                item = items.Course()
                item["category"] = self.cate_id
                item["course_name"] = course.xpath("h4/a/text()").get()
                item["course_link"] = course.xpath("h4/a/@href").get()
                item["course_img"] = course.xpath("a/img/@src").get()
                item["course_price"] = course.xpath("div[2]/span[1]/text()").get()
                item["course_source"] = course.xpath("div[1]/a/text()").get()
                item["course_tag"] = "tag"
                print("############## ", item["course_name"])
                yield item

            # 产生下一页
            next_page_item = response.xpath("//section[1]/div/div[5]/a[6]/@href").get()
            print("############# next_page_item: ", next_page_item)

            if next_page_item == "javascript:void(0);":
                break;

            if next_page_item is not None:
                print("### 进入下一页")
                yield scrapy.Request(next_page_item, callback=self.parse)

            # i+=1

        # 爬取下一类
        try:
            self.cate_id, self.cate_link = next(self.category)
            url = "http://" + self.allowed_domains[0] + "/course/list?" + self.cate_link
            print("### request, url: ", url)
            yield scrapy.Request(url, callback=self.parse)
        except StopIteration:
            print("########### 进入下一类")
            pass












