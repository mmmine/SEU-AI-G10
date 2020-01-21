# -*- coding: utf-8 -*-
import scrapy
import course.items

class AllcourseSpider(scrapy.Spider):
    name = 'allcourse'
    allowed_domains = ['ke.qq.com']
    page_number = 1
    urls = 'https://ke.qq.com/course/list?page=%d'

    def start_requests(self):
        url = self.urls % self.page_number
        request = scrapy.Request(
            url=url, method='get', 
            callback=self.parse_pos, errback=self.parse_error, 
            dont_filter=True)
        yield request

    def parse_pos(self, response):
        print("提取课程数据")
        course_list = response.xpath('//div[@class="market-bd market-bd-6 course-list course-card-list-multi-wrap js-course-list"]/ul/li')
        for course_offering in course_list:
            item = course.items.CourseItem()
            item['课程名称'] = course_offering.xpath('h4/a/text()').get()
            item['培训机构'] = course_offering.xpath('div/a/text()').get()
            item['费用'] = course_offering.xpath('div[@class="item-line item-line--bottom"]/span/text()').get()
            item['课程参与人数'] = course_offering.xpath('div[@class="item-line item-line--bottom"]/span[@class="line-cell item-user custom-string"]/text()').get().replace(" ", "")
            item['课程参与人数'] = item['课程参与人数'].strip('\n')
            yield item
        
        self.page_number += 1
        url = self.urls % self.page_number
        request = scrapy.Request(
            url=url, method='get', 
            callback=self.parse_pos, errback=self.parse_error, 
            dont_filter=True)
        yield request
            
    def parse_error(self, error):
        print("处理爬取异常")