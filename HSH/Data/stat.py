##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

"""

Import:
    from HSH.Data.stat import clear_outlier_onetime, clear_outlier_literally
"""
from __future__ import print_function
import numpy as np

def clear_outlier_onetime(np_array, outlier_criterion = 2):
    """
    INPUT: numpy.array
    """
    m, std = np_array.mean(), np_array.std()
#     print(m, std)  
    return np_array[ np.where( abs(np_array - m) <= outlier_criterion * std )]

def clear_outlier_literally(np_array, outlier_criterion = 2):
    while 1:
        n_before = np_array.size
        np_array = clear_outlier_onetime(np_array, outlier_criterion)
        if n_before == np_array.size:
            return np_array
    

