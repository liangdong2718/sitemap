# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from site_crawl.items import SiteCrawlItem
from site_crawl.urlhandler import obtain_key
from pybloom import BloomFilter
from urlparse import urlparse

import scrapy
import pdb

class UrlSpider(CrawlSpider):
    name = "urlspider"
    allowed_domains = ["tianya.cn"]
    start_urls = ("http://www.hao123.com", )
    rules = (
            Rule(SgmlLinkExtractor(allow=()), callback="parse_resp", follow= True),
            )

    def __init__(self, *args, **kwargs):
        # run using: scrapy crawl xss_spider -a url='http://example.com'
        super(UrlSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('url')]
        hostname = urlparse(self.start_urls[0]).hostname
        self.allowed_domains = [hostname] # adding [] around the value seems to allow it to crawl subdomain of value
        self.fingerprints = BloomFilter(3000000, 0.0001)

    def parse_start_url(self, response):
        print "start:"+response.url
        return

    def parse_resp(self, response):
        fp = response.url
        new_fp = obtain_key(fp)
        if new_fp in self.fingerprints:
            return
        self.fingerprints.add(new_fp)

        item = SiteCrawlItem()
        item["url"] = response.url
        yield item

    #def parse(self, response):
    #    print "parse2"+response.url

