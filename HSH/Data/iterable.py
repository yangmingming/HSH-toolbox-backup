##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-10-06

import itertools
import time
import random

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

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(itertools.islice(iterable, n, None), default)

def shuffled(iterable):
    "Returns the shuffled iterable"
    return random.sample(iterable, len(iterable))

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

def grouper_dict(DICT, n):
    "evenly divide DICTIONARY into fixed-length piece, no filled value if chunk size smaller than fixed-length"
    for group in grouper(DICT, n):
        chunk_d = dict()
        for k in group:
            if k != None:
                chunk_d[k] = DICT[k]
        yield chunk_d

def grouper_list(LIST, n):
    "evenly divide LIST into fixed-length piece, no filled value if chunk size smaller than fixed-length"
    for group in grouper(LIST, n):
        chunk_l = list()
        for i in group:
            if i != None:
                chunk_l.append(i)
        yield chunk_l

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

def unit_test2():
    """Test for grouper, grouper_list, grouper_dict
    """
    for chunk in grouper('abcdefg',3):
        print chunk
        
    a = {key: 'hello' for key in xrange(10)} ## test grouper_list
    for chunk_d in grouper_dict(a, 3):
        print chunk_d
        
    b = xrange(10) # test grouper_dict
    for chunk_l in grouper_list(b, 3):
        print chunk_l
        
if __name__ == '__main__':
#     unit_test1()
    unit_test2()
    pass