##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

from __future__ import print_function
from HSH.DataSci.psm import psm
import pandas as pd

if __name__ == "__main__":
    def psm_UT():
        data = pd.read_csv(r"re78.csv", index_col=0)
        control, treatment = data[data["treat"] == 0].values, data[data["treat"] == 1].values
        psm(control, treatment, k = 1, usecol = [1,2,3,4,5,6], enable_log=True)
    
    psm_UT()