# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re

class DayanSpider(scrapy.Spider):
    name = "Dayan"
    # allowed_domains = ["http://travel.qunar.com/p-oi705404-dayanta#"]
    start_urls = 'http://travel.qunar.com/p-oi705404-dayanta#/'

    def start_requests(self):
        url=self.start_urls
        yield Request(url,self.parse)
    def parse(self, response):
        aa=re.compile('<p class="first">(.*?)</p>',re.S)
        list=aa.findall(response.text)
        for i in list:
            print(i)