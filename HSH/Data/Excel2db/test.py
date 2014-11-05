##encoding=utf8

from __future__ import print_function
import pandas as pd
import csv
import time

"""
txt 文件在IO上有绝对的优势
"""
st = time.clock()
df1 = pd.read_excel("easy.xlsx", index_col = False)
print(time.clock() - st)

st = time.clock()
df2 = pd.read_csv("easy.txt", sep = "\t",index_col = False)
print(time.clock() - st)

print(df1.shape)
print(df2.shape)
print(df1.columns)
print(df2.columns)
print(df1.dtypes)
print(df2.dtypes)