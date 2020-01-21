# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class TencentCategoriesPipeline(object):
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456', 'tencentcourse')
        # 创建游标
        self.cursor = self.conn.cursor()

        # if spider.name == "categorySpider":
        #     sql = "DELETE from categories"
        #     self.cursor.execute(sql)
        #     self.conn.commit()

    def process_item(self, item, spider):
        if spider.name == "categorySpider":
            print("### categorySpider-pipeline")

            sql = "insert into categories values(NULL, %s, %s)"
            link = item["category_link"]

            self.cursor.execute(sql, (item["category_name"], link[link.index("?") + 1 :]))
            self.conn.commit()

        if spider.name == "courseSpider":
            print("### courseSpider-pipeline")
            sql = "insert into course values(NULL, %s, %s, %s, %s, %s, %s, %s)"

            # self.cursor.execute(sql, (item.category, item.course_name, item.course_link, item.course_img,
            #                           item.course_price, item.course_source, item.course_tag))

            self.cursor.execute(sql, (item["category"], item["course_name"], item["course_link"], item["course_img"],
                                      item["course_price"], item["course_source"], item["course_tag"]))
            self.conn.commit()


class TencentSubCategoriesPipeline(object):
    def process_item(self, item, spider):
        print("##pipeline###########################################################################")

        sql = "insert into categories values(NULL, %s, %s)"
        link = item["category_link"]

        self.cursor.execute(sql, (item["category_name"], link[link.index("?") + 1 :]))
        self.conn.commit()
