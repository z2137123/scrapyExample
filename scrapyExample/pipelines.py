# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from tutorial.items import ngaItem

class TutorialPipeline(object):
    def __init__(self):
        self.file = open('items.txt', 'wb')

    def process_item(self, item, spider):
			#eItem = dict(item)
			line = 'Topic:=====>>' #+ item['topic'] + '<<=====\n'
			for each in item['context']:
				if len(','.join(each['quote'])) > 1:
					line = line + 'Quote:' + ','.join(each['quote']) + "\n"
				if len(','.join(each['img'])) > 1:
					line = line + 'Img:' + ','.join(each['Img']) + "\n"
				line = line + 'reply:' + each['reply'] + "\n"
			line = line + 'COL:=====================================================\n'	
			self.file.write(line)
			return item
