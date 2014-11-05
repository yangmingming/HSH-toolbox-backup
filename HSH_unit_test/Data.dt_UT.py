##encoding=utf8

from HSH.Data.dt import day_interval, month_interval, year_interval

def UT1():
    print(day_interval(2012, 2, 29, mode = "str") )
    print(month_interval(2014, 12, mode = "str") )
    print(year_interval(1999, mode = "str") )
    
UT1()