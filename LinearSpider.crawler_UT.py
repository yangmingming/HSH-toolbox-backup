##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-12

from HSH.LinearSpider.crawler import Crawler, Taskplanner, ignore_iterkeys, ignore_itervalues, ignore_iteritems
from HSH.Data.jt import *

def UT_crawl_html():
    url = 'https://www.python.org/'
    spider = Crawler()
    print spider.html(url)

def UT_Taskplanner():
    tp = Taskplanner()
    tp.todo['https://www.python.org'] = {'ref': {'city': 'arlington',
                                                 'state': 'VA'},
                                         'https://www.python.org/page01' : {'ref': {}},
                                         'https://www.python.org/page02' : {'ref': {}},
                                         }
    tp._dump_todo('todo.json', replace = True)
    tp._load_todo('todo.json')
    for k, v in ignore_iteritems( tp.todo['https://www.python.org'] ):
        print k, v

if __name__ == '__main__':
    UT_crawl_html()
    UT_Taskplanner()