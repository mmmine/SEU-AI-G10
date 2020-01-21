# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class CoursePipeline(object):
	def __init__(self):
		self.conn = pymysql.connect(host="127.0.0.1",
									user="root",
									password="apple321",
									db="keqq")

	def process_item(self, item, spider):
		name=item["课程名称"]
		users=item["课程参与人数"]
		price=item["费用"]
		agency=item["培训机构"]
		cursor = self.conn.cursor()
		sql="insert into course_qq(name,users,price,agency) values('"+name+"','"+users+"','"+ price+"','"+agency+"');"
		cursor.execute(sql)
		self.conn.commit()
		return item

	def close_spider(self,spider):
		self.conn.close()