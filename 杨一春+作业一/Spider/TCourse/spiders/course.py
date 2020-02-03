# -*- coding: utf-8 -*-
import scrapy
import scrapy.loader
from urllib.parse import urljoin
from First.items import CourseItem


def GetIndexName(i, level):
    if(level == 2):
        return i.xpath('a/@title').get()
    return i.xpath('a/h2/text()').get()



class CourseSpider(scrapy.Spider):
    name = 'course'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list']
    download_delay = 1




    def parse(self, response):
        level = -1
        yield scrapy.Request(url = self.start_urls[0], callback = lambda respomse, l = level + 1: self.parse_index(response, l))

    #level = 0/1/2
    def parse_index(self, response, level):
        result = response.xpath('//*[@id="auto-test-1"]/div[1]/dl/dd')
        for i in result:
            next_url = urljoin(response.url, i.xpath('a/@href').get())
            if next_url == response.url:
                continue

            if level == 2:
                yield scrapy.Request(url = next_url, callback = self.parse_course)
            else:
                yield scrapy.Request(url = next_url, callback = lambda next_resp, l = level + 1: self.parse_index(next_resp, l))

    
    def parse_course(self, response):   #最终爬取课程
        result = response.xpath('//section[1]/div/div[3]/ul/li')
        
        for i in result:
            ri = CourseItem()      #定义在items中
            load = scrapy.loader.ItemLoader(item = ri, selector = i)
            
            load.add_xpath('first_index', '//section[1]/div/nav/div[1]/a/@title')

            load.add_xpath('second_index', '//section[1]/div/nav/div[2]/a/@title')

            load.add_xpath('third_index', '//*[@id="auto-test-1"]/div[1]/dl/dd[@class = "curr"]/a/@title')

            load.add_xpath('cname', 'h4/a/text()')

            load.add_xpath('company', 'div[1]/a/text()')
            
            load.add_xpath('link', 'h4/a/@href')

            load.add_xpath('number', 'div[2]/span[@class = "line-cell item-user custom-string"]/text()')

            load.add_xpath('price', 'div[2]/span[1]/text()')

            yield load.load_item()  #item项处理再items.py中

        next_page = response.xpath('//section[1]/div/div[5]/a[@class="page-next-btn icon-font i-v-right"]/@href').get()
        if next_page:
            yield scrapy.Request(url = next_page, callback = self.parse_course)


'''
            ri = CourseItem(first_index = first, 
                             second_index = second,
                             third_index = third, 
                             cname = name,
                             company = ccompany,
                             clink = link,
                             cnumber = number,
                             cprice = price)

'''





