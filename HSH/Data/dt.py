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
Repack of datetime standard library
    1. generate day, month, year interval start, end timestamp for SQL datetime related query.
    
compatibility: python2, python3

prerequisites: None

import:
    from HSH.Data.jt import day_interval, month_interval, year_interval
"""

from __future__ import print_function
from datetime import datetime as dt, date as dd, timedelta as td

def day_interval(year, month, day, mode = "dt"):
    """
    """
    start, end = dt(year, month, day), dt(year, month, day) + td(days=1) - td(seconds=1)
    if mode == "dt":
        return start, end
    elif mode == "str":
        return str(start), str(end)

def month_interval(year, month, mode = "dt"):
    """
    """
    if month == 12:
        start, end = dt(year, month, 1), dt(year+1, 1, 1) - td(seconds=1)
    else:
        start, end = dt(year, month, 1), dt(year, month+1, 1) - td(seconds=1)
    if mode == "dt":
        return start, end
    elif mode == "str":
        return str(start), str(end)
    
def year_interval(year, mode = "dt"):
    """
    """
    start, end = dt(year, 1, 1), dt(year+1, 1, 1) - td(seconds=1)
    if mode == "dt":
        return start, end
    elif mode == "str":
        return str(start), str(end)

def std_date(datestr, ind = None):
    """包含很多个模板的，日期格式标准化转换器
    可从模板中自动检测标准，省去了手动写格式匹配串的麻烦
    """
    templates = {k: v for k, v in enumerate(["%m/%d/%Y", "%m/%d/%y", # 月，日，年1
                                             "%b/%d/%Y", "%b/%d/%y", # 月，日，年2
                                             "%B/%d/%Y", "%B/%d/%y", # 月，日，年3
                                             "%d/%m/%Y", "%m/%m/%y", # 日，月，年1
                                             "%d/%b/%Y", "%m/%b/%y", # 日，月，年2
                                             "%d/%B/%Y", "%m/%B/%y", # 日，月，年3
                                             "%Y/%m/%d", "%y/%m/%d", # 年，月，日1
                                             "%Y/%b/%d", "%y/%b/%d", # 年，月，日1
                                             "%Y/%B/%d", "%y/%B/%d", # 年，月，日1
                                             ])}
    if ind:
        return dt.strftime(dt.strptime(datestr, templates[ind]), "%Y-%m-%d")
    else:
        for k, v in templates.items():
            try:
                iso_date = dt.strftime(dt.strptime(datestr, v), "%Y-%m-%d")
                return iso_date, k
            except:
                pass
        return None

if __name__ == "__main__":
    def UT1():
        print(day_interval(2012, 2, 29, mode = "str") )
        print(month_interval(2014, 12, mode = "str") )
        print(year_interval(1999, mode = "str") )
        
#     UT1()
    
    def UT2():
        print(std_date("2/21/1998")[0])
    
    UT2()