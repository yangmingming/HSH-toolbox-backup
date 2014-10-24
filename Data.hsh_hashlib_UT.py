##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-07


from __future__ import print_function
from HSH.Data.hsh_hashlib import md5_str, md5_obj, md5_file

if __name__ == '__main__':
    print( md5_str('hello world!') )
    print( md5_obj(['1',2,'3',4]) )
    print( md5_file('Data.js_UT.py') )