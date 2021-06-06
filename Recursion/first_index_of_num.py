# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:17:14 2021

@author: Abhi
"""


def firstindex(lis,num):
    if len(lis)==0:
        return -1
    if lis[0]==num:
        return 0
    else:
        return 1+firstindex(lis[1:],num)
    
lis=[10,8,9,8,9]
num=9
print(firstindex(lis,num))