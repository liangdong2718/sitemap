from scrapy.exceptions import IgnoreRequest
from pybloom import BloomFilter
import random
import re

# Filter out duplicate requests with Bloom filters since they're much easier on memory
#URLS_FORMS_HEADERS = BloomFilter(3000000, 0.00001)
URLS_SEEN = BloomFilter(300000, .0001)

USER_AGENT_LIST = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0']

class RandomUserAgentMiddleware(object):
    ''' Use a random user-agent for each request '''
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        if 'payload' in request.meta:
            payload = request.meta['payload']
            if 'User-Agent' in request.headers:
                if payload == request.headers['User-Agent']:
                    return

        request.headers.setdefault('User-Agent', ua)
        request.meta['UA'] = ua

