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
TODO. 删除python脚本注释的小工具
"""


from __future__ import print_function
import os

def delete_one(script_name):
    with open(script_name, "r") as f:
        res = list()
        for line in f.readlines():
            