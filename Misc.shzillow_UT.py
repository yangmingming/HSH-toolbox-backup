##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

from __future__ import print_function
from HSH.Misc.shzillow import  zillow_property_detail
from HSH.Misc.logger import Log

if __name__ == "__main__":
#     log = Log()
#     try:
#         result = zillow_property_detail("18727 DUKE LAKE DR", "77383")
#         print(result)
#     except Exception as e:
#         log.write(e, e.index)
    
    address, zipcode = "5522 SEQUIN DR", "77388"
    try:
        print(zillow_property_detail(address, zipcode))
    except Exception as e:
        print(e)