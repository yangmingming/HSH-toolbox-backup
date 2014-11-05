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
Linear Regression Tool Box

imoprt:
    from HSH.DataSci.linreg import linreg_predict
"""

from __future__ import print_function
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import numpy as np

def glance_2d(x, y):
    """多元线性回归一瞥
    """
    if type(x) != np.ndarray:   # 如果x不是np.ndarray
        x = np.array(x)         # 则转换成np.ndarray
    if len(x.shape) == 1:       # 如果是一维行向量
        x = x[np.newaxis].transpose()   # 转化成列向量
    clf = LinearRegression()
    clf.fit(x,y)
    print("coef = %s, constant = %s" % (clf.coef_, clf.intercept_))
    y2 = clf.predict(x)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x, y, ".")
    plt.plot(x, y2, "-")
    ax.set_xlabel("x") # 子图的 x axis label
    ax.set_ylabel("y")
    plt.show()

def linreg_predict(X, y, X1):
    """多元线性回归预测器
    """
    if type(X) != np.ndarray:   # 如果x不是np.ndarray
        X = np.array(X)         # 则转换成np.ndarray
    if len(X.shape) == 1:       # 如果是一维行向量
        X = X[np.newaxis].transpose()   # 转化成列向量
    if type(X1) != np.ndarray:   # 如果x不是np.ndarray
        X1 = np.array(X1)         # 则转换成np.ndarray
    if len(X1.shape) == 1:       # 如果是一维行向量
        X1 = X1[np.newaxis].transpose()   # 转化成列向量
    clf = LinearRegression()
    clf.fit(X,y)
    return clf.predict(X1) 

def linreg_coef(X, y):
    """多元线性回归预测器
    """
    if type(X) != np.ndarray:   # 如果x不是np.ndarray
        X = np.array(X)         # 则转换成np.ndarray
    if len(X.shape) == 1:       # 如果是一维行向量
        X = X[np.newaxis].transpose()   # 转化成列向量
    clf = LinearRegression()
    clf.fit(X,y)
    return clf.intercept_, clf.coef_

if __name__ == "__main__":
    x = np.array([1,2,3,4,5,6,7,8,9,10])
    y = [3.4, 5.4, 4.3, 2.1, 7.8, 9.2, 11.4, 14.5, 17.3, 19.3]
    glance_2d(x,y)
    print(linreg_predict(x, y, x))
    print(linreg_coef(x, y))