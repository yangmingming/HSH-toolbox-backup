##encoding=utf8
##version =py27
##author=Sanhe
##date  =2014-09-02

""" XXXXXXXXXXXXXXXXXX 过时的包，已经迁移到了js.py，免除了第三方库的需要
This module pack some frequently used operation up in functions
1. load json object from file
2. dump json object to file. Replace existing file when replace = True
3. pretty print json object
4. transform a dict data to jsontree object

compatible: python2 only

usage:
    from jt import load_jt, dump_jt, prt_jt, d2j, ignore_iterkeys, ignore_itervalues, ignore_iteritems
"""
from __future__ import print_function
import jsontree
import os
import time

def load_jt(fname):
    """load json object from file"""
    print("Loading from %s..." % fname)
    st = time.clock()
    if os.path.exists(fname): # exists, then load
        with open(fname, "rb") as f:
            jt = jsontree.loads(f.read())
            print("\tComplete! Elapse %s sec." % (time.clock() - st) )
            return jt
    else:
        print("%s not exists! cannot load!" % fname)
        print("\tComplete! Elapse %s sec." % (time.clock() - st) )
        return jsontree.jsontree()
        
def dump_jt(jt, fname, fastmode = False, replace = False):
    """dump json object to file.
    dump without pretty indent can be faster when fastmode = True
    Replace existing file when replace = True"""
    print("Dumping to %s..." % fname)
    st = time.clock()
    if os.path.exists(fname): # if exists, check replace option
        if replace: # replace existing file
            with open(fname, "wb") as f:
                if fastmode:
                    f.write(jsontree.dumps(jt))
                else:
                    f.write(jsontree.dumps(jt, sort_keys=True,indent=4,separators=("," , ": ")))
        else: # stop, print error message
            print("CANNOT WRITE to %s, it's already exists" % fname)
    else: # if not exists, just write to it
        with open(fname, "wb") as f:
            if fastmode:
                f.write(jsontree.dumps(jt))
            else:
                f.write(jsontree.dumps(jt, sort_keys=True,indent=4,separators=("," , ": ")))
    print("\tComplete! Elapse %s sec" % (time.clock() - st) )
    
def prt_jt(jt):
    """pretty print json object"""
    print(jsontree.dumps(jt, sort_keys=True,indent=4,separators=("," , ": ")) )
    
def d2j(dictionary):
    """transform a dict data to jsontree object"""
    return jsontree.loads(jsontree.dumps(dictionary))

def unit_test():
    data = {"a": [1,2,3]}
    prt_jt(d2j(data))
    
    # The speed comparison of Simple Dumps and Dumps with Pretty Indent
    import time
    d = {key: list(xrange(1000)) for key in xrange(1000)}
    
    st = time.clock()
    jt1 = jsontree.dumps(d) # 10 times faster than dumps with pretty indent
    print( time.clock()-st )
    
    st = time.clock()
    jt2 = jsontree.dumps(d, sort_keys=True,indent=4,separators=("," , ": "))
    print( time.clock()-st )
    
if __name__ == "__main__":
    unit_test()