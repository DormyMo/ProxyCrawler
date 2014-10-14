# -*- coding: utf-8 -*-
'''
Created on 2014-10-11

@author: modm
'''
'''
item->mongodb
'''
import json
from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter
from scrapy import log
from scrapy.exceptions import DropItem
#==================================
from pymongo import MongoClient,errors
import datetime
import hashlib
import datetime

class SingleMongodbPipeline(object):
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/') #mongo ip:port
        self.db = self.client['dxy'] #mongo db name
    def process_item(self,item,spider):
        _id= hashlib.sha1(item.get('ip')).hexdigest()
        speed = item.get('speed').strip().replace(u'秒','')
        content ={'_id':_id,
        'ip':item.get('ip'),
        'port':item.get('port'),
        'location':item.get('location').strip(),
        'status':item.get('status'),
        'speed':speed,
        'post_time':'20'+item.get('post_time').strip()}
        posts = self.db.proxy #mongo collection name
        try:
            post_id = posts.insert(content)
            log.msg('done\t'+str(post_id), level=log.INFO)
        except errors.DuplicateKeyError,e:
            #print speed
            #posts.update({'_id':_id}, {"$set": {'speed':speed}}, upsert=False)
            pass