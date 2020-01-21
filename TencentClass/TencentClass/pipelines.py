# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TencentclassPipeline(object):
    def process_item(self, item, spider):
        if type(item["price($)"]) == str:
            price = ""
            for index in range(len(item["price($)"])):
                if item["price($)"][index] == '1':
                    price += "6"
                if item["price($)"][index] == "2":
                    price += "0"
                if item["price($)"][index] == '3':
                    price += "2"
                if item["price($)"][index] == "4":
                    price += "7"
                if item["price($)"][index] == '5':
                    price += "1"
                if item["price($)"][index] == "6":
                    price += "8"
                if item["price($)"][index] == '7':
                    price += "9"
                if item["price($)"][index] == "8":
                    price += "3"
                if item["price($)"][index] == '9':
                    price += "5"
                if item["price($)"][index] == "0":
                    price += "4"
                if item["price($)"][index] == '.':
                    price += '.'
            item["price($)"] = price
        number = ""
        for index in range(len(item["Number of people purchased"])):
            if item["Number of people purchased"][index] == '1':
                number += "6"
            if item["Number of people purchased"][index] == "2":
                number += "0"
            if item["Number of people purchased"][index] == '3':
                number += "2"
            if item["Number of people purchased"][index] == "4":
                number += "7"
            if item["Number of people purchased"][index] == '5':
                number += "1"
            if item["Number of people purchased"][index] == "6":
                number += "8"
            if item["Number of people purchased"][index] == '7':
                number += "9"
            if item["Number of people purchased"][index] == "8":
                number += "3"
            if item["Number of people purchased"][index] == '9':
                number += "5"
            if item["Number of people purchased"][index] == "0":
                number += "4"
        item["Number of people purchased"] = number
        print(item)
        return item
