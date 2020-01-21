import scrapy
from TencentclassSpider.items import TencentclassspiderItem
from time import sleep
import re

class classSpider(scrapy.Spider):
    name = 'all_class'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list?page=1']  #首页网址
    url = "https://ke.qq.com/course/list?page="   #翻页前缀
    page_num = 1  #翻页起始数


    def parse(self, response):

        # 记录获取信息
        names = []
        organizations = []
        links = []
        numbers = []
        statuses = []
        prices = []

        result = response.xpath('//section[1]/div/div[3]/ul/li')

        self.page_num += 1

        for class_ in result:
            # 课程名称
            name = class_.xpath('h4/a/text()').get()
            names.append(name)

            # 培训机构
            organization = class_.xpath('div[@class="item-line item-line--middle"]/a/text()').get()
            organizations.append(organization)

            # 课程链接
            link = class_.xpath('a/@href').get()
            links.append(link)

            # 报名人数
            number = class_.xpath('div[@class="item-line item-line--bottom"]/span[@class="line-cell item-user custom-string"]/text()').get().strip()
            rule = str.maketrans("0123456789", "4602718935")
            number = number.translate(rule)
            number_list = re.findall('\d+', number)
            number = number_list[0]
            numbers.append(number)

            # 课程情况
            status = class_.xpath('div[@class="item-line item-line--middle"]/span/text()').get()
            statuses.append(status)

            # 课程价格
            price = class_.xpath('div[@class="item-line item-line--bottom"]/span[1]/text()').get().strip()
            price = price.translate(rule)
            if(price.find("免费") >= 0):
                price = 0
            else:
                price_list = re.findall('\d+', price )
                price = price_list[0]
            prices.append(price)

        #获取下一页链接
        next_url = self.url + str(self.page_num)
        sleep(0.5)

        #存入items容器
        for i in range(len(names)):  # for循环列表的长度，获取到所有信息
            info = TencentclassspiderItem()  # 实例一个类info用来保存数据
            info["name"] = names[i]  # 将每一个属性列表中的每一个数据保存依次保存到info中去
            info["organization"] = organizations[i]
            info["link"] = links[i]
            info["number"] = numbers[i]
            info["status"] = statuses[i]
            info["price"] = prices[i]
            yield info


        if self.page_num <= 416 : #416为最后一页
            yield scrapy.Request(next_url,callback = self.parse)




