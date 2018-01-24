# -*- coding: utf-8 -*-
import re
import string

import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector


from craw_xiaopian.items import CrawXiaopianItem


class NewsSpider(Spider):
    name = 'xiaopian'
    allowed_domains = ['www.dy2018.com']
    start_urls = ['http://www.dy2018.com/html/gndy/dyzz/index.html']

    def parse(self, response):
        for page in range(1,296):
            url = 'http://www.dy2018.com/html/gndy/dyzz/index_'+str(page+1)+'.html'
            # print(url)
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        sel = Selector(response)
        all_ul = sel.xpath('//*[@class="tbspan"]')
        if all_ul:
            for ul in all_ul:
                item = CrawXiaopianItem()
                title = ul.xpath('tr[2]/td[2]/b/a/text()').extract()
                relese_date = ul.xpath('tr[3]/td[2]/font/text()').extract()
                d_char = relese_date[0].split(' ')
                rq = d_char[0].split('：')
                dj = d_char[1].split('：')
                item['relese_date'] = rq[1]
                item['click_num'] = dj[1]
                url = ul.xpath('tr[2]/td[2]/b/a/@href').extract()

                item['title'] = title[0]
                item['link'] = 'http://www.dy2018.com'+str(url[0])
                yield scrapy.Request(url=item['link'], meta={'item': item}, callback=self.parse_detail,
                                     dont_filter=True)

    def parse_detail(self, response):
            item = response.meta['item']
            yiming = response.xpath('//*[@id="Zoom"]/p[2]/text()').extract()
            if not len(yiming):
                yiming = '暂无'
            pianming = response.xpath('//*[@id="Zoom"]/p[3]/text()').extract()
            if not len(pianming):
                pianming = '暂无'
            niandai = response.xpath('//*[@id="Zoom"]/p[4]/text()').extract()
            if not len(niandai):
                niandai = '暂无'
            chandi = response.xpath('//*[@id="Zoom"]/p[5]/text()').extract()
            if not len(chandi):
                chandi = '暂无'
            leibie = response.xpath('//*[@id="Zoom"]/p[6]/text()').extract()
            if not len(leibie):
                leibie = '暂无'
            yuyan = response.xpath('//*[@id="Zoom"]/p[7]/text()').extract()
            if not len(yuyan):
                yuyan = '暂无'
            zimu = response.xpath('//*[@id="Zoom"]/p[8]/text()').extract()
            if not len(zimu):
                zimu = '暂无'
            shangyingriqi = response.xpath('//*[@id="Zoom"]/p[9]/text()').extract()
            if not len(shangyingriqi):
                shangyingriqi = '暂无'
            wenjiandaxiao = response.xpath('//*[@id="Zoom"]/p[14]/text()').extract()
            if not len(wenjiandaxiao):
                wenjiandaxiao = '暂无'
            pianchang = response.xpath('//*[@id="Zoom"]/p[15]/text()').extract()
            if not len(pianchang):
                pianchang = '暂无'
            daoyan = response.xpath('//*[@id="Zoom"]/p[16]/text()').extract()
            if not len(daoyan):
                daoyan = '暂无'
            zhuyan = response.xpath('//*[@id="Zoom"]/p[17]/text()').extract()
            if not len(zhuyan):
                zhuyan = '暂无'

            item['yiming'] =yiming
            item['pianming']  = pianming
            item['niandai'] = niandai
            item['chandi'] = chandi
            item['leibie'] = leibie
            item['yuyan'] = yuyan
            item['zimu'] = zimu
            item['shangyingriqi'] = shangyingriqi
            item['wenjiandaxiao'] = wenjiandaxiao
            item['pianchang'] = pianchang
            item['daoyan'] = daoyan
            item['zhuyan'] = zhuyan

            ftp = response.xpath('//tr/td/a/text()').extract()
            if ftp:
                download_url = ''
                for t in ftp:
                    print(t)
                    if t.find('ftp')>=0:
                        download_url = download_url+" "+ t
                item['download_url'] = download_url
                yield item

    @staticmethod
    def getContent(content):
        co = ''
        for i in range(len(content)):
            co += content[i]
        return co

    def find_string(s, t):
        try:
            string.index(s, t)
            return True
        except(ValueError):
            return False