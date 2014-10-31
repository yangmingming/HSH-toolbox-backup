##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

from __future__ import print_function
from six import iteritems

class SuperList(object):
    def difference(main_list, compared_list):
        """
        return the result of after removing all item in main_list
        if it is in compared_list.
        """
        return list(set(main_list).difference(set(compared_list)))
    
class SuperSet(object):
    def intersect_all(list_of_set):
        """interesct a list of set
        list_of_set can be a list or a generator object
        """
        res, flag = set(), 1
        for jihe in list_of_set:
            if flag:
                res.update(jihe)
                flag = 0
            else:
                res.intersection_update(jihe)
        return res
    
    def union_all(list_of_set):
        """union a list of set
        list_of_set can be a list or a generator object
        """
        res = set()
        for jihe in list_of_set:
            res.update(jihe)
        return res

class SuperDict(object):
    pass

if __name__ == "__main__":
    
    def superSet_UT():
        def gen(list_of_set):
            for i in list_of_set:
                yield i
        
        print(SuperSet.intersect_all(gen([{1,2,3}, 
                                          {2,3,4}, 
                                          {3,5,6}])))
        print(SuperSet.intersect_all([{1,2,3}, 
                                      {2,3,4}, 
                                      {3,5,6}]))
        print(SuperSet.union_all(gen([{1,2,3}, 
                                      {2,3,4}, 
                                      {3,5,6}])))
        print(SuperSet.union_all([{1,2,3}, 
                                  {2,3,4}, 
                                  {3,5,6}]))
        
#     superSet_UT()