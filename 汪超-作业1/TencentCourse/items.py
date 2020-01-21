# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentcourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 课程名称
    course_name = scrapy.Field()
    # 培训机构
    course_organization = scrapy.Field()
    # 课程连接
    course_link = scrapy.Field()
    # 报名人数
    course_number = scrapy.Field()
    # 课程状态
    course_status = scrapy.Field()
    # 课程价格
    course_price = scrapy.Field()


class CourseCategories(scrapy.Item):
    category_name = scrapy.Field()
    category_link = scrapy.Field()


class SubCourseCategories(scrapy.Item):
    parent = scrapy.Field()
    category_name = scrapy.Field()
    category_link = scrapy.Field()


class Course(scrapy.Item):
    category = scrapy.Field()
    course_name = scrapy.Field()
    course_link = scrapy.Field()
    course_img = scrapy.Field()
    course_price = scrapy.Field()
    course_num = scrapy.Field()
    course_source = scrapy.Field()  # 来源
    course_tag = scrapy.Field()     # 标签

