# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:16:17 2021

@author: Abhi
"""
def selectionsort(lis):
    n=len(lis)
    for i in range(len(lis)-1):
        ele=min(lis[i:])
        ind=lis.index(ele)
        lis[i],lis[ind]=lis[ind],lis[i]
    print(lis)
select([3,5,7,2,1])
