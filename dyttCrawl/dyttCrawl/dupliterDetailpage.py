import os

from scrapy.dupefilters import RFPDupeFilter
from scrapy.utils.request import request_fingerprint

class CustomFilter(RFPDupeFilter):
    """A dupe filter that considers specific ids in the url"""
    def isListPage(self,url):
        if "list" in url or "index" in url:
            return True

    def request_seen(self, request):
        url = request.url
        if self.isListPage(url):
            return False
        elif url in self.fingerprints:
            return True
        self.fingerprints.add(url)
        if self.file:
            self.file.write(url + os.linesep)