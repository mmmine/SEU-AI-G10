# -*- coding: utf-8 -*-
import scrapy


class ClassspiderSpider(scrapy.Spider):
    name = 'classSpider'
    allowed_domains = ['qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1']

    def parse(self, response):
        datalist = response.xpath(
            "//div[@class='market-bd market-bd-6 course-list course-card-list-multi-wrap js-course-list']//li")
        for data in datalist:
            item = {}
            if data.xpath(".//h4//a/text()").extract_first() != None:
                item["name"] = data.xpath(".//h4//a/text()").extract_first()
                item["institution"] =data.xpath(".//div[@class='item-line item-line--middle']//a/text()").extract_first()
                item["price($)"] = data.xpath(
                    ".//span[@class='line-cell item-price  custom-string']/text()").extract_first()
                item["Number of people purchased"] = data.xpath(
                    "normalize-space(.//span[@class='line-cell item-user custom-string']/text())").extract_first()
                yield item
        # 找到下一页的url地址
        next_url = response.xpath("//a[@class='page-next-btn icon-font i-v-right']/@href").extract_first()
        if next_url != "javascript:void(0);" and next_url != None:
            # 通过yield把地址包装成Request请求传向引擎
            yield scrapy.Request(next_url, callback=self.parse)
