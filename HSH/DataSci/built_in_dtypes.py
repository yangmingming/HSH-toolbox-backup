##################################
#encoding=utf8                   #
#version =py33 only              #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
注意：在python2中
import:
    from built_in_dtypes import OrderedSet, SupperSet
"""
from __future__ import print_function
import collections
from six import iteritems

class SuperList(object):
    @staticmethod
    def difference(main_list, compared_list):
        """
        return the result of after removing all item in main_list
        if it is in compared_list.
        """
        return list(set(main_list).difference(set(compared_list)))
    
class SuperSet(object):
    @staticmethod
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
    
    @staticmethod
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

class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)


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
    
    def orderedSet_UT1():
        s = OrderedSet(list())
        s.add("c")
        s.add("g")
        s.add("a")
        s.discard("g")
        print(s)
        print(list(s))
        
    def orderedSet_UT2():
        s = OrderedSet('abracadaba') # {"a", "b", "r", "c", "d"}
        t = OrderedSet('simsalabim') # {"s", "i", "m", "a", "l", "b"}
        print(s | t) # s union t
        print(s & t) # s intersect t
        print(s - t) # s different t
        
    orderedSet_UT1()
    orderedSet_UT2()