##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-07

import itertools
import time

def flatten(listOfLists):
    "Flatten one level of nesting"
    return itertools.chain.from_iterable(listOfLists)

def flatten_all(listOfLists):
    "Flatten arbitrary depth of nesting"
    for i in listOfLists:
        if hasattr(i, '__iter__'):
            for j in flatten_all(i):
                yield j
        else:
            yield i

def unit_test1():
    '''Test for flatten & flatten_all
    '''
    a = [[1,2,3],[4,[5,6],[7,8]], [9,10]] * 100000
    b = range(100000)
    st = time.clock()
    for i in flatten_all(a):
        pass
    print time.clock() - st
    
    st = time.clock()
    for i in b:
        pass
    print time.clock() - st
    
if __name__ == '__main__':
    unit_test1()
