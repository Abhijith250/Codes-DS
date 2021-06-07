# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:30:35 2021

@author: Abhi
"""
from sys import setrecursionlimit
setrecursionlimit(5000)
#multiply

def mul(m,n):
    if m==0 or n==0:
        return 0
    return m+mul(m,n-1)

print(mul(10,2))

#sumofdigits

def sod(s):
    if len(s)==0:
        return 0
    return int(s[0])+sod(s[1:])

print(sod("123"))

#geometric sum (1+1/2+1/4+....+1/2^k)

def geometricsum(k):
    if k==0 or k==1:
        return k
    return 1/pow(2,k)+geometricsum(k-1)
print(geometricsum(6))

#check palindrome

def checkpali(s):
    if len(s)==0 or len(s)==1:
        return True
    if s[0]!=s[len(s)-1]:
        return False
    return checkpali(s[1:len(s)-1])

print(checkpali("abhi"))

print(checkpali("abhiihba"))

print(checkpali("aaa"))






