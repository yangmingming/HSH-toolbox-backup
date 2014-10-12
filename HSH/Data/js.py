##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

"""
This module is re-pack of some json utility functions
    1. load json object from file
    2. dump json object to file. Replace existing file when replace = True
    3. pretty print json object
    4. transform a dict data to jsontree object

compatible: python2 and python3

import:
    from HSH.Data.js import load_js, dump_js, prt_js
"""

from __future__ import print_function
import json
import sys
import os
import time

is_py2 = (sys.version_info[0] == 2)
if is_py2:
    read_mode, write_mode = "rb", "wb"
else:
    read_mode, write_mode = "r", "w"
    
def load_js(fname):
    """load dict object from file"""
    print("Loading from %s..." % fname)
    st = time.clock()
    if os.path.exists(fname): # exists, then load
        js = json.load(open(fname, read_mode) )
        print("\tComplete! Elapse %s sec." % (time.clock() - st) )
        return js
    else:
        print("%s not exists! cannot load!" % fname)
        print("\tComplete! Elapse %s sec." % (time.clock() - st) )
        return dict()

def dump_js(js, fname, fastmode = False, replace = False):
    """dump dict object to file.
    dump without pretty indent can be faster when fastmode = True
    Replace existing file when replace = True"""        
    print("Dumping to %s..." % fname)
    
    st = time.clock()
    
    if os.path.exists(fname): # if exists, check replace option
        if replace: # replace existing file
            if fastmode: # no sort and indent, do the fastest dumping
                json.dump(js, open(fname, write_mode))
            else:
                json.dump(js, open(fname, write_mode), sort_keys=True, indent=4,separators=("," , ": ") )
        else: # stop, print error message
            print("CANNOT WRITE to %s, it's already exists" % fname)
    else: # if not exists, just write to it
        if fastmode: # no sort and indent, do the fastest dumping
            json.dump(js, open(fname, write_mode))
        else:
            json.dump(js, open(fname, write_mode), sort_keys=True, indent=4,separators=("," , ": ") )
            
    print("\tComplete! Elapse %s sec" % (time.clock() - st) )

def prt_js(js):
    """pretty print dict object"""
    print(json.dumps(js, sort_keys=True,indent=4,separators=("," , ": ")) )