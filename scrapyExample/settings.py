# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

HTTPERROR_ALLOWED_CODES = [403]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
	 #'cookie': 'guestJs=1553150682; lastpath=/thread.php?fid=-7&rand=42; UM_distinctid=1699efeaf39a1a-088175e4238018-5701631-100200-1699efeaf3a7a; CNZZDATA1256638820=1113703577-1553148961-https%253A%252F%252Fbbs.nga.cn%252F%7C1553148961; CNZZDATA30043604=cnzz_eid%3D1649574403-1553148299-https%253A%252F%252Fbbs.nga.cn%252F%26ntime%3D1553148299; CNZZDATA30039253=cnzz_eid%3D1984504970-1553148093-https%253A%252F%252Fbbs.nga.cn%252F%26ntime%3D1553148093; taihe=f82fc084c582692ff730b1851d35c6f9; taihe_session=77e3da7f4c3dbdcccd879208255b9444; Hm_lvt_5adc78329e14807f050ce131992ae69b=1553150685; PHPSESSID=l89tmsjm3sedk1997q0uef2uu1; lastvisit=1553150713; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A%22b%22%2C1%3A1553151014%7D%7D; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1553150715; ngaPassportOid=2e0bbefc601efb3c261e2ff9844c83f3; ngacn0comUserInfo=Bazinga_93%09Bazinga_93%0939%0939%09%0910%0920200%094%090%090%0961_64; ngacn0comUserInfoCheck=ad055f4d37cd208cce41067d87c7ab8d; ngacn0comInfoCheckTime=1553150744; ngaPassportUid=38669789; ngaPassportUrlencodedUname=Bazinga_93; ngaPassportCid=X8os4d79o98t4m9meqfmdqkutt5esgklbfjb6098',
	 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
	
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tutorial.pipelines.TutorialPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#FEED_EXPORT_ENCODING = 'GBK'