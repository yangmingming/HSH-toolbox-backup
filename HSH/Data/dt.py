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
Repack of datetime module
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


if __name__ == "__main__":
    def UT1():
        print(day_interval(2012, 2, 29, mode = "str") )
        print(month_interval(2014, 12, mode = "str") )
        print(year_interval(1999, mode = "str") )
        
    UT1()

    