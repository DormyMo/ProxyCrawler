# -*- coding: utf-8 -*-
'''
Created on 2014-10-11

@author: modm
'''
'''
item->json File
'''
import json
from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter
from scrapy import log
#==================================
from pymongo import MongoClient
import datetime
import hashlib

class JsonFilePipeline(object):
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        with open('proxy.json','a') as f:
              f.write(line.encode('utf8'))
        f.close