#!/usr/bin/env python

import argparse
from scrapy.cmdline import execute
import sys

__author__ = 'Dong Liang'
__license__ = 'BSD'
__version__ = '1.0'
__email__ = 'liangdong46@gmail.com'

def get_args():
    parser = argparse.ArgumentParser(description=__doc__,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-u', '--url', help="URL to scan; -u http://example.com")
    parser.add_argument('-c', '--connections', default='30', help="Set the max number of simultaneous connections allowed, default=30")
    parser.add_argument('-r', '--ratelimit', default='0', help="Rate in requests per minute, default=0")
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    rate = args.ratelimit
    if rate not in [None, '0']:
        rate = str(60 / float(rate))
    try:
        execute(['scrapy', 'crawl', 'urlspider',
                 '-a', 'url=%s' % args.url,
                 '-s', 'CONCURRENT_REQUESTS=%s' % args.connections,
                 '-s', 'DOWNLOAD_DELAY=%s' % rate,
                 '-o', 'url.json'])
    except KeyboardInterrupt:
        sys.exit()

main()
