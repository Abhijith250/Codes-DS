# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:21:48 2021

@author: Abhi
"""

#method1
def lastindex(lis,num):
    if len(lis)==0:
        return -1
    s=lastindex(lis[1:],num) #assume the second half finds value,if it finds it returns index else -1
    if s==-1:
        if lis[0]==num:
            return 0
    else:
        return s+1
    
#method2  
def lastindex2(lis,num):
    if len(lis)==0:
        return -1
    return 1+lastindex(lis[1:],num)
    if lis[0]==num:
            return 0
    
lis=[10,8,9,8,9]
num=9
print(lastindex(lis,num))