##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-12

'''smtf (smart folder) is a re-pack of some useful functionality of os
from HSH.OS.smtf import *
'''

import os

def getdirsize(path):
    '''calculate size of a directory
    DISCUSSION:
        The code here actually is a bad solution. Check this out:
            http://stackoverflow.com/questions/2485719/very-quickly-getting-total-size-of-folder
        The better way is to install pywin32 extension and call WINDOWS API
        === Sample code ===
        import win32com.client as com
        
        folderPath = r"D:\Software\Downloads"
        fso = com.Dispatch("Scripting.FileSystemObject")
        folder = fso.GetFolder(folderPath)
        MB=1024*1024.0
        print  "%.2f MB"%(folder.Size/MB)
    '''
    if os.path.isdir(path):
        total = 0
        for current_dir, folderlist, fnamelist in os.walk(path):
            for fname in fnamelist:
                total += os.path.getsize(os.path.join(current_dir, fname))
        return total
    else:
        raise Exception("%s is not a directory!" % path)
    
def string_SizeInBytes(size_in_bytes):
    '''make size in bytes human readable. Doesn't support size greater than 1TB
    '''
    res, by = divmod(size_in_bytes,1024)
    res, kb = divmod(res,1024)
    gb, mb = divmod(res,1024)
    if gb != 0:
        human_readable_size = '%.2fGB' % (gb + mb/float(1024) )
    elif mb != 0:
        human_readable_size = '%.2fMB' % (mb + kb/float(1024) )
    elif kb != 0:
        human_readable_size = '%.2fKB' % (kb + by/float(1024) )
    else:
        human_readable_size = '%sKB' % by
    return human_readable_size

def unit_test():
    print getdirsize(os.getcwd())
    print string_SizeInBytes(43428985831)
    print getdirsize(r'smtf.py')
    
if __name__ == '__main__':
    unit_test()