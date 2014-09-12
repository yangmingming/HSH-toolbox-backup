##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-11

'''
'''
import requests
import sys
import os
import random
import jsontree
from ..Data.jt import load_jt, dump_jt, d2j, prt_jt

reload(sys); # change the system default encoding = utf-8
eval('sys.setdefaultencoding("utf-8")')

class Crawler(object):
    '''Simple http Crawler class
    '''
    def __init__(self):
        self.user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
                            'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
                            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
                            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11, (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11']
        self.auth = None # initialize the self.auth. Then if there's no login, Crawler.html can work in regular mode
    
    def _gen_header(self):
        headers = {'User-Agent': random.choice(self.user_agents),
                   'Accept':'text/html;q=0.9,*/*;q=0.8',
                   'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                   'Accept-Encoding':'gzip',
                   'Connection':'close',
                   'Referer':None}
        return headers
    
    def _login(self, url, payload, timeout = 6):
        '''website log in
        url = login_page_url
        payload = {key1: acc, key2: password}
        '''
        self.auth = requests.Session()
        try:
            self.auth.post(url, data=payload, timeout=timeout)
            print 'successfully loged in to %s' % url
            return True
        except:
            return False
    
    def html(self, url, timeout = 6):
        '''return the html for the url
        '''
        if not self.auth: # if no login needed, then self.c = None, then not self.c = True
            ## regular get html, use requests.get
            try:
                r = requests.get(url, headers = self._gen_header(), timeout = timeout)
                return r.text # if success, return html
            except:
#                 print '%s time out!' % url # <=== 测试时才用
                return None # if failed, return none
        else: # if login needed, use self.auth.get
            try:
                r = self.auth.get(url, headers = self.headers, timeout = timeout)
                return r.text # if success, return html
            except:
#                 print '%s time out!' % url <=== 测试时才用
                return None # if failed, return none
            
class Taskplanner(object):
    '''Taskplanner crawling model
    there are two step in linear crawling.
        1. plan the url tree to crawl. 
        2. download html and extract data
        
    The first step is to find where are those target data locate at. The todo_urllist
    jsontree is saved at self.todo
    
    In the second step, we need to save which url we have been crawled and we
    already got the data we need. The crawled url list is saved at self.finished
    '''
    def __init__(self):
        self.todo = jsontree.jsontree()
        self.finished = jsontree.jsontree()
    
    def _dump_todo(self, path, fastmode = False, replace = False):
        '''dump taskplanner.todo to local file.
        When replace = False, existing local file will not be overwrite. For safety
        '''
        dump_jt(self.todo, path, fastmode = fastmode, replace = replace)

    def _dump_finished(self, path, replace = False):
        '''dump taskplanner.finished to local file.
        When replace = False, existing local file will not be overwrite. For safety
        '''
        dump_jt(self.finished, path, fastmode = fastmode, replace = replace)

    def _load_todo(self, path):
        '''load taskplanner.todo data from local file
        '''
        if os.path.exists(path): # exists, then load
            with open(path, 'rb') as f:
                self.todo = jsontree.loads(f.read())
        else:
            print 'CANNOT load! %s not exists!' % path

    def _load_finished(self, path):
        '''load taskplanner.fished data from local file
        '''
        if os.path.exists(path): # exists, then load
            with open(path, 'rb') as f:
                self.finished = jsontree.loads(f.read())
        else:
            print 'CANNOT load! %s not exists!' % path
            
def ignore_iterkeys(dictionary, ignore = ['ref']): # data 在线性爬虫中用于默认储存task.todo的传递信息，详情见Readme.MD
    '''iter dict keys, ignore the key in the "ignore" list'''
    for key in dictionary:
        if key not in ignore:
            yield key

def ignore_itervalues(dictionary, ignore = ['ref']):
    '''iter dict keys, ignore the key in the "ignore" list'''
    for key in dictionary:
        if key not in ignore:
            yield dictionary[key]
            
def ignore_iteritems(dictionary, ignore = ['ref']):
    '''iter dict keys, ignore the key in the "ignore" list'''
    for key, value in dictionary.iteritems():
        if key not in ignore:
            yield key, value