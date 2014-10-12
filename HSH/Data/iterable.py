##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

"""
This module provides high performance iterator recipes
best time and memory complexity implementation at all

compatible: python2 and python3

import:
    from HSH.Data.iterable import flatten, flatten_all, nth, shuffled, grouper, grouper_dict, grouper_list
"""

import itertools
import time
import random
import sys

is_py2 = (sys.version_info[0] == 2)
if is_py2:
    from itertools import ifilterfalse as filterfalse, izip_longest as zip_longest
else:
    from itertools import filterfalse, zip_longest
    
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
    return zip_longest(fillvalue=fillvalue, *args)

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