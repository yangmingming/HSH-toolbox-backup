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

"""
This module is re-pack of some hashlib utility functions
    1. md5 a string
    2. md5 a python object
    3. md5 a file

compatible: python2 and python3

usage:
    from HSH.Data.hsh_hashlib import md5_str, md5_obj, md5_file
"""

from __future__ import print_function
import hashlib
import pickle
import sys

is_py2 = (sys.version_info[0] == 2)
if is_py2:
    pickle_protocol = 2
else:
    pickle_protocol = 3
    
def md5_str(text):
    """return md5 value from a STRING
    """
    m = hashlib.md5()
    m.update(text.encode("utf-8"))
    return m.hexdigest()

def md5_obj(obj):
    """return md5 value from a PYTHON OBJECT
    """
    m = hashlib.md5()
    if is_py2:
#         print( [pickle.dumps(obj, protocol = 2)] )
        m.update( pickle.dumps(obj, protocol = pickle_protocol) )
    else:
#         print( [str(pickle.dumps(obj, protocol = 2) )] )
        m.update( str(pickle.dumps(obj, protocol = pickle_protocol)).encode('utf-8') )
        
    return m.hexdigest()

def md5_obj(obj):
    """return md5 value from a PYTHON OBJECT
    """
    m = hashlib.md5()
    if is_py2:
#         print( [pickle.dumps(obj, protocol = 2)] )
        m.update( pickle.dumps(obj, protocol = pickle_protocol) )
    else:
#         print( [str(pickle.dumps(obj, protocol = 2) )] )
        m.update( str(pickle.dumps(obj, protocol = pickle_protocol)).encode('utf-8') )
        
    return m.hexdigest()

def md5_file(fname, chunk_size = 2**10 ):
    """return md5 value from a FILE
    Estimate processing time on:
        CPU = i7-4600U 2.10GHz - 2.70GHz, RAM = 8.00 GB
        1 second can process 0.25GB data
            0.59G - 2.43 sec
            1.3G - 5.68 sec
            1.9G - 7.72 sec
            2.5G - 10.32 sec
            3.9G - 16.0 sec
    
    ATTENTION:
        When you md5 a file, if you change the meta data (for example, the title, years information
        in audio, video), then the md5 value gonna change.
    """
    m = hashlib.md5()
    with open(fname, "rb") as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            m.update(data)
    return m.hexdigest()