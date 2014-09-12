##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-12

from HSH.Data.jt import load_jt, dump_jt, prt_jt, d2j, ignore_iterkeys, ignore_itervalues, ignore_iteritems

def unit_test():
    frequency = {i : 0 for i in 'abcdefg'}
    dump_jt(frequency, 'frequency.json', fastmode = False, replace = True) 

if __name__ == '__main__':
    unit_test()