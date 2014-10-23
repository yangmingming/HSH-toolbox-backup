##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

from __future__ import print_function
from HSH.Misc.shzillow import  zillow_property_detail
from HSH.Misc.logger import Log

if __name__ == "__main__":
    log = Log()
    try:
        result = zillow_property_detail("18727 DUKE LAKE DR", "77388", enable_logger = True)
        print(result)
    except Exception as e:
        print(e)
        print(e.index)