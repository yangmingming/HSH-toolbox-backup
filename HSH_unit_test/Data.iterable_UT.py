##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

from __future__ import print_function
from HSH.Data.iterable import flatten, flatten_all, nth, shuffled, grouper, grouper_dict, grouper_list
from HSH.Data.iterable import running_windows, cycle_running_windows, cycle_slice
import time

def unit_test1():
    """Test for flatten_all
    """
    complexity = 1000
    a = [[1,2,3],[4,[5,6],[7,8]], [9,10]] * complexity
    b = range(complexity * 10)
    st = time.clock()
    for i in flatten_all(a):
        pass
    print(time.clock() - st)
    
    st = time.clock()
    for i in b:
        pass
    print(time.clock() - st)

def unit_test2():
    """Test for grouper, grouper_list, grouper_dict
    """
    
    print("=== Test for grouper ===")
    for chunk in grouper("abcdefg",3):
        print("\t", chunk)
        
    print("=== Test for grouper_dict ===")
    a = {key: "hello" for key in range(10)} ## test grouper_list
    for chunk_d in grouper_dict(a, 3):
        print("\t", chunk_d)
        
    print("=== Test for grouper_list ===")
    b = range(10) # test grouper_dict
    for chunk_l in grouper_list(b, 3):
        print("\t", chunk_l)

def unit_test3():
    """Test for nth
    """
    n = 1000000
    array = [i for i in range(n)]
    st = time.clock()
    for i in range(100, n):
        a = array[i]
    print(time.clock() - st)
    
    st = time.clock()
    for i in array[100:]:
        a = i
    print(time.clock() - st)
#     st = time.clock()
#     for i in range(n):
#         b = nth(array, i)
#     print(time.clock() - st)
        
def unit_test4():
    array = [1,2,3,4,5,6,7,8,9,10]
    print("Testing running windows")
    for i in running_windows(array,3):
        print(i)
        
    print("Testing cycle running windows")
    for i in cycle_running_windows(array, 3):
        print(i)
    
    print(cycle_slice(array, 3, 6) )
    print(cycle_slice(array, 6, 3) )
                
if __name__ == "__main__":
#     unit_test1()
#     unit_test2()
#     unit_test3()
#     unit_test4()
