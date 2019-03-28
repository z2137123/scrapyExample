# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import requests
from tutorial.items import ngaItem

class TutorialPipeline(object):
    def __init__(self):
        self.file = open('items.txt', 'wb')

    def process_item(self, item, spider):
			line = 'Topic:=====>>'  + item['topic'] + '<<=====\n'
			line = line + 'mainFloor:' + item['mainFloor'] + "\n"
			for each in item['context']:
				if len(','.join(each['quote'])) > 1:
					line = line + 'Quote:' + ','.join(each['quote']) + "\n"
				if len(','.join(each['img'])) > 1:
					for eachImg in each['img']:
						if len(eachImg.split('[/img]')) > 1:
							url = eachImg.split('[/img]')[0]
							line = line + 'Img:' + url + "\n"
							fileName = url.split('/')[-1]
							#print fileName
							
							if url.startswith('.'):
								url = url[1:]
								url = 'https://img.nga.178.com/attachments' + url
							#print url
							
							with open('dlImg\\' + fileName,'wb') as f:
								req = requests.get(url)
								f.write(req.content)
								
				line = line + 'reply:' + each['reply'] + "\n"
			line = line + 'COL:=====================================================\n'	
			self.file.write(line)
			return item
			
