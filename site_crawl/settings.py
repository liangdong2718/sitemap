# -*- coding: utf-8 -*-

# Scrapy settings for site_crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'site_crawl'

SPIDER_MODULES = ['site_crawl.spiders']
NEWSPIDER_MODULE = 'site_crawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'site_crawl (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {'site_crawl.middlewares.RandomUserAgentMiddleware': 200,}

DUPEFILTER_CLASS = 'site_crawl.bloomfilters.BloomURLDupeFilter'


