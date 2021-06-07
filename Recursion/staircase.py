# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:46:21 2021

@author: Abhi
"""



def staircase(num):
    if num==0 or  num==1:
        return 1
    elif num==2:
        return 2
    elif num==3:
        return 4
    return staircase(num-1)+staircase(num-2)+staircase(num-3)

n=int(input())
print(staircase(n))