##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-22

from __future__ import print_function
from ..LinearSpider.crawler import Crawler
from bs4 import BeautifulSoup as BS4

class HttpError(Exception):
    def __init__(self, address, zipcode, url):
        self.address= address
        self.zipcode = zipcode
        self.url = url
        self.index = "Zillow Crawler HttpError"
        
    def __str__(self):
        return "Failed to get http response from url = %s,  address = %s, zipcode = %s" % (self.address, 
                                                                                           self.zipcode, 
                                                                                           self.url)

class ExtractorError(Exception):
    def __init__(self, address, zipcode, url):
        self.address= address
        self.zipcode = zipcode
        self.url = url
        self.index = "Zillow Crawler ExtractorError"
        
    def __str__(self):
        return "Failed to analysis address = %s, zipcode = %s from url = %s" % (self.address, 
                                                                                self.zipcode, 
                                                                                self.url)

def gen_url(address, zipcode):
    base = "http://www.zillow.com/homes/"
    return base + address.replace(" ", "-") + "-" + zipcode + "_rb/"

def zillow_property_detail(address, zipcode, enable_logger = False):
    url = gen_url(address, zipcode)
    spider = Crawler()
    html = spider.html(url)
    if html:
        try:
            soup = BS4(html)
            dt = soup.find("dt", class_ ="property-data")
            info = dt.text.strip()
            span = soup.find("span", itemprop = "addressLocality")
            city = span.text.strip()
            span = soup.find("span", itemprop = "addressRegion")
            state = span.text.strip()
            return address, city, state, zipcode, info
        except:
            raise ExtractorError(address, zipcode, url)
    else:
        raise HttpError(address, zipcode, url)