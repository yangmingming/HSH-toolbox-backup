##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-11

'''一个简单的日志文件夹和日志文件的管理小工具
log文件总在脚本执行开始创建，文件名为
    "脚本运行的时间.txt"
log信息格式:
    <datetime><class><message><info>
'''

import datetime
import os

class Log(object):
    def __init__(self, directory = 'log'):
        self.fname = '%s.txt' % datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H_%M_%S')
        self.directory = directory
        
    def clear_all(self):
        '''DELETE all log file under #directory
        '''
        cmd = raw_input('Are you sure you want to delete all log file under folder "%s"?\nENTER "YES" to confirm: ' % self.directory)
        if cmd == 'YES':
            for fname in os.listdir(self.directory):
                os.remove(os.path.join(self.directory, fname))
            print 'All log file under folder "%s" have been deleted.' % self.directory
        else:
            print 'DELETE operation canceled.'
            
    def write(self, index, message):
        '''Write line to local log file
        log line format:
            <datetime><index><message>
                index: type of this log
                message: log text message
        '''
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        line = '<%s><%s><%s>\n' % (datetime.datetime.now(), 
                                                 index, 
                                                 message)
        print '\t log = %s' % line
        with open(os.path.join(self.directory, self.fname), 'a') as f:
            f.write(line)

def unit_test():
    log = Log()
    log.write('request denied', ('www.python.org', 5))
    log.clear_all()
    
if __name__ == '__main__':
    unit_test()