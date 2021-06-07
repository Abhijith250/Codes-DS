# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:08:05 2021

@author: Abhi
"""

def stringtoint(s):
    if len(s)==0:
        return 0
    return int(s[0])*pow(10,len(s)-1)+stringtoint(s[1:])

print(stringtoint("12345"))

#method-1
def countzeros(n):
    k=str(n)
    if len(k)==0:
        return 0
    k=str(n)
    if k[0]=="0":
        return 1+countzeros(k[1:])
    else:
        return countzeros(k[1:])
#method-2

def countzeros2(n):
    if n==0:
        return 1
    if n%10==0:
        return 1+countzeros2(n//10)
    else:
        return countzeros2(n//10)
print(countzeros(100100))
print(countzeros2(10000))
print(countzeros2(0))
print(countzeros(0))
    
    