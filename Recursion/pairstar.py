# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:46:21 2021

@author: Abhi
"""
#pair star(aaa=a*a*a)

def pair(a):
    l=len(a)
    if l==0 or l==1:
        return a
    if a[0]==a[1]:
        return a[0]+"*"+pair(a[1:])
    else:
        return a[0]+pair(a[1:])







i=input()
print(pair(i))
