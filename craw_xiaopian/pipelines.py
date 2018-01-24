# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from craw_xiaopian.util.db import con


class CrawXiaopianPipeline(object):
    def process_item(self, item, spider):
        return item


def checkTitleFromDb(title):
    cursor = con.cursor()
    sqlStr = "select title from xiaopian_video where title ='"+title+"'"
    cursor.execute(sqlStr)
    d = cursor.fetchone()
    return d

class insertDbPipeline(object):
    '''
    将内容保存到数据库中
    '''

    def process_item(self, item, spider):
        # 使用cursor()方法获取操作游标
        cursor = con.cursor(pymysql.cursors.DictCursor)
        row = checkTitleFromDb(item['title'])
        if row:
            return
        else:
            sql = (
            "insert into xiaopian_video(title, relese_date, click_num, yiming, pianming,niandai,chandi,leibie,yuyan,zimu,shangyingriqi,wenjiandaxiao,pianchang,daoyan,zhuyan,download_url)""values( %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s,%s,%s)")
            lis = (item['title'], item['relese_date'], item['click_num'], item['yiming'], item['pianming'], item['niandai'],item['chandi'], item['leibie'], item['yuyan'],item['zimu'], item['shangyingriqi'], item['wenjiandaxiao'],item['pianchang'], item['daoyan'], item['zhuyan'] ,item['download_url'])
            cursor.execute(sql, lis)
            con.commit()
            # cursor.close()
            # con.close()
            return item