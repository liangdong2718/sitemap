from pybloom import BloomFilter
from scrapy.utils.job import job_dir
from scrapy.dupefilter import BaseDupeFilter
from urlhandler import obtain_key

class BloomURLDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""

    def __init__(self, path=None):
        self.file = None
        self.fingerprints = BloomFilter(3000000, 0.0001)

    @classmethod
    def from_settings(cls, settings):
        return cls(job_dir(settings))

    def request_seen(self, request):
        fp = request.url
        new_fp = obtain_key(fp)
        if new_fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)

    def close(self, reason):
        self.fingerprints = None
