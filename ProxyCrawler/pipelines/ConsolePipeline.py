'''
Created on 2014-10-11

@author: modm
'''
from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter
from scrapy import log
#==================================
from pymongo import MongoClient
import datetime
import hashlib

class ConsolePipeline(object):
    def process_item(self,item,spider):
        print item