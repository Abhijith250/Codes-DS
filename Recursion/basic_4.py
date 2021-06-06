# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:30:41 2021

@author: Abhi
"""
#fibonacci sum
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(3))

#factorial
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(6))

#sum of array
def soa(lis):
    if len(lis)==0 or len(lis)==1:
        return lis[0]
    return lis[0]+soa(lis[1:])
lis=[1,2,3]
print(soa(lis))

#check num present or not

def numpresent(lis,num):
    if len(lis)==0:
        return False
    if lis[0]==num:
        return True
    return numpresent(lis[1:], num)

lis2=[1,2,3,4]
num=4
print(numpresent(lis2,num))
