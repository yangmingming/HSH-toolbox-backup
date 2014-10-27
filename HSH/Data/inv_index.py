##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-10-27

"""
index: a dict
"""

from __future__ import print_function
from six import iteritems

def inv_index(pos_index):
    """
    [Args]
    ------
    pos_index: normal index dictionary
        key: value = item_id: indices
    """
    invert_index = dict()
    for item_id, indices in iteritems(pos_index):
        for index in indices:
            if index not in invert_index:
                invert_index[index] = set({item_id})
            else:
                invert_index[index].add(item_id)
    return invert_index


    
if __name__ == "__main__":
    pos_index = {"let it go": {"mp3", "pop", "dance"},
                 "can you feel the love tonight": {"acc", "pop", "movie"},
                 "Just dance": {"pop", "dance", "club"}}

    res, flag = set(), 1
    for jihe in [{1,2,3}, {2,3,4}, {3,5,6}]:
        if flag:
            res.update(jihe)
            flag = 0
        else:
            res.intersection_update(jihe)
    print(res)