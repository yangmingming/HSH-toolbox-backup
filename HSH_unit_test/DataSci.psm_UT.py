##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

from __future__ import print_function
from HSH.DataSci.psm import psm
import pandas as pd

if __name__ == "__main__":
    def psm_UT():
        data = pd.read_csv(r"..\test_data\re78.csv", index_col=0)
        control, treatment = data[data["treat"] == 0].values, data[data["treat"] == 1].values

        _, treatment, each_matched = psm(control, 
                                         treatment[10], 
                                         k = 10, 
                                         usecol = [1,2,3,4,5,6], 
                                         stratified_col = [1],  # usecol[2] = 3 也就是第四列 black 作为 第一分层优先级
                                         enable_log = True)
        print(selected_control)
    
    psm_UT()