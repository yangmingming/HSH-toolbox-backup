##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-31             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
很多时候我们需要把整个列表中的数据结构进行改变
"""

from __future__ import print_function
import numpy as np
import time

def int_to_str(array, fixed_length = None):
    """
    situation1:
        int array to string
            1. naive str (23 -> "23")
                numpy x2 faster than iterator
                
            2. length fixed (23 -> "0023")
                numpy cannot do that
    """
    res = list()
    for i in array:
        res.append(str(i))
    return res

def float_to_str(array, precision = 2):
    res = list()
    for i in array:
        res.append("%.2f")

def unit_test():
    a = [i for i in range(1000000000, 1000001000)]
    a1 = np.array(a)
    
    st = time.clock()
    int_to_str(a)
    print(time.clock() - st)
    
    st = time.clock()
    a1.astype(str).tolist()
    print(time.clock() - st)
    print(a1)
    
unit_test()