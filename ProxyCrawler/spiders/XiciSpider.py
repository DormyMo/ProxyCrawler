#coding:utf8
'''
Created on 2014-10-13

@author: modm
'''
from scrapy.spider import Spider
from scrapy.contrib.loader import ItemLoader
from scrapy import Selector
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy import log
from scrapy.http import Request, FormRequest
#=======================================
from ProxyCrawler.items import ProxycrawlerItem
import datetime

class Spider_xici(Spider):
    name = "xici"
    allowed_domains = ["xici.net.co"]# 限定 spider 的抓取活动只能在指定的 domain 中进行
    start_urls = [
        "http://www.xici.net.co/wn"
    ]
    def parse(self, response):
        #log.msg('crawl\t'+response.url, level=log.INFO)
        sel =Selector(response)
        item = ProxycrawlerItem()
        for ipItem in response.xpath('//*[@id="ip_list"]//tr'):
            item['ip'] = self.getFirstItem(ipItem.xpath('td[3]/text()').extract())
            item['port'] = self.getFirstItem(ipItem.xpath('td[4]/text()').extract())
            item['location'] = self.getFirstItem(ipItem.xpath('td[5]/text()').extract())
            item['status'] = self.getFirstItem(ipItem.xpath('td[6]/text()').extract())
            item['speed'] = self.getFirstItem(ipItem.xpath('td[8]/div/@title').extract())
            item['post_time'] = self.getFirstItem(ipItem.xpath('td[10]/text()').extract())
            if item['ip']:
                yield item
        nextLink = self.getFirstItem(sel.xpath(u'//*[@class="next_page"]/@href').extract())#get next page link
        if  nextLink:
            #print '______next link______www.xici.net.co'+nextLink
            yield Request('http://www.xici.net.co'+nextLink)
        
    def parse_detail(self,response):
        pass
    def getFirstItem(self,item):
        if len(item)>0:
            return item[0]
        else:
            return None