# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class CrawXiaopianItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = Field()
    title = Field()
    relese_date = Field()
    click_num = Field()
    download_url = Field()
    yiming = Field()
    pianming = Field()
    niandai = Field()
    chandi = Field()
    leibie = Field()
    yuyan = Field()
    zimu = Field()
    shangyingriqi = Field()
    wenjiandaxiao = Field()
    pianchang = Field()
    daoyan = Field()
    zhuyan = Field()
