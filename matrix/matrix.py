# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:36:50 2021

@author: Abhi
"""

def transpose(matrix):
    res=[]
    for i in range(len(matrix[0])):
        temp=[]
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        res.append(temp)
    return res

def addition(matrix1,matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            c[i][j]=matrix1[i][j]+matrix2[i][j]
    return c

def sub(matrix1,matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            c[i][j]=matrix1[i][j]-matrix2[i][j]
    return c

def multiply(matrix1,matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            c[i][j]=matrix1[i][j]*matrix2[i][j]
    return c