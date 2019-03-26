# -*- coding: utf-8 -*-
import scrapy
import re
from tutorial.items import ngaItem

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class ExampleSpider(scrapy.Spider):
	        
	name = 'example'
	allowed_domains = ['nga.cn']
	start_urls = ['https://bbs.nga.cn/read.php?tid=16766611&_ff=-7']
	request_cookies = {'guestJs':'1553150682',
										'ngaPassportUid':'38669789',
										'ngaPassportUrlencodedUname':'Bazinga_93',
										'ngaPassportCid':'X8os4d79o98t4m9meqfmdqkutt5esgklbfjb6098'}
	
	request_headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
										 'host':'bbs.nga.cn',
										 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
										 #'cookie': 'guestJs=1553150682; lastpath=/thread.php?fid=-7&rand=42; UM_distinctid=1699efeaf39a1a-088175e4238018-5701631-100200-1699efeaf3a7a; CNZZDATA1256638820=1113703577-1553148961-https%253A%252F%252Fbbs.nga.cn%252F%7C1553148961; CNZZDATA30043604=cnzz_eid%3D1649574403-1553148299-https%253A%252F%252Fbbs.nga.cn%252F%26ntime%3D1553148299; CNZZDATA30039253=cnzz_eid%3D1984504970-1553148093-https%253A%252F%252Fbbs.nga.cn%252F%26ntime%3D1553148093; taihe=f82fc084c582692ff730b1851d35c6f9; taihe_session=77e3da7f4c3dbdcccd879208255b9444; Hm_lvt_5adc78329e14807f050ce131992ae69b=1553150685; PHPSESSID=l89tmsjm3sedk1997q0uef2uu1; lastvisit=1553150713; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A%22b%22%2C1%3A1553151014%7D%7D; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1553150715; ngaPassportOid=2e0bbefc601efb3c261e2ff9844c83f3; ngacn0comUserInfo=Bazinga_93%09Bazinga_93%0939%0939%09%0910%0920200%094%090%090%0961_64; ngacn0comUserInfoCheck=ad055f4d37cd208cce41067d87c7ab8d; ngacn0comInfoCheckTime=1553150744; ngaPassportUid=38669789; ngaPassportUrlencodedUname=Bazinga_93; ngaPassportCid=X8os4d79o98t4m9meqfmdqkutt5esgklbfjb6098',
										 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}									 	
										 	
	ngaItems = {}
	
	      
	def thread_prase(self, response):
		print(response.url)
		#with open('example','w+') as f:
		#	f.write(response.body.decode('gbk'))
		for each in response.xpath('//table/tbody'):
			item = ngaItem()
			item['topic'] = each.xpath('tr/td[@class="c2"]/a/text()').extract_first()
			item['link'] = each.xpath('tr/td[@class="c2"]/a/@href').extract_first()
			item['replies'] = each.xpath('tr/td[@class="c1"]/a/text()').extract_first()
			item['id'] = each.xpath('tr/td[@class="c3"]/span/text()').extract_first()
			item['context'] = [] 
			#print item
			self.ngaItems.update({item['id']:item})
			replyPage = response.urljoin(item['link'])
			id = each.xpath('tr/td[@class="c3"]/span/text()').extract_first()
			if item['replies'] > 0:
				yield scrapy.Request(replyPage,headers=self.request_headers,cookies=self.request_cookies,callback=self.read_prase, meta={'id': id})
			return self.ngaItems
		#print(self.ngaItems)
	
	def read_prase(self, response):
		id = response.meta['id']
		with open('example','w+') as f:
			f.write(response.body.decode('gbk'))
		next_page = response.xpath('//div[@id="pagebbtm"]/a[@class="pager_spacer"]/@href').extract()
		if len(''.join(next_page)) > 1:
			yield scrapy.Request(response.urljoin(''.join(next_page)),headers=self.request_headers,cookies=self.request_cookies,callback=self.read_prase, meta={'id': 0})
		replyList = []
		for each in response.xpath('//table[@class="forumbox postbox"]'):
			context = each.xpath('tr/td[@class="c2"]//span[@class="postcontent ubbcode"]').extract_first()
			if context != None:
				context = str(context).decode('utf8')
				item = {'context':context,'quote':None,'b':None,'reply':None,'img':None}
				img = re.findall(r'\[img\](.*)\[/img\]',context)
				context = re.sub('\[img\]Reply.*\[/img\]','',context)
				quote = re.findall(r'\[quote\](.*)\[/quote\]',context)
				context = re.sub(r'\[quote\](.*)\[/quote\]','',context)
				context = re.sub('\[b\]Reply.*\[/b\]','',context)
				reply = (re.findall(r'>.*</span>',context)[0]).replace('</span>','').replace('>','',1)
				item.update({'reply':reply})
				item.update({'quote':quote})
				item.update({'img':img})
				replyList.append(item)
		topicItem = ngaItem() #self.ngaItems[id]
		topicItem['context'] = replyList
		self.ngaItems.update({id:topicItem})
		#return topicItem
		
		
	      
	def parse(self, response):
	  currentUrl = response.url
	  if re.match('.*thread.*',currentUrl):
	 		yield scrapy.Request(response.url,headers=self.request_headers,cookies=self.request_cookies,callback=self.thread_prase)	  
	  if re.match('.*read.*',currentUrl):
	 		yield scrapy.Request(response.url,headers=self.request_headers,cookies=self.request_cookies,callback=self.read_prase)	  
	  

    